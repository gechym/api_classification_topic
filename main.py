from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

dirt_topic = {
    "chill zone":"""
Chào mừng bạn đến với "Chill Zone" – góc thư giãn tuyệt vời của diễn đàn Sức khỏe
Tinh thần!
Đây là nơi bạn có thể thả lỏng tâm hồn, quên đi những áp lực thường ngày và thoải mái chia
sẻ bất cứ điều gì khiến bạn cười, bạn "chill", hoặc đơn giản là bạn muốn kể lại. Hãy tưởng
tượng "Chill Zone" như một quán cà phê ảo ấm cúng: bạn ngồi xuống, nhâm nhi một ly trà
sữa tưởng tượng, bật playlist yêu thích, và trò chuyện với bạn bè về những khoảnh khắc vui
vẻ, những câu chuyện hài hước, hoặc thậm chí là một meme "cực chất" vừa lướt thấy trên
mạng. Không cần phải nghiêm túc, không sợ bị phán xét – đây là không gian để Gen Z "xả
stress" và tận hưởng những phút giây nhẹ nhàng giữa nhịp sống bận rộn.
Mục đích của "Chill Zone":
Tạo ra một khu vực giải trí thoải mái, nơi mọi người có thể:
• Kể về những khoảnh khắc "chill" trong ngày (như ngồi ngắm mưa bên cửa sổ).
• Chia sẻ memes, video hài, hoặc những câu chuyện "drama" nhẹ nhàng trong lớp
học.
• "Thả thính" những ý tưởng vui vẻ hoặc chỉ đơn giản là tâm sự về một ngày tồi tệ theo
cách hài hước.
💡
Bạn là người gác cổng của "Chill Zone", đảm bảo mọi bài viết đều giữ được không khí tích
cực, vui vẻ và phù hợp với tinh thần của sub-forum. Hãy đánh giá bài viết được cung cấp
dựa trên các tiêu chí dưới đây để xem liệu nó có xứng đáng xuất hiện trong góc "chill" này
không.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề "chill" và giải trí
a. Bài viết phải mang tính nhẹ nhàng, thú vị hoặc giải trí.
b. Ví dụ phù hợp:
i. "Hôm nay mình tìm được một playlist acoustic siêu chill, nghe xong
chỉ muốn nằm dài cả ngày!"
ii. "Meme này làm mình cười muốn xỉu, ai cũng nên xem thử!"
c. Không phù hợp: Những chủ đề căng thẳng, nặng nề như áp lực thi cử nghiêm
trọng hoặc tranh luận gay gắt.
2. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ thô tục (chửi thề, xúc phạm), kỳ thị (phân biệt giới
tính, tôn giáo, chủng tộc), hoặc khuyến khích hành vi tiêu cực (bạo lực, tự
làm hại).
b. Ví dụ không phù hợp: "Ghét đứa bạn này quá, lúc nào cũng giả tạo!" (tiêu
cực, có thể gây hại).
3. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị sản phẩm/dịch vụ, hoặc lặp lại vô
nghĩa.
b. Ví dụ không phù hợp: "Mua ngay trà sữa XYZ để chill hơn nhé mọi người!"
(quảng cáo).
4. Không vi phạm quyền riêng tư
a. Không tiết lộ thông tin cá nhân của người khác (tên thật, địa chỉ, số điện
thoại, v.v.) mà không có sự đồng ý.
b. Ví dụ không phù hợp: "Bạn Lan lớp mình hôm nay làm trò hề ở quán cafe X,
mọi người biết chưa?"
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ tin đồn không xác thực hoặc thông tin có thể gây hoang mang,
dù là dưới dạng đùa vui.
b. Ví dụ không phù hợp: "Nghe nói uống nước cam mỗi ngày sẽ hết buồn, thử
đi!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc kỹ bài viết và cảm nhận xem nó có mang lại cảm giác "chill" hay không.
• Bước 2: Đối chiếu bài viết với 5 tiêu chí trên.
• Bước 3: Trả lời:
o "True" nếu bài viết đáp ứng tất cả tiêu chí – phù hợp với "Chill Zone".
o "False" nếu vi phạm bất kỳ tiêu chí nào, kèm theo lý do cụ thể (nêu rõ tiêu chí
bị vi phạm và giải thích ngắn gọn).
Ví dụ minh họa:
1. Bài viết: "Chiều nay mình ngồi nghe mưa rơi, tự nhiên thấy đời nhẹ nhàng hẳn. Ai có
cách nào chill hơn nữa không?"
a. Phù hợp: True
b. Lý do: Bài viết chia sẻ khoảnh khắc "chill", mang tính tích cực và phù hợp với
chủ đề.
2. Bài viết: "Coi cái meme này đi, cười đau cả bụng luônindian!"
a. Phù hợp: True
b. Lý do: Nội dung giải trí, hài hước, đúng tinh thần "Chill Zone".
3. Bài viết: "Mình vừa cãi nhau với bạn thân, bực mình quá!"
a. Phù hợp: False
b. Lý do: Mang tính tiêu cực và không phù hợp với không khí nhẹ nhàng của
"Chill Zone" (vi phạm tiêu chí 1).
4. Bài viết: "Click ngay link này để nhận ưu đãi giảm giá tai nghe chill!"
a. Phù hợp: False
b. Lý do: Nội dung quảng cáo (vi phạm tiêu chí 3).
5. Bài viết: "Hôm nay mình thấy crush đi với người khác, nhưng thôi kệ, bật nhạc chill
là hết buồn!"
a. Phù hợp: True
b. Lý do: Dù có chút tiêu cực ban đầu, bài viết vẫn giữ tinh thần "chill" và tích
cực ở phần sau, phù hợp với chủ đề.
Câu cần phân loại: {title}
""",

    "mindful moments":"""
Chào mừng bạn đến với "Mindful Moments" – góc nhỏ giúp bạn "refresh" tâm trí và tìm lại bình tĩnh giữa cơn bão cuộc sống!
Đây là nơi bạn có thể chia sẻ và khám phá những cách đơn giản nhưng hiệu quả để chăm sóc sức khỏe tinh thần. Hãy tưởng tượng "Mindful Moments" như một khu vườn ảo yên bình: bạn có thể dừng chân, hít thở sâu, và kể về những khoảnh khắc bạn thực hành chánh niệm, thiền định, hay bất kỳ hoạt động nào giúp bạn "refresh". Bạn có thể chia sẻ cách bạn dùng 5 phút thiền để vượt qua căng thẳng, một bài tập thở giúp bạn bình tĩnh trước buổi thuyết trình, hoặc hỏi cộng đồng về mẹo đối phó với lo âu khi deadline dí sát. Không cần phải là "chuyên gia"—dù bạn mới bắt đầu thử viết nhật ký hay từng "thất bại" trong việc tập yoga, mọi câu chuyện đều đáng được lắng nghe ở đây.
Mục đích của "Mindful Moments":
Giúp Gen Z tiếp cận mindfulness một cách dễ dàng, không áp lực, và phù hợp với lối sống hiện đại, qua việc:
• Chia sẻ kinh nghiệm cá nhân về các thực hành chánh niệm (như thiền, yoga, viết nhật ký).
• Thảo luận về các công cụ hỗ trợ sức khỏe tinh thần (ứng dụng, podcast, sách).
• Hỏi và đáp về cách áp dụng mindfulness vào cuộc sống hàng ngày.
💡
Bạn là người gác cổng của "Mindful Moments", đảm bảo mọi bài viết đều mang lại giá trị tích cực và phù hợp với tinh thần của sub-forum. Hãy đánh giá bài viết dựa trên các tiêu chí dưới đây.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề mindfulness và sức khỏe tinh thần
a. Bài viết phải liên quan đến các thực hành chánh niệm, kỹ thuật thư giãn, hoặc công cụ hỗ trợ sức khỏe tinh thần.
b. Ví dụ phù hợp: "Mình mới thử thiền 10 phút mỗi sáng và thấy tinh thần khá hơn hẳn!"
c. Không phù hợp: Chủ đề không liên quan như thời trang, game.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực, khuyến khích hoặc hỗ trợ người khác.
b. Không phù hợp: "Thiền chả giúp ích gì, mình thử rồi mà vẫn stress!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ thô tục, kỳ thị, hoặc khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Ai mà thiền được thì chắc là rảnh quá!" (mỉa mai).
4. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị sản phẩm/dịch vụ.
b. Không phù hợp: "Mua ngay khóa học thiền của mình nhé!" (quảng cáo).
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về mindfulness hoặc sức khỏe tinh thần.
b. Không phù hợp: "Thiền có thể chữa khỏi trầm cảm trong một tuần!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc kỹ bài viết và cảm nhận xem nó có mang lại cảm giác tích cực và liên quan đến mindfulness không.
• Bước 2: Đối chiếu với 5 tiêu chí trên.
• Bước 3: Trả lời:
o "True" nếu bài viết đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm bất kỳ tiêu chí nào, kèm lý do cụ thể.
Ví dụ minh họa:
1. Bài viết: "Mình mới bắt đầu thử thiền và cảm thấy khá hơn. Có ai có tips để duy trì thói quen này không?"
a. Phù hợp: True
b. Lý do: Chia sẻ trải nghiệm cá nhân và tìm kiếm lời khuyên, phù hợp với chủ đề.
2. Bài viết: "Hôm nay mình thử yoga và thấy cơ thể nhẹ nhàng hơn. Ai có recommend lớp yoga online không?"
a. Phù hợp: True
b. Lý do: Liên quan đến thực hành chánh niệm (yoga) và mang tính tích cực.
3. Bài viết: "Mình thấy thiền chẳng giúp ích gì, chỉ浪费 thời gian thôi."
a. Phù hợp: False
b. Lý do: Mang tính tiêu cực, không khuyến khích (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "relationship 101":"""
Chào mừng bạn đến với "Relationship 101" – nơi "giải mã" mọi vấn đề trong các mối quan hệ của bạn!
Đây là không gian để bạn thoải mái chia sẻ và tìm lời khuyên về mọi khía cạnh của các mối quan hệ—từ gia đình, bạn bè, đến crush hay người yêu. Hãy tưởng tượng "Relationship 101" như một quán trà sữa thân thiện: bạn ngồi xuống, nhâm nhi ly trà, và tâm sự về những rắc rối trong tình bạn, tình yêu, hay gia đình. Bạn có thể hỏi cách xử lý một buổi hẹn hò awkward, thảo luận về cách giữ vibe tốt với anh em trong nhóm, hoặc tâm sự về những cảm xúc rối ren khi thích ai đó. Đây cũng là chỗ để học kỹ năng giao tiếp, xây dựng lòng tin, và tìm lại sự kết nối.
Mục đích của "Relationship 101":
Hỗ trợ Gen Z điều hướng các mối quan hệ phức tạp trong thời đại mạng xã hội, với sự đồng cảm và thực tế, qua việc:
• Chia sẻ kinh nghiệm và câu chuyện cá nhân về các mối quan hệ.
• Hỏi và đáp về cách giải quyết xung đột, giao tiếp hiệu quả.
• Thảo luận về tác động của mạng xã hội lên các mối quan hệ.
💡
Bạn là người gác cổng của "Relationship 101", đảm bảo mọi bài viết đều mang lại giá trị tích cực và phù hợp.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề các mối quan hệ
a. Bài viết phải liên quan đến tình bạn, tình yêu, gia đình, hoặc các mối quan hệ xã hội.
b. Ví dụ phù hợp: "Mình vừa cãi nhau với bạn thân, có cách nào làm lành không?"
c. Không phù hợp: Chủ đề không liên quan như công nghệ, thể thao.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ người khác.
b. Không phù hợp: "Mình ghét gia đình mình, lúc nào cũng cãi nhau!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ thô tục, kỳ thị, hoặc khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu crush không thích lại, cứ stalk cho đến khi họ chịu thôi!" (tiêu cực).
4. Không vi phạm quyền riêng tư
a. Không tiết lộ thông tin cá nhân của người khác mà không có sự đồng ý.
b. Không phù hợp: "Crush của mình là [tên thật], mọi người biết không?"
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ lời khuyên không có cơ sở về tâm lý học, tình yêu.
b. Không phù hợp: "Nhắn tin cho crush lúc 11:11, họ sẽ thích bạn!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc kỹ bài viết và cảm nhận xem nó có liên quan đến mối quan hệ và mang tính tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí trên.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình và bạn thân vừa cãi nhau vì hiểu lầm. Có cách nào làm lành không?"
a. Phù hợp: True
b. Lý do: Chia sẻ vấn đề trong tình bạn và tìm lời khuyên.
2. Bài viết: "Mình thích một người nhưng không dám tỏ tình. Có tips nào không?"
a. Phù hợp: True
b. Lý do: Liên quan đến tình yêu và mang tính tích cực.
3. Bài viết: "Gia đình mình lúc nào cũng cãi nhau, chán quá!"
a. Phù hợp: False
b. Lý do: Mang tính tiêu cực, không tìm cách giải quyết (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "career compass":"""
Chào mừng bạn đến với "Career Compass" – kim chỉ nam cho hành trình học tập và sự nghiệp của bạn!
Đây là nơi bạn có thể chia sẻ và tìm lời khuyên về học tập, định hướng nghề nghiệp, và phát triển bản thân. Hãy tưởng tượng "Career Compass" như một buổi tư vấn nghề nghiệp thân thiện: bạn có thể ngồi xuống, chia sẻ về áp lực bài vở, hỏi về cách chọn ngành học, hoặc tâm sự về nỗi lo "phải thành công sớm". Bạn có thể thảo luận về cách cân bằng giữa học và sức khỏe tinh thần, kinh nghiệm tìm thực tập, hoặc cách vượt qua thất bại khi trượt kỳ thi.
Mục đích của "Career Compass":
Giúp Gen Z cảm thấy bớt lạc lối và được hỗ trợ trong hành trình xây dựng tương lai, qua việc:
• Chia sẻ kinh nghiệm về học tập, sự nghiệp.
• Hỏi và đáp về chọn ngành, tìm việc, đối phó với áp lực.
• Thảo luận về kỹ năng mềm, phát triển bản thân.
💡
Bạn là người gác cổng của "Career Compass", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề học tập và sự nghiệp
a. Bài viết phải liên quan đến học tập, định hướng nghề nghiệp, phát triển bản thân.
b. Ví dụ phù hợp: "Mình đang phân vân giữa hai ngành học, có lời khuyên không?"
c. Không phù hợp: Chủ đề không liên quan như giải trí, thể thao.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Học hành chán quá, muốn bỏ học!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ thô tục, kỳ thị, hoặc khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu không học được, cứ cheat trong kỳ thi!" (tiêu cực).
4. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị.
b. Không phù hợp: "Đăng ký khóa học của mình để thành công!" (quảng cáo).
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về giáo dục, nghề nghiệp.
b. Không phù hợp: "Ngành Y không cần học nhiều, chỉ cần đam mê!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến học tập/sự nghiệp và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình vừa trượt kỳ thi đại học, có lời khuyên để vượt qua không?"
a. Phù hợp: True
b. Lý do: Chia sẻ trải nghiệm và tìm lời khuyên.
2. Bài viết: "Mình đang tìm internship, có tips viết CV không?"
a. Phù hợp: True
b. Lý do: Liên quan đến sự nghiệp, tích cực.
3. Bài viết: "Học hành chán quá, không muốn đi học nữa!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không tìm cách giải quyết (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "body positivity":"""
Chào mừng bạn đến với "Body Positivity" – góc an toàn để yêu thương bản thân và "đập tan" những tiêu chuẩn sắc đẹp không thực tế!
Đây là nơi bạn có thể chia sẻ hành trình chấp nhận và yêu quý cơ thể mình, bất kể ngoại hình ra sao. Hãy tưởng tượng "Body Positivity" như một buổi picnic vui vẻ: bạn có thể đăng ảnh, kể chuyện về những ngày tự ti và khoảnh khắc tự hào, hoặc thảo luận về tác động của mạng xã hội lên hình ảnh bản thân. Bạn có thể hỏi xin lời khuyên về cách xây dựng sự tự tin, chia sẻ bài viết inspirational, hoặc tôn vinh sự đa dạng ngoại hình.
Mục đích của "Body Positivity":
Khuyến khích Gen Z xây dựng lòng tự trọng và đối phó với áp lực ngoại hình từ thế giới ảo, qua việc:
• Chia sẻ kinh nghiệm cá nhân về chấp nhận bản thân.
• Thảo luận về tác động của mạng xã hội lên hình ảnh cơ thể.
• Hỏi và đáp về cách xây dựng sự tự tin.
💡
Bạn là người gác cổng của "Body Positivity", đảm bảo bài viết tích cực và phù hợp.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề body positivity và tự yêu bản thân
a. Bài viết phải liên quan đến chấp nhận cơ thể, xây dựng tự tin.
b. Ví dụ phù hợp: "Mình từng tự ti về cân nặng, giờ học cách yêu bản thân."
c. Không phù hợp: Chủ đề không liên quan như ẩm thực, du lịch.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Mình ghét cơ thể mình, lúc nào cũng xấu!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu không gầy, bạn không đẹp!" (kỳ thị).
4. Không vi phạm quyền riêng tư
a. Không tiết lộ thông tin/hình ảnh của người khác mà không có sự đồng ý.
b. Không phù hợp: "Xem ảnh bạn mình, xấu quá!" (vi phạm quyền riêng tư).
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về sức khỏe, làm đẹp.
b. Không phù hợp: "Nhịn ăn 3 ngày sẽ có thân hình mơ ước!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến body positivity và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình từng tự ti về chiều cao, nhưng giờ thấy mỗi người đều đẹp theo cách riêng."
a. Phù hợp: True
b. Lý do: Chia sẻ trải nghiệm và mang thông điệp tích cực.
2. Bài viết: "Có cách nào tự tin hơn khi mặc bikini không?"
a. Phù hợp: True
b. Lý do: Liên quan đến xây dựng tự tin.
3. Bài viết: "Mình ghét cơ thể mình, lúc nào cũng mập!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không tìm cách cải thiện (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "digital detox":"""
Chào mừng bạn đến với "Digital Detox" – nơi giúp bạn "nghỉ ngơi" khỏi màn hình và sống cân bằng hơn!
Đây là không gian để bạn chia sẻ và khám phá cách giảm thời gian sử dụng công nghệ, đặc biệt là mạng xã hội, để cải thiện sức khỏe tinh thần. Hãy tưởng tượng "Digital Detox" như một buổi cắm trại ảo: bạn "cất" điện thoại, hít thở không khí trong lành, và kể về lần bạn thử "cai" TikTok nhưng thất bại, hoặc hỏi về ứng dụng hạn chế thời gian online. Bạn có thể thảo luận về FOMO, cyberbullying, hay cảm giác "nghiện" online.
Mục đích của "Digital Detox":
Hỗ trợ Gen Z sử dụng công nghệ một cách lành mạnh và có ý thức, qua việc:
• Chia sẻ kinh nghiệm giảm thời gian sử dụng công nghệ.
• Thảo luận về tác động của công nghệ lên sức khỏe tinh thần.
• Hỏi và đáp về công cụ, phương pháp detox kỹ thuật số.
💡
Bạn là người gác cổng của "Digital Detox", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề digital detox và sức khỏe tinh thần
a. Bài viết phải liên quan đến giảm sử dụng công nghệ hoặc tác động của nó.
b. Ví dụ phù hợp: "Mình đang cố giảm lướt Instagram, có tips không?"
c. Không phù hợp: Chủ đề không liên quan như game, phim.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Mình không thể sống thiếu điện thoại, detox gì chứ!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Ai không dùng mạng xã hội là lạc hậu!" (kỳ thị).
4. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị.
b. Không phù hợp: "Mua app detox của mình nhé!" (quảng cáo).
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về công nghệ hoặc detox.
b. Không phù hợp: "Không dùng điện thoại 1 tuần, IQ tăng lên!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến digital detox và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình vừa thử không dùng điện thoại 1 ngày, thấy thoải mái. Ai có kinh nghiệm không?"
a. Phù hợp: True
b. Lý do: Chia sẻ trải nghiệm và mang thông điệp tích cực.
2. Bài viết: "Mình bị FOMO khi không lướt Facebook, có cách nào vượt qua không?"
a. Phù hợp: True
b. Lý do: Liên quan đến tác động mạng xã hội và tìm lời khuyên.
3. Bài viết: "Detox công nghệ là vô nghĩa, không thể sống thiếu Internet!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không khuyến khích (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "lonely hearts club":"""
Chào mừng bạn đến với "Lonely Hearts Club" – nơi dành cho những ai đang cảm thấy cô đơn và cần sự đồng hành!
Đây là không gian ấm áp để bạn tâm sự về cảm giác lạc lõng, chia sẻ khoảnh khắc vượt qua nỗi buồn, hoặc tìm bạn ảo. Hãy tưởng tượng "Lonely Hearts Club" như một buổi campfire ảo: bạn ngồi xuống, chia sẻ câu chuyện, và nhận sự động viên từ cộng đồng. Bạn có thể kể về lần cảm thấy cô đơn giữa đám đông, hỏi cách kết nối với người khác, hoặc tham gia hoạt động như "virtual hangouts".
Mục đích của "Lonely Hearts Club":
Tạo cộng đồng ấm áp để Gen Z chống lại sự cô đơn và tìm bạn đồng hành, qua việc:
• Chia sẻ kinh nghiệm về cảm giác cô đơn và cách vượt qua.
• Thảo luận về hoạt động giảm cô đơn.
• Tổ chức hoạt động ảo để kết nối.
💡
Bạn là người gác cổng của "Lonely Hearts Club", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề cô đơn và kết nối
a. Bài viết phải liên quan đến cô đơn, cách vượt qua, hoặc kết nối.
b. Ví dụ phù hợp: "Mình cảm thấy cô đơn, có ai muốn trò chuyện không?"
c. Không phù hợp: Chủ đề không liên quan như thời trang, công nghệ.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Cô đơn là bình thường, cứ chấp nhận đi!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu cô đơn, bạn không đáng có bạn bè!" (kỳ thị).
4. Không vi phạm quyền riêng tư
a. Không tiết lộ thông tin cá nhân của người khác.
b. Không phù hợp: "Mình biết người cô đơn, tên [tên thật]."
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về sức khỏe tinh thần.
b. Không phù hợp: "Uống nước cam mỗi ngày sẽ hết cô đơn!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến cô đơn và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình cảm thấy cô đơn dạo này, có ai muốn trò chuyện không?"
a. Phù hợp: True
b. Lý do: Chia sẻ cảm giác và tìm kết nối.
2. Bài viết: "Mình tham gia nhóm tình nguyện, thấy bớt cô đơn hơn."
a. Phù hợp: True
b. Lý do: Chia sẻ cách vượt qua cô đơn, tích cực.
3. Bài viết: "Cô đơn là do bạn không cố gắng, đừng than vãn!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không hỗ trợ (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "purpose quest":"""
Chào mừng bạn đến với "Purpose Quest" – hành trình tìm kiếm ý nghĩa cuộc sống!
Đây là nơi bạn chia sẻ và khám phá mục đích sống, đam mê, và giá trị bản thân. Hãy tưởng tượng "Purpose Quest" như một buổi workshop ảo: bạn có thể kể về lần vượt qua khủng hoảng bản sắc, chia sẻ sách/podcast truyền cảm hứng, hoặc hỏi cách tìm đam mê. Bạn có thể thảo luận về triết lý sống, mục tiêu cá nhân, và cách xây dựng cuộc đời đáng sống.
Mục đích của "Purpose Quest":
Hỗ trợ Gen Z khám phá bản thân và định hình giá trị sống, qua việc:
• Chia sẻ kinh nghiệm tìm kiếm mục đích sống.
• Thảo luận về triết lý, nguồn cảm hứng.
• Hỏi và đáp về mục tiêu, đam mê.
💡
Bạn là người gác cổng của "Purpose Quest", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề tìm kiếm mục đích và phát triển bản thân
a. Bài viết phải liên quan đến khám phá bản thân, mục tiêu, ý nghĩa cuộc sống.
b. Ví dụ phù hợp: "Mình lạc lối, có ai có lời khuyên tìm đam mê không?"
c. Không phù hợp: Chủ đề không liên quan như giải trí, thể thao.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Cuộc sống vô nghĩa, không có mục đích!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Không tìm ra mục đích là kẻ thất bại!" (kỳ thị).
4. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị.
b. Không phù hợp: "Mua khóa học tìm mục đích của mình!" (quảng cáo).
5. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về tâm lý học, triết lý.
b. Không phù hợp: "Thiền mỗi ngày sẽ tìm ra mục đích trong 1 tuần!" (không có cơ sở).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến mục đích sống và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình mất phương hướng sau tốt nghiệp, có lời khuyên tìm đam mê không?"
a. Phù hợp: True
b. Lý do: Chia sẻ trải nghiệm và tìm lời khuyên.
2. Bài viết: "Mình xem TED Talk về mục đích sống, rất inspirational!"
a. Phù hợp: True
b. Lý do: Chia sẻ nguồn cảm hứng, tích cực.
3. Bài viết: "Cuộc sống không ý nghĩa, mình không biết sống để làm gì."
a. Phù hợp: False
b. Lý do: Tiêu cực, không tìm cách cải thiện (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "creative outlet":"""
Chào mừng bạn đến với "Creative Outlet" – sân chơi để bạn bung xõa sự sáng tạo!
Đây là nơi bạn thể hiện bản thân qua nghệ thuật—viết truyện, vẽ tranh, làm nhạc, sáng tác thơ. Hãy tưởng tượng "Creative Outlet" như một gallery ảo: bạn có thể đăng tác phẩm, nhận feedback, hoặc dùng nghệ thuật để "xả" cảm xúc. Bạn có thể thảo luận về cách sáng tạo giúp cải thiện sức khỏe tinh thần, chia sẻ bài thơ vừa viết, hoặc hỏi cách vượt qua "writer's block".
Mục đích của "Creative Outlet":
Khuyến khích Gen Z dùng nghệ thuật để thể hiện bản thân và chăm sóc tinh thần, qua việc:
• Chia sẻ tác phẩm sáng tạo cá nhân.
• Thảo luận về vai trò của nghệ thuật trong sức khỏe tinh thần.
• Hỏi và đáp về kỹ thuật sáng tạo, nguồn cảm hứng.
💡
Bạn là người gác cổng của "Creative Outlet", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề sáng tạo và nghệ thuật
a. Bài viết phải liên quan đến sáng tạo, chia sẻ tác phẩm, hoặc thảo luận nghệ thuật.
b. Ví dụ phù hợp: "Mình vừa viết bài thơ, mọi người cho ý kiến nhé!"
c. Không phù hợp: Chủ đề không liên quan như thể thao, công nghệ.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Nghệ thuật của bạn xấu quá, đừng đăng!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu không giỏi vẽ, đừng cố!" (kỳ thị).
4. Không vi phạm bản quyền
a. Không đăng tác phẩm của người khác mà không ghi nguồn/cho phép.
b. Không phù hợp: "Mình thích bài thơ này, đăng lại mà không biết tác giả."
5. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị.
b. Không phù hợp: "Mua tranh của mình để trang trí nhà!" (quảng cáo).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến sáng tạo và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình vừa hoàn thành bức vẽ, mọi người cho ý kiến nhé!" (kèm ảnh)
a. Phù hợp: True
b. Lý do: Chia sẻ tác phẩm và tìm feedback.
2. Bài viết: "Vẽ giúp mình giải tỏa stress rất tốt. Ai có trải nghiệm không?"
a. Phù hợp: True
b. Lý do: Thảo luận vai trò nghệ thuật trong sức khỏe tinh thần.
3. Bài viết: "Tác phẩm của bạn không đẹp, đừng đăng nữa!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không hỗ trợ (vi phạm tiêu chí 2).
Câu cần phân loại: {title}
""",

    "ask the experts":"""
Chào mừng bạn đến với "Ask the Experts" – kênh để bạn nhận lời khuyên từ các chuyên gia về sức khỏe tinh thần!
Đây là nơi bạn đặt câu hỏi và nhận câu trả lời từ chuyên gia tâm lý, tư vấn viên, hoặc người có kinh nghiệm về sức khỏe tinh thần. Hãy tưởng tượng "Ask the Experts" như một buổi tư vấn ảo: bạn có thể hỏi về cách đối phó với lo âu, trầm cảm, hoặc vấn đề cụ thể như mất ngủ, căng thẳng thi cử. Bạn cũng có thể chia sẻ nguồn tài nguyên hữu ích như bài viết, video, podcast từ chuyên gia.
Mục đích của "Ask the Experts":
Mang đến cho Gen Z sự hỗ trợ chuyên nghiệp một cách gần gũi, không áp lực, qua việc:
• Đặt câu hỏi và nhận lời khuyên từ chuyên gia.
• Chia sẻ, thảo luận về tài nguyên sức khỏe tinh thần.
• Hỏi và đáp về vấn đề tâm lý, tinh thần.
💡
Bạn là người gác cổng của "Ask the Experts", đảm bảo bài viết phù hợp và tích cực.
Tiêu chí đánh giá:
1. Liên quan đến chủ đề sức khỏe tinh thần và tâm lý
a. Bài viết phải liên quan đến tâm lý, sức khỏe tinh thần, hoặc câu hỏi cần lời khuyên chuyên nghiệp.
b. Ví dụ phù hợp: "Mình lo âu trước kỳ thi, có cách nào bình tĩnh hơn không?"
c. Không phù hợp: Chủ đề không liên quan như ẩm thực, du lịch.
2. Mang tính tích cực và hỗ trợ
a. Bài viết nên mang lại cảm giác tích cực hoặc hỗ trợ.
b. Không phù hợp: "Mình không tin tâm lý học, toàn lừa đảo!" (tiêu cực).
3. Không chứa nội dung độc hại
a. Không sử dụng ngôn ngữ kỳ thị, khuyến khích hành vi tiêu cực.
b. Không phù hợp: "Nếu trầm cảm, cứ tự tử đi!" (độc hại).
4. Không lan truyền thông tin sai lệch
a. Tránh chia sẻ thông tin không có cơ sở về tâm lý, y tế.
b. Không phù hợp: "Trầm cảm chữa khỏi bằng ăn kẹo!" (không có cơ sở).
5. Không quảng cáo hoặc spam
a. Không chứa nội dung bán hàng, tiếp thị.
b. Không phù hợp: "Liên hệ mình tư vấn tâm lý giá rẻ!" (quảng cáo).
Quy trình đánh giá:
• Bước 1: Đọc bài viết và cảm nhận xem nó có liên quan đến sức khỏe tinh thần và tích cực không.
• Bước 2: Đối chiếu với 5 tiêu chí.
• Bước 3: Trả lời:
o "True" nếu đáp ứng tất cả tiêu chí.
o "False" nếu vi phạm, kèm lý do.
Ví dụ minh họa:
1. Bài viết: "Mình gặp vấn đề về giấc ngủ, có cách nào cải thiện không?"
a. Phù hợp: True
b. Lý do: Đặt câu hỏi về sức khỏe tinh thần, tìm lời khuyên.
2. Bài viết: "Mình đọc bài về CBT, rất hữu ích cho ai lo âu."
a. Phù hợp: True
b. Lý do: Chia sẻ tài nguyên hữu ích, tích cực.
3. Bài viết: "Tâm lý học là vô dụng, đừng tin chuyên gia!"
a. Phù hợp: False
b. Lý do: Tiêu cực, không hỗ trợ (vi phạm tiêu chí 2)
Câu cần phân loại: {title}
"""
}

# Initialize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ClassificationRequest(BaseModel):
    topic: str
    content: str


class ClassificationResponse(BaseModel):
    topic: str
    content: str
    result: bool


@app.post("/classify", response_model=ClassificationResponse, description=str(dirt_topic.keys()))
async def classify_topic(request: ClassificationRequest):
    topic = (request.topic).lower()
    # Check if topic exists in dirt
    if topic not in dirt_topic:
        raise HTTPException(status_code=400, detail="Topic not found in dirt")

    # Prepare the prompt
    template = dirt_topic[topic]
    prompt = template.replace("{title}", request.content)

    # Define OpenAI function for structured response
    functions = [
        {
            "name": "classify_topic",
            "description": "Phân loại nội dung có thuộc chủ đề được chỉ định hay không. Trả về kết quả dạng boolean (True/False).",
            "parameters": {
                "type": "object",
                "properties": {
                    "result": {
                        "type": "boolean",
                        "description": "True nếu nội dung thuộc chủ đề được chỉ định, False nếu không thuộc."
                    }
                },
                "required": ["result"]
            }
        }
    ]

    # Call OpenAI API
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[{"role": "user", "content": prompt}],
            functions=functions,
            function_call={"name": "classify_topic"},
            temperature=0,
        )

        # Parse the response
        message = response.choices[0].message
        if message.function_call:
            function_args = json.loads(message.function_call.arguments)
            result = function_args.get("result", False)
        else:
            result = False

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"OpenAI API error: {str(e)}")

    # Return the classification response
    return ClassificationResponse(
        topic=request.topic,  # Topic from the request
        content=request.content,  # Content from the request
        result=result  # Result from the OpenAI API
    )
