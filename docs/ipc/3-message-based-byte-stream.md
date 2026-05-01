---
title: "Message-based & Byte-stream"
---

# 3. Message-based & Byte-stream

## 🧾 Content

- byte-stream: dữ liệu đc truyền như 1 dòng liên tục các byte, k có ranh giới các byte, 
ví dụ: nếu write("Hello) | write("World), read(8bytes) thì data có thể là : HelloWor
tức là người dùng sẽ phải tự control message

- message-based: dữ liệu đc gửi theo từng message riêng biệt, rõ ràng. kernel sẽ đảm bảo tính đúng đắn của các message. cũng là ví dụ trên Msg1: Hello; Msg2: World =&gt; nhận đúng Hello World
không bao giờ bị như byte-stream

## 📝 Note


