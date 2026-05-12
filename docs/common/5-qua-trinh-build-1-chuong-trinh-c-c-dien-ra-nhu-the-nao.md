---
title: "5. Quá trình build 1 chương trình C/C++ diễn ra như thế nào?"
sidebar_position: 5
---

# 5. Quá trình build 1 chương trình C/C++ diễn ra như thế nào?

## 🧾 Content

1. Preprocessing
- Input: .c; .cpp; .h
- Xoá bỏ chú thích
- Chỉ thị tiền xử lý C# cũng được xử lý
- Output: include header, expand (.i, .ii)

2. Compilation
- Phân tích syntax của mã nguồn
- Chuyển sang mã assembly
- Output: asembly code (.s)

3. Assembly
- Dịch chương trinhf sang mã máy 0&amp;1
- Output: machine code (.o, .obj)

4. Linking
- Liên kết các object lại
- Mã máy của các thư viện cũng đc liên kết ở đây
- Output: excutable file

## 📝 Note


