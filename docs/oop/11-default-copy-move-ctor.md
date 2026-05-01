---
title: "default/copy/move ctor"
---

# 11. default/copy/move ctor

## 🧾 Content

default ctor: khởi tạo đối tượng mà kh cần bất kì đối số nào

move ctor
thay vì copy, move ctor chuyển ownership của object cũ sang object mới và đặt object cũ về trạng thái rỗng.

vấn đề khi dùng default copy ctor (shallow copy ctor) - example
*kịch bản: object A có một con trỏ trỏ đến vùng nhớ M. Khi bạn dùng Shallow Copy để tạo object B từ A, con trỏ của B cũng trỏ đến đúng vùng nhớ M đó
*hậu quả: 
1. double free
- sau khi object A bị hủy, nó giải phóng vùng nhớ M, sau khi object B bị hủy, nó giải phóng M thêm 1 lần nữa
- double free, memory managerment sẽ báo lỗi và crash ngay lập tức
2. dữ liệu bị thay đổi ngoài ý muốn (Data Corruption)
- khi A thay đổi thì B cũng thay đổi theo (bản chất là chung vùng nhớ)
- phá vỡ tính đóng gói và độc lập của object, lỗi logic cực kì khó tìm
3. con trỏ lơ lửng (Dangling Pointer)
- nếu A bị hủy trước, M bị thu hồi, lúc này B trỏ đến vùng nhớ không hợp lệ, nếu B tiếp tục truy cập hoặc ghi đè vào đó thì 
- gây lỗi segment fault (linux) or access violation (window), ctrinh crash ngay lập tức

Solution
- Nếu lớp không dùng con trỏ (properties chỉ là kiểu dữ liệu nguyên thủy): Shallow Copy (mặc định của C++) là đủ và nhanh.
- Nếu lớp có dùng con trỏ (cấp phát new): Bắt buộc phải tự định nghĩa copy ctor để thực hiện Deep Copy (cấp phát vùng nhớ mới và chép giá trị sang).

## 📝 Note


