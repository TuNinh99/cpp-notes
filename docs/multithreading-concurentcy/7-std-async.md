---
title: "7. Std::async"
sidebar_position: 7
---

# 7. Std::async

## 🧾 Content

```cpp
- Mục tiêu của async là "tranh thủ" làm việc khác trong khi có các tác vụ nặng đang đợi, tức là tận dụng tgian trống
- Chạy 1 hàm bất đồng bộ, có thể tạo thread mới hoặc trì hoãn tùy thuộc vào std::launch policy
- Std::launch::async: chạy ngay lập tức, tạo luồng riêng biệt
- Std::launch::deferred: trì hoãn, chạy trên luồng hiện tại gọi đến nó
- Std::launch::async | std::launch::deferred: đây là policy mặc định, nếu CPU còn rảnh -&gt; async, còn k thì sẽ là deferred
*Node: async sẽ  trả về 1 future, nếu call get() của future thì nó sẽ block main thread tại thời điểm gọi hàm nếu có tác vụ nào đó chưa xong
```

## 📝 Note

code: async
