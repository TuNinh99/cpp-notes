---
title: "20. Thread Pool"
sidebar_position: 20
---

# 20. Thread Pool

## 🧾 Content

```cpp
1. Thread pool là gì?
trong C++, thread pool là 1 mô hình trong đó chương trình tạo ra sẵn 1 nhóm (pool) các thread worker và tái sử dụng để chúng để xử lý nhiều task thay vì liên tục tạo rồi huỷ thread mới.

2. Ý tưởng
- Tạo trước N thread ở trạng thái chờ waiting
- Khi có task -&gt; đẩy nó vào queue
- Khi có 1 thread rảnh sẽ lấy task từ queue để xử lý
- Xong task -&gt; thread sẽ quay lại trạng thái chờ, không bị huỷ

Ví dụ nếu xử lý 1000 task mà mỗi task tạo một std::thread
→ sẽ:
- Tốn thời gian tạo
- Tốn RAM stack
- Có thể vượt giới hạn thread OS
- Scheduling hỗn loạn
```

## 📝 Note

code: thread pool
