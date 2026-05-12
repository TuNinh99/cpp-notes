---
title: "4. Biến static & biến global khác nhau như thế nào?"
sidebar_position: 4
---

# 4. Biến static & biến global khác nhau như thế nào?

## 🧾 Content

1. Biến global
- Mục đích: chia sẻ dử liệu chung cho cả hệ thống
- Khai báo ngoài hàm
- Có thể sử dụng từ bất kì đâu trong toàn bộ dự án

2. Biến static
- Mục đích: bảo toàn giá trị giữa các lần gọi &amp; giới hạn truy cập để bảo vệ giữ liệu

- Static local:
+) chỉ có thể truy cập trong hàm khai báo nó
+) giá trị đc bảo toàn giữa các lần gọi hàm

- Static global:
+) chỉ truy cập đc trong file chưa nó
+) giúp tránh xung đột tên

Note:
- Out of scope -&gt; luôn không dùng đc biến đó, kể cả static
- Nếu lưu đc đ/c, vẫn dùng được bth
&lt; vì biến static lưu ở Data thay vì Stack &gt;
- Ví dụ

## 📝 Note


