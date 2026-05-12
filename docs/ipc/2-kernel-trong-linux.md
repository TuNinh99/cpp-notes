---
title: "Kernel trong Linux"
---

# 2. Kernel trong Linux

## 🧾 Content

Kernel là gì?
- Là tầng trung gian, bộ não điều khiển ở giữa phần cứng thật (CPU, RAM, Disk, network, USB,...) và ứng dụng
- Kernel quản lý CPU: ctrinh nào chạy trước, ctrinh nào đợi, chia CPU theo tgian (sheduler)
- Quản lý RAM: ứng dụng sẽ phải xin RAM do kernel cấp, không cho ứng dụng này xâm phạm vùng nhớ ứng dụng khác
- Quản lý file hệ thống: mở/lưu/đóng; tạo folder
- Bảo mật

Tại sao Kernel có vùng nhớ riêng?
- Vùng nhớ riêng này của Kernel nằm trong cùng RAM của máy, chỉ Kernel đc phép dùng
- Để bảo vệ hệ thống không bị phá: nếu ứng dụng có thể ghi lung tung vào RAM của kernel thì nếu ghi nhầm -&gt; hệ thống sẽ crash
- Tách vai trò giữa Kernel &amp; App
- Để hệ thống chạy ổn định và đa nhiệm: g/s có 1 app đang chạy, app khác lại ghi lung tung vào bộ nhớ -&gt; tất cả sập

## 📝 Note


