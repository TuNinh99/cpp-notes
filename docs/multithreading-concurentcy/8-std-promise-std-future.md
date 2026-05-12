---
title: "8. Std::promise & std::future"
sidebar_position: 8
---

# 8. Std::promise & std::future

## 🧾 Content

```cpp
- Std::promise: phía "hứa" sẽ cung cấp giá trị. call set_value() để set giá trị
- Std::future: phía "chờ" để lấy giá trị đó từ promise. call get_future() để lấy giá trị từ promise.
future chỉ truyền giữ liệu được 1 lần duy nhất. sau khi call get_future(). future đó sẽ không dùng lại được nữa
```

## 📝 Note

code: promise &amp; future
