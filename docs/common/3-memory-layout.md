---
title: "3. Memory layout"
sidebar_position: 3
---

# 3. Memory layout

## 🧾 Content

1. Stack
- Function param
- Return adess
- Local variable

2. Heap: cấp phát động

3. Uninitialized Data (BSS): global &amp; static variable ko khởi tạo hoặc khởi tạo bằng 0

4. Initialized Data (DS) : global &amp; static variable có giá trị khác 0

5. Text segment: source file

Question: const đc lưu trữ tuỳ thuộc vào phạm vi 
- Global/static const: tex segment
- Local const: stack
- Const chuỗi: .rodata (read-only-data)

## 📝 Note


