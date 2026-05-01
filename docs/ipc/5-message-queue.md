---
title: "Message Queue"
---

# 5. Message Queue

## 🧾 Content

1. Là cơ chế IPC cho phép các process trao đổi dữ liệu thông qua các message riêng biệt, được lưu thông trong một hàng đợi do kernel quản lý.

2. Giải thích cơ chế message đc lưu trong queue của kernel
- khi tạo 1 message queue, nó không nằm trong bộ nhớ user-space của process mà được tạo ra và lưu trong kernel-space
- kernel giữ 1 data structure dạng hàng đợi (queue) đẻ chứa các message
- mọi thao tác send/receive đều thông qua system call -&gt; kernel đứng ra trung gian.
- queue, buffer, size limits, permission, thứ tự và đồng bộ hoá (sync/async) của message queue đều đc kernel quản lý. 
- các user process chỉ tương tác với nó thông qua các lệnh gọi hệ thống như msgsnd/msgrcv hoặc mq_send/mq_receive

3. Behavior
- Nếu queue đầy -&gt; call msgsnd() -&gt; block/fail EAGAIN nếu non-blocking
- Nếu queue rỗng -&gt; msgrcv() -&gt; block/fail ENOMSG
- Odering: theo FIFO nhưng có thể override bằng message priority
- Limit: có giới hạn nhưng có thể cấu hình qua msgctl
- Lifetime: System V tồn tại đến khi bị xoá/POSIX tồn tại đến khi mq_unlink()/ reboot (System V & POSIX là 2 kiểu message type)

## 📝 Note


