---
title: "12. Object slicing"
sidebar_position: 12
---

# 12. Object slicing

## 🧾 Content

xảy ra khi gán object derived cho obj base theo kiểu pass-by-value → 

hậu quả
- Mất phần derived.
- Mất tính đa hình

solution
- Dùng con trỏ: Base *p = &amp;derivedObj;
- Dùng tham chiếu: Base &amp;r = derivedObj;

## 📝 Note

Classic trap
