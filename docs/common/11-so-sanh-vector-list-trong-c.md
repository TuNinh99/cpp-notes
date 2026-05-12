---
title: "So sánh vector & list trong C++"
---

# 11. So sánh vector & list trong C++

## 🧾 Content

```cpp
1. Std::vector (Dynamic Array)
- Bản chất: Là một mảng động, các phần tử nằm ở các ô nhớ liên tiếp nhau.
- Truy cập: Hỗ trợ truy cập ngẫu nhiên (Random Access) cực nhanh qua chỉ số [] với độ phức tạp \(O(1)\).
- Chèn/Xóa: Ở cuối: Rất nhanh (\(O(1)\)).Ở đầu/giữa: Chậm (\(O(n)\)) vì phải dịch chuyển các phần tử còn lại.
- Bộ nhớ: Ít tốn kém hơn (chỉ lưu dữ liệu), nhưng có thể lãng phí một khoảng trống dự phòng (capacity) để tránh cấp phát lại nhiều lần.

2. Std::list (Doubly Linked List)
- Bản chất: Là một danh sách liên kết đôi, mỗi phần tử (node) nằm rải rác trong bộ nhớ và kết nối với nhau qua con trỏ.
- Truy cập: Không hỗ trợ truy cập ngẫu nhiên. Muốn tìm phần tử thứ \(n\) phải duyệt từ đầu, độ phức tạp \(O(n)\).
- Chèn/Xóa: Rất nhanh (\(O(1)\)) tại bất kỳ vị trí nào nếu đã biết vị trí của node đó, vì chỉ cần thay đổi liên kết con trỏ.
- Bộ nhớ: Tốn kém hơn vì mỗi node phải lưu thêm ít nhất 2 con trỏ (trỏ trước và trỏ sau).
```

## 📝 Note


