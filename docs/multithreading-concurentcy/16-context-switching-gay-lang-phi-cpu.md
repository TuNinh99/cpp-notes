---
title: "Context Switching -> gây lãng phí CPU"
---

# 16. Context Switching -> gây lãng phí CPU

## 🧾 Content

CPU trên thực tế chỉ có thể làm 1 việc tại 1 thời điểm trên mỗi nhân, để tạo cảm giác có nhiều luồng chạy song song, hệ điều hành phải đảo qua đảo lại giữa các luồng cực kì nhanh
1. Nó làm gì? Khi chuyển từ Luồng A sang Luồng B, CPU phải:
- Tạm dừng Luồng A.
- Lưu trạng thái hiện tại (giá trị các thanh ghi, con trỏ lệnh, ngăn xếp...) vào bộ nhớ.
- Tải trạng thái đã lưu trước đó của Luồng B lên.
- Tiếp tục chạy Luồng B
2. Tại sao là vấn đề?
Quá trình lưu và tải này không tạo ra kết quả cho ứng dụng nhưng lại chiếm chu kỳ CPU. Nếu bạn tạo quá nhiều luồng (vượt xa số nhân thực tế), CPU sẽ dành phần lớn thời gian chỉ để "đổi chỗ" thay vì làm việc.
3. Hệ lụy: Làm mất dữ liệu trong Cache L1/L2. Khi luồng mới nhảy vào, dữ liệu nó cần có thể không có sẵn trong cache nhanh của CPU, buộc CPU phải đợi đọc từ RAM (chậm hơn hàng trăm lần).

## 📝 Note


