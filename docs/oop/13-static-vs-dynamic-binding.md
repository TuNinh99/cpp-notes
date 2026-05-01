---
title: "Static vs Dynamic binding"
---

# 13. Static vs Dynamic binding

## 🧾 Content

binding là quá trình kết nối một lời gọi hàm với thân hàm
- static binding (early binding): xác định hàm → lưu địa chỉ hàm vào bộ nhớ → thay thế lời gọi hàm (binding) → đóng gói (executable)
- dynamic binding (late binding): obj → vptr → vtable → function (giống dynamic dispatch)

## 📝 Note

Gắn với polymorphism
