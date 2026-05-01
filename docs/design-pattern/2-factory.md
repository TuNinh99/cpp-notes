---
title: "Factory"
---

# 2. Factory

## 🧾 Content

Factory pattern giúp tách việc tạo object ra khỏi nơi sử dụng object,
client không cần biết cụ thể class nào sẽ được tạo, chỉ làm việc qua interface.

- Simple Factory: Có một chỗ trung tâm quyết định tạo object nào dựa trên input.
- Factory Method: Việc tạo object được giao cho subclass quyết định bằng cách override hàm tạo.
- Abstract Factory: Dùng khi cần tạo một họ sản phẩm liên quan và phải đồng bộ với nhau, ví dụ UI Mac vs Windows.

## 📝 Note

Ưu điểm:
- Giảm sự phụ thuộc (Loose Coupling): Giúp tách biệt mã nguồn của client khỏi các lớp cụ thể (concrete classes). Client chỉ giao tiếp qua interface hoặc abstract class, giúp chương trình độc lập với cách các đối tượng được tạo ra.
- Tuân thủ nguyên tắc Open/Closed (OCP): Bạn có thể thêm các loại sản phẩm mới vào chương trình mà không cần sửa đổi mã nguồn hiện có của client.
- Quản lý tập trung: Toàn bộ logic khởi tạo đối tượng được gom vào một nơi duy nhất (Factory), giúp mã nguồn dễ bảo trì, theo dõi và kiểm thử hơn.
- Che giấu logic phức tạp: Nếu việc tạo một đối tượng đòi hỏi nhiều bước thiết lập phức tạp, Factory sẽ đảm nhận việc này, giúp phía client luôn sạch sẽ và đơn giản. 

Nhược điểm:
- Rò rỉ bộ nhớ (Memory Leaks): Trong các ngôn ngữ như C++, nếu Factory tạo đối tượng bằng new nhưng phía Client quên delete, hoặc Factory không sử dụng smart pointers (như std::unique_ptr), bộ nhớ sẽ bị rò rỉ.
- Cạn kiệt tài nguyên: Nếu Factory được gọi liên tục trong một vòng lặp vô tận (do lỗi logic) để tạo ra hàng nghìn đối tượng mà không có cơ chế quản lý hoặc giải phóng (như Object Pooling), hệ thống sẽ hết bộ nhớ (Out of Memory) và dẫn đến crash
