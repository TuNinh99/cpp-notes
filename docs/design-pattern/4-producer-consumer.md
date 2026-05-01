---
title: "Producer – Consumer"
---

# 4. Producer – Consumer

## 🧾 Content

Main Thread / Event Source  ---&gt;  Queue  ---&gt;  Worker Thread(s)
- Thread A (UI / I/O / logic chính) chỉ push task vào queue
- Worker Thread(s) chỉ việc lấy task ra và xử lý
- Hai phía không phụ thuộc trực tiếp vào nhau

## 📝 Note


