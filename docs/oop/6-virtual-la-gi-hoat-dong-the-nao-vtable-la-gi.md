---
title: "virtual là gì? hoạt động thế nào? vtable là gì?"
---

# 6. virtual là gì? hoạt động thế nào? vtable là gì?

## 🧾 Content

1. virtual là gì? 
virtual dùng để bật cơ chế dynamic dispatch (late binding), cho phép chúng gọi hàm của object thực tế (runtime type) thay vì kiểu con trỏ/reference (compile-time type)

2. vtable là gì?
là 1 bảng các con trỏ hàm được compiler tạo ra cho mỗi class có virtual function

3. hoạt động thế nào? - quá trình dynamic dispatch
obj -&gt; vptr -&gt; vtable -&gt; function

4. chi phí (overhead)
- memory overhead: mỗi object có thêm 1 vptr (thường là 8bytes)
- runtime overhead: thêm 1 lần tìm kiếm thông qua vtable
- cache miss (có thể): ko inline được dễ dàng

## 📝 Note

Hay hỏi sâu memory layout
