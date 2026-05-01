---
title: "Memory Usage -> gây lãng phí RAM"
---

# 18. Memory Usage -> gây lãng phí RAM

## 🧾 Content

- mỗi luồng không "miễn phí", nó tiêu tốn một lượng RAM nhất định để duy trì sự tồn tại.
- Thread Stack: Mỗi luồng cần một không gian bộ nhớ riêng (Stack) để lưu trữ các biến cục bộ và lịch sử gọi hàm. Tùy ngôn ngữ và hệ điều hành, con số này thường từ 512KB đến 2MB mỗi luồng.

## 📝 Note

Ví dụ: Nếu bạn tạo 1.000 luồng, bạn có thể mất ngay ~1GB đến 2GB RAM chỉ để giữ cho các luồng đó "đứng đợi", chưa tính dữ liệu thực tế chúng xử lý.
Thread Control Block (TCB): Hệ điều hành cần một cấu trúc dữ liệu nhỏ để quản lý thông tin của mỗi luồng (ID, độ ưu tiên, trạng thái). Khi số luồng lên tới hàng nghìn, việc quản lý danh sách này cũng làm chậm bộ lập lịch (Scheduler) của hệ thống.
