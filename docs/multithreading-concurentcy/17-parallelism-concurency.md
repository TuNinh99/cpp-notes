---
title: "Parallelism & Concurency"
---

# 17. Parallelism & Concurency

## 🧾 Content

1. concurency - đồng thời
- Bản chất: xử lý nhiều việc cùng một lúc (nhưng không nhất thiết phải cùng 1 thời điểm)
- Số lượng nhân CPU: Có thể chạy trên nhân CPU bằng cách chia nhỏ thời gian
- Cách hoạt động: chạy 1 chút việc A ---&gt; dừng việc A ---&gt; chạy 1 chút việc B
- Mục tiêu: giải quyết sự chờ đợi (chờ phản hồi ở ổ cứng/mạng,...)

2. parallelism - song song
- Bản chất: thực hiện nhiều việc tại 1 thời điểm vật lý
- Số lượng nhân CPU: bắt buộc phải có nhiều nhân CPU
- Cách hoạt động: việc A & việc B chạy trên 2 đường thẳng song song riêng biệt
- Mục tiêu: tăng tốc độ xử lý (tính toán đồ họa, render video)

## 📝 Note

1. Concurentcy - 1 người làm nhiều việc
Bạn đang nấu ăn. Bạn bật bếp đun nước, trong lúc đợi nước sôi, bạn quay sang thái hành. Sau đó nước sôi, bạn cho mì vào, rồi lại quay lại thái thịt.
Thực tế: Tại một thời điểm, tay bạn chỉ làm một việc (hoặc thái hành, hoặc cho mì).
Kết quả: Bạn hoàn thành bữa ăn nhanh hơn vì tận dụng thời gian "chết" của bếp. Đây là cách 1 nhân CPU xử lý nhiều luồng.

2. Parallelism (Song song) - Nhiều người làm nhiều việc
Bạn rủ thêm một người bạn nữa vào bếp. Bạn thái hành, người bạn kia đứng canh nồi nước sôi.
Thực tế: Cả hai việc thái hành và đun nước đang diễn ra cùng một lúc.
Kết quả: Công việc xong nhanh hơn hẳn vì có 2 nguồn lực (2 nhân CPU) hoạt động độc lập.
