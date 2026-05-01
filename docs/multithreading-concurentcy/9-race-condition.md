---
title: "race condition"
---

# 9. race condition

## 🧾 Content

- là lỗi logic xảy ra khi kết quả phụ thuộc vào thứ tự thực thi giữa các thread/process
- hệ quả là kết quả không như mong muốn: sai logic, deadlock, undefined behavior
- để hạn chế nó thì chỉ có thể design tốt tức là phải gom logic lại, xác định chính xác ownership, không share mutable state

Lưu ý:
- Có thể bị Data Race mà không bị Race Condition (ví dụ: ghi đè cùng một giá trị giống hệt nhau),
- hoặc bị Race Condition mà không bị Data Race (ví dụ: các lệnh đã được bảo vệ bằng Lock nhưng sai thứ tự logic)."

## 📝 Note

ex: bạn kiểm tra số dư ngân hàng (if balance &gt; 100), sau đó mới thực hiện rút tiền. Dù lệnh kiểm tra và lệnh rút đều được bảo vệ bởi Lock riêng lẻ, nhưng nếu một luồng khác nhảy vào giữa hai lệnh này để rút hết tiền, luồng đầu tiên vẫn sẽ rút tiền dù số dư đã về 0

code: race condition
