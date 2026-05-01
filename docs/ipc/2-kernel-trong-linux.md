---
title: "Kernel trong Linux"
---

# 2. Kernel trong Linux

## 🧾 Content

Kernel là gì?
- là tầng trung gian, bộ não điều khiển ở giữa phần cứng thật (CPU, RAM, Disk, network, USB,...) và ứng dụng
- kernel quản lý CPU: ctrinh nào chạy trước, ctrinh nào đợi, chia CPU theo tgian (sheduler)
- quản lý RAM: ứng dụng sẽ phải xin RAM do kernel cấp, không cho ứng dụng này xâm phạm vùng nhớ ứng dụng khác
- quản lý file hệ thống: mở/lưu/đóng; tạo folder
- Bảo mật

Tại sao Kernel có vùng nhớ riêng?
- vùng nhớ riêng này của Kernel nằm trong cùng RAM của máy, chỉ Kernel đc phép dùng
- để bảo vệ hệ thống không bị phá: nếu ứng dụng có thể ghi lung tung vào RAM của kernel thì nếu ghi nhầm -&gt; hệ thống sẽ crash
- Tách vai trò giữa Kernel & App
- Để hệ thống chạy ổn định và đa nhiệm: g/s có 1 app đang chạy, app khác lại ghi lung tung vào bộ nhớ -&gt; tất cả sập

## 📝 Note


