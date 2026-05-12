---
title: "10. Double buffer & shared memory"
sidebar_position: 10
---

# 10. Double buffer & shared memory

## 🧾 Content

có 2 buffer 
- Producer-&gt; ghi data
- Consumer -&gt; đọc và xử lý data
nếu consumer chưa xử lý xong -&gt; producer ghi đe/dừng khi. tùy lựa chọn, bài toán cụ thể
nếu khi xử lý xong -&gt; swap buffer
khi lập trình thì nên có 1 biến is_swap để làm điều này, biến này quyết định đọc/ghi ở buffer nào

## 📝 Note

code: double buffer
