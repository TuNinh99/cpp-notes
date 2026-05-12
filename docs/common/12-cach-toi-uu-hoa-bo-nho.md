---
title: "12. Cách tối ưu hoá bộ nhớ"
sidebar_position: 12
---

# 12. Cách tối ưu hoá bộ nhớ

## 🧾 Content

1. Chọn đúng kiêu dữ liệu: chọn kiểu dữ liệu nhỏ nhất có thể
Ex: nếu value 0 -&gt; 255 dùng uint8_t thay vì int
2. Quản lý cấp phát động
- Sử dụng RAll (như smartpointer) để tự động giải phóng bộ nhớ, tránh rò rỉ
- Hạn chế cấp phát quá nhiều trong vòng lặp
-&gt; dùng memory pool (cấp phát khối lớn, chia nhỏ &amp; dùng dần)
3. Struct padding
- Khai báo các thành phần lớn nhất trong struct trước để giảm thiểu padding do căn chỉnh bộ nhớ
4. Data locality
- Ưu tiên dùng vector với những dữ liệu liên tiếp nhau, giúp tận dụng bộ nhớ đệm cache của CPU tốt hơn.
5. Hạn chế biến toàn cục nếu không cần thiết
- Tránh chiếm RAM trong suốt chương trình

## 📝 Note


