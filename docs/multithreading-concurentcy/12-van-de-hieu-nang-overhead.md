---
title: "Vấn đề hiệu năng (Overhead)"
---

# 12. Vấn đề hiệu năng (Overhead)

## 🧾 Content

Không phải cứ nhiều luồng là sẽ nhanh hơn. Multithreading tiêu tốn tài nguyên cho: 
- Context Switching: Chi phí CPU để chuyển đổi qua lại giữa các luồng.
- Memory Usage: Mỗi luồng cần một vùng nhớ ngăn xếp (stack) riêng.
- Quản lý luồng: Việc tạo và hủy luồng liên tục gây tốn kém, thường được khắc phục bằng Thread Pool.

## 📝 Note


