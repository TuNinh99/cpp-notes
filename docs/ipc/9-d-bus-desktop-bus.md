---
title: "9. D-Bus (Desktop bus)"
sidebar_position: 9
---

# 9. D-Bus (Desktop bus)

## 🧾 Content

1. D-Bus là 1 cơ chế IPC high level trong linux
- Dùng để giao tiếp giữa các process không họ hàng
- Giao tiếp giữa app ↔ service hệ thống
- Truyền message dạng structured
- Có 2 loại d-bus là system bus &amp; section bus

2. System bus
- Là bus hệ thống chạy dưới quyền root
- Ảnh hưởng đến toàn hệ thống, nhiều user dùng chung

3. Session bus
- Là bus cấp user session, chạy dưới quyền user
- Mỗi user sẽ có 1 bus riêng, dùng để ipc giữa ứng dụng trong cùng session
- Session: ở đây là phiên đăng nhập của 1 user

## 📝 Note


