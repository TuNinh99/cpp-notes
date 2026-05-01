---
title: "thread lifecycle"
---

# 1. thread lifecycle

## 🧾 Content


```cpp
1. new std::thread t(worker_thread): luồng sẽ chạy ngay lập tức
2. running: thực thi mã code
3. block/waiting: đợi mutex, condition variable hoặc I/O
4. terminate: kết thúc hàm
*note: nếu chương trình kết thúc mà chưa gọi join() hay detach() sẽ ctrinh sẽ gọi std::terminate()
```


## 📝 Note


