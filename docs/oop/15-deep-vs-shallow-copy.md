---
title: "Deep vs Shallow copy"
---

# 15. Deep vs Shallow copy

## 🧾 Content

Shallow copy: copy pointer.
- Chỉ copy giá trị của các member.
- Nếu có con trỏ, nó chỉ copy địa chỉ, 2 object trỏ cùng 1 vùng nhớ
→ dễ gây double free/dangling.
- Default copy constructor trong C++ là shallow copy

Deep copy: copy data thật.
- Copy dữ liệu thực sự.
- Nếu có con trỏ, sẽ cấp phát vùng nhớ mới và copy nội dung sang → mỗi object quản lý vùng nhớ riêng.

## 📝 Note

Liên quan Rule of 3
