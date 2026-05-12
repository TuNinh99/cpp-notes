---
title: "8. Dangling pointer"
sidebar_position: 8
---

# 8. Dangling pointer

## 🧾 Content

- Là một con trỏ vẫn trỏ đến 1 địa chỉ bộ nhớ sau khi đối tượng tại đ/c đó đã bị giải phóng hoặc xoá bỏ
- 3 TH gây dangliing pointer
1. Giải phóng bộ nhớ nhưng gán NULL
2. Trỏ vào biến cục bộ đã out of scope
3. Biến nằm ngoài phạm vi khối lệnh, giống #2

Hậu quả:
1. Crash ngay
vùng nhớ bị thu hồi hoàn toàn/đánh dấu là ko thể truy cập -&gt; segmentation fault -&gt; crash

2. Sai logic
chứa giá trị cũ/ giá trị rác -&gt; ctrinh chạy bth nhưng sai kết quả

3. Lỗi bảo mật/hỏng dữ liệu
vùng nhớ đó đã được cấp phát cho 1 biến khác của ctrinhf -&gt; dùng dangling pointer để ghi đè giá trị -&gt; hành vi kì quặc &amp; khó hiểu

## 📝 Note


