---
title: "D-Bus (Desktop bus)"
---

# 9. D-Bus (Desktop bus)

## 🧾 Content

1. D-Bus là 1 cơ chế IPC high level trong linux
- dùng để giao tiếp giữa các process không họ hàng
- giao tiếp giữa app ↔ service hệ thống
- truyền message dạng structured
- có 2 loại d-bus là system bus & section bus

2. System bus
- là bus hệ thống chạy dưới quyền root
- ảnh hưởng đến toàn hệ thống, nhiều user dùng chung

3. Session bus
- là bus cấp user session, chạy dưới quyền user
- mỗi user sẽ có 1 bus riêng, dùng để ipc giữa ứng dụng trong cùng session
- session: ở đây là phiên đăng nhập của 1 user

## 📝 Note


