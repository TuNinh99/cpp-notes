---
title: "Các Thread communication với nhau thế nào?"
---

# 15. Các Thread communication với nhau thế nào?

## 🧾 Content

Threads giao tiếp bằng shared data + synchronization, phổ biến nhất là mutex, atomic và condition_variable
1️⃣ mutex / lock → bảo vệ critical section
2️⃣ atomic → chia sẻ biến nhỏ, tránh mutex
3️⃣ condition_variable → đồng bộ theo sự kiện (wait/notify)

## 📝 Note


