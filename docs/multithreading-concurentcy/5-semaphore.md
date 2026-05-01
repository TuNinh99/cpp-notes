---
title: "semaphore"
---

# 5. semaphore

## 🧾 Content


```cpp
- cơ chế cho phép nhiều luồng cùng truy cập vào 1 tài nguyên, thay vì chỉ 1 luồng duy nhất như mutex
- std::counting_semaphore: cho phép &gt; 1 luồng truy cập tài nguyên cùng 1 lúc.
- std::binary_semaphore: trường hợp đặc biết của counting_semaphore, tương tự mutex, tuy nhiên, luồng giải phóng không nhất thiết phải là luồng đã khóa
- cách hoạt động: 
acquire() - nếu bộ đếm (counting) lớn hơn 0, giảm bộ đếm, nếu counting = 0, luồng sẽ bị chặn cho đến khi counting tăng lên
release() - tăng counting và unlock các luồng đang chờ (nếu có)
```


## 📝 Note

Giả sử có bãi đậu xe 5 chỗ
- Mỗi xe vào → lấy 1 “thẻ”
- Khi đầy 5 xe → xe thứ 6 phải đợi
- Xe ra → trả thẻ → xe khác vào được
→ Semaphore = cho phép tối đa N đơn vị truy cập cùng lúc

code: samaphore
