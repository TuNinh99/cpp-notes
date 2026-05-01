---
title: "Thread Pool"
---

# 19. Thread Pool

## 🧾 Content


```cpp
1. Thread pool là gì?
trong C++, thread pool là 1 mô hình trong đó chương trình tạo ra sẵn 1 nhóm (pool) các thread worker và tái sử dụng để chúng để xử lý nhiều task thay vì liên tục tạo rồi huỷ thread mới.

2. Ý tưởng
- tạo trước N thread ở trạng thái chờ waiting
- khi có task -&gt; đẩy nó vào queue
- khi có 1 thread rảnh sẽ lấy task từ queue để xử lý
- xong task -&gt; thread sẽ quay lại trạng thái chờ, không bị huỷ

Ví dụ nếu xử lý 1000 task mà mỗi task tạo một std::thread
→ sẽ:
- tốn thời gian tạo
- tốn RAM stack
- có thể vượt giới hạn thread OS
- scheduling hỗn loạn
```


## 📝 Note

code: thread pool
