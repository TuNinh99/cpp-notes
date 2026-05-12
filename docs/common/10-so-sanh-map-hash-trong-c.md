---
title: "10. So sánh map & hash trong C++"
sidebar_position: 10
---

# 10. So sánh map & hash trong C++

## 🧾 Content

```cpp
1. Std::map (Ordered Map)
- Cấu trúc dữ liệu: Sử dụng Cây nhị phân tìm kiếm cân bằng (thường là Cây Đỏ-Đen).
- Đặc điểm: Các phần tử luôn được sắp xếp theo khóa (Key).
- Độ phức tạp: Các thao tác tìm kiếm, chèn, xóa đều là \(O(\log n)\).
- Sử dụng khi: Cần duy trì thứ tự các phần tử, cần duyệt theo phạm vi (range queries) hoặc khi số lượng phần tử nhỏ

2. Std::unordered_map (Hash Map)
- Cấu trúc dữ liệu: Sử dụng Bảng băm (Hash Table).
- Đặc điểm: Các phần tử không có thứ tự nhất định.
- Độ phức tạp: Trung bình: \(O(1)\) cho tìm kiếm, chèn, xóa.Tệ nhất: \(O(n)\) (khi xảy ra xung đột hàm băm - hash collision).
- Sử dụng khi: Cần tốc độ truy xuất nhanh nhất và không quan tâm đến thứ tự của dữ liệu.
```

## 📝 Note


