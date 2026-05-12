---
title: "6. Hành vi của compiler khi dùng template"
sidebar_position: 6
---

# 6. Hành vi của compiler khi dùng template

## 🧾 Content

```cpp
1. Chưa sinh mã khi khai báo: Compiler chỉ lưu lại "bản thiết kế" (blueprint), không sinh ra mã máy ngay lập tức.
2. Cụ thể hóa (Instantiation): Khi bạn sử dụng template với một kiểu dữ liệu (vd: int), compiler mới sinh ra mã thực tế cho kiểu đó. Nếu không dùng, sẽ không có mã nào được tạo ra.
3. Lỗi kiểm tra muộn: Compiler thực hiện kiểm tra kiểu (type checking) tại thời điểm sử dụng. Do đó, lỗi chỉ xuất hiện khi bạn truyền vào một kiểu dữ liệu không hỗ trợ các toán tử mà template yêu cầu.
4. Hệ quả: Làm tăng thời gian biên dịch và kích thước file thực thi (Code Bloat), nhưng tối ưu hiệu năng vì mã được tối ưu riêng cho từng kiểu dữ liệu.
```

## 📝 Note


