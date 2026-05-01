---
title: "RAII là gì?"
---

# 17. RAII là gì?

## 🧾 Content

- RAII = resource acquisition is initialization
- Resource sẽ được acquire trong constructor và release trong destructor nên rất clean up
- Đây là 1 idiom trong C++ không chỉ cho memory mà còn cho cả các non-memory khác như file, mutex, lock,...
- Resource gắn với lifetime object. Destructor auto cleanup.

## 📝 Note

Rất quan trọng trong C++
