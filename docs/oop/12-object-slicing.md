---
title: "Object slicing"
---

# 12. Object slicing

## 🧾 Content

xảy ra khi gán object derived cho obj base theo kiểu pass-by-value → 

hậu quả
- mất phần derived.
- mất tính đa hình

solution
- dùng con trỏ: Base *p = &derivedObj;
- dùng tham chiếu: Base &r = derivedObj;

## 📝 Note

Classic trap
