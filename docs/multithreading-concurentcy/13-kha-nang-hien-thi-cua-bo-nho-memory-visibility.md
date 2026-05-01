---
title: "Khả năng hiển thị của bộ nhớ ( Memory Visibility)"
---

# 13. Khả năng hiển thị của bộ nhớ ( Memory Visibility)

## 🧾 Content


```cpp
Tại sao luồng này kh thấy thay đổi của luồng kia?
Trong các hệ thống hiện đại tốc độ của CPU cao hơn rất nhiều so với RAM, để không phải chờ RAM, mỗi core của CPU đều có các tầng bộ nhớ đệm riêng (L1, L2 cache)
1. Khi luồng A chạy trên core 1, thay đổi biến stop = true giá trị này thường chỉ được cập nhật vào L1 cache hoặc 1 bảng đệm ghi (write buffer).
2. Core 1 sẽ chưa cập nhật ngay xuống RAM, vì ghi xuống RAM rất chậm
3. Luồng B chạy trên core 2 kiểm tra biến stop. Nó sẽ đọc từ L1 cache của chính nó hoặc RAM. Vì core 1 chưa xả dữ liệu xuống RAM, nên stop = false.
kết quả: luồng B chạy mãi mãi, dù luồng A đã ra lệnh dừng

Solution:
1. Gom cụm các thao tác ghi (batching)
đừng ghi vào biến dùng chung (shared variable) quá thường xuyên
- sai: mỗi lần vòng lặp chạy, cộng dồn vào 1 biến toàn cục std::atomic. việc này ép CPU phải xả cache liên tục gây nghẽn bus bộ nhớ.
- đúng: dùng 1 biến cục bộ local variable để tính toán trong cache của riêng nhân đó, sau khi xong xuôi mới ghi kết quả cuồi cùng vào biến dùng chung 1 lần duy nhất.

2. thiết kế single-writer (chỉ một luồng ghi)
hiệu năng tốt nhất đạt được khi thiết kế hệ thống sao cho
- nhiều luồng có thể đọc (read-only) một vùng nhớ
- chỉ uy nhất một luồng được quyền ghi vào cùng nhớ đó. khi đó, có thể dùng memory_order_relaxed hoặc thậm chí không cần lock trong nhiều trường hợp vì không có xung đột khi ghi
```


## 📝 Note


