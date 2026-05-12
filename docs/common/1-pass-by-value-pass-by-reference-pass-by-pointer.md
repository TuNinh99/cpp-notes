---
title: "1. Pass by value, pass by reference, pass by pointer"
sidebar_position: 1
---

# 1. Pass by value, pass by reference, pass by pointer

## 🧾 Content

1. Pass by value
- Bản chất: copy giá trị của biến vào tham số của hàm
- Ảnh hưởng: mọi thay đổi bên trong hàm chỉ tác động lên bản sao, không thay đổi biến gốc bên ngoài
- Sử dụng khi: muốn bảo vệ dữ liệu gốc, chỉ cần lấy giá trị để tính toán

2. Pass by reference
- Bản chất: truyền bí danh (alias) của biến, hàm thao tác trực tiếp trên vùng nhớ của biến gốc
- Ảnh hưởng: thay đổi bên trong hàm sẽ làm thay đổi trực tiếp biến gốc
- Sử dụng khi: cần hàm cập nhật kết quả vào biến truyền vào hoặc khi làm việc với đối tượng lớn để tránh chi phí copy dữ liệu

3. Pass by pointer
- Bản chất: truyền địa chỉ ô nhớ của biến
- Ảnh hưởng: tương tự tham chiếu, thay đổi giá trị của biến gốc
- Điểm khác biệt so với #2:
+) con trỏ có thể bị NULL nên cần kiểm tra trước khi dùng
+) có thể thay đổi để trỏ sang vùng nhớ khác, trong khi tham chiếu thì không

## 📝 Note


