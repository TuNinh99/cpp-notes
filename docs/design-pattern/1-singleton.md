---
title: "Singleton"
---

# 1. Singleton

## 🧾 Content


```cpp
1. Ý tưởng:
- đảm bảo chỉ có 1 instance duy nhất trong toàn chương trình + global access
- dùng khi: logger, config system, resource manger, hardware controller(camera, loa, ...)
- lưu ý: 
thread safe cho singleton khi khởi tạo đối tượng: std::lock_guard&lt;std::mutex&gt; lock(mtx);
```


## 📝 Note

Ưu điểm
- Kiểm soát truy cập: Đảm bảo chỉ có duy nhất một đối tượng của lớp đó tồn tại trong suốt vòng đời ứng dụng.
- Điểm truy cập toàn cục: Cung cấp một cách lấy instance dễ dàng từ bất kỳ đâu trong code.
- Tiết kiệm tài nguyên: Tránh việc khởi tạo lặp đi lặp lại các đối tượng nặng (như kết nối Database, Logging, Configuration).
- Lazy Loading: Có thể trì hoãn việc khởi tạo cho đến khi thực sự cần dùng đến.

Nhược điểm
- Khó Unit Test: Do tạo ra trạng thái toàn cục, khó cô lập đối tượng để kiểm thử.
- Vi phạm nguyên tắc SOLID: Cụ thể là nguyên tắc Đơn nhiệm (Single Responsibility), vì nó vừa quản lý logic vừa tự quản lý vòng đời của chính mình.
- Gây phụ thuộc chặt (Tight Coupling): Làm code cứng nhắc, khó thay đổi hoặc mở rộng sau này.
- Vấn đề đa luồng: Nếu code không khéo dễ dẫn đến tình trạng tạo ra nhiều instance ngoài ý muốn (Race condition).
