---
title: "2. Return by value, return by reference, return by pointer"
sidebar_position: 2
---

# 2. Return by value, return by reference, return by pointer

## 🧾 Content

1. Return by value
- Cách thức: tạo ra 1 bản sao của dữ liệu &amp; trả bản sao đó về cho bên gọi
- Đặc điểm:
+) an toàn vì dữ liệu gốc trong hàm bị huỷ đi cũng không sao
+) tuy nhiên nếu dữ liệu lớn, việc copy sẽ gây tốn hiệu năng
- Khi nào dùng: trả về các kiểu dữ liệu cơ bản (int, float) hoăc các object nhỏ

2. Return by reference
- Cách thức: trả về 1 bí danh trỏ trực tiếp đến vùng nhớ của biến
- Đặc điểm:
+) không tốn chi phí copy, hiệu năng cao
+) có thể dùng kết quả trả về ở vế trái phép gán (ví dụ: func() = 10)
- Nguy hiểm: nếu trả về tham chiếu của biến local thì khi out of scope, biến sẽ bị huỷ dẫn đến tham chiếu rác
- Khi nào dùng:
+) khi nạp chồng toán tử 
+) truy xuất phần tử trong mảng/container

3. Return by pointer
- Cách thức: trả về địa chỉ ô nhớ của dữ liệu
- Đặc điểm: tươg tự tham chiếu , nhưng linh hoạt hơn vì có thể gán NULL
- Nguy hiểm:
+) tương tự tham chiếu, đừng trả về địa chỉ của biến cục bộ
+) nếu trả về con trỏ vùng nhớ đc cấp phát động, bên gọi phải nhớ giải phóng để tránh rò rỉ bộ nhớ
- Khi nào dùng: khi đối tượng trả về có thể không tồn tại (return NULL) hoặc khi làm việc với mảng động

## 📝 Note


