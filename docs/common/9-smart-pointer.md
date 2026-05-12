---
title: "9. Smart pointer"
sidebar_position: 9
---

# 9. Smart pointer

## 🧾 Content

```cpp
1. Std::unique_ptr (Sở hữu độc quyền)
- Mỗi đối tượng chỉ được sở hữu bởi duy nhất một unique_ptr.
- Không thể sao chép (copy), chỉ có thể di chuyển (move) quyền sở hữu.
- Tự động giải phóng bộ nhớ khi pointer đi ra khỏi phạm vi (scope).

2. Std::shared_ptr (Sở hữu chung)
- Nhiều shared_ptr có thể cùng trỏ vào một đối tượng.
- Sử dụng cơ chế Reference Counting (biến đếm): Mỗi khi thêm một pointer trỏ tới, biến đếm tăng lên; khi pointer bị hủy, biến đếm giảm đi.
- Đối tượng chỉ bị giải phóng khi biến đếm bằng 0.

3. Std::weak_ptr (Sở hữu không ràng buộc)
- Đi kèm với shared_ptr để quan sát đối tượng mà không làm tăng biến đếm.
- Dùng để giải quyết vấn đề vòng lặp tham chiếu (circular reference) khiến bộ nhớ không bao giờ được giải phóng.Phải chuyển đổi thành shared_ptr mới có thể truy cập dữ liệu bên trong.
```

## 📝 Note


