---
title: "Starvation (Bỏ đói luồng)"
---

# 14. Starvation (Bỏ đói luồng)

## 🧾 Content

- Xảy ra khi một hoặc nhiều luồng không bao giờ được cấp phát tài nguyên để thực thi
Các nguyên nhân phổ biến nhất:
1. ưu tiên luồng (thread priority) không hợp lý: OS ưu tiên các thread có high priority, nếu các threads này xuất hiện liên tục thì các threads có low priority sẽ không bao giờ được chạm vào.
2. tranh chấp lock (unfair locking): sau khi mutex/lock đc giải phóng, hệ thống sẽ chọn ngẫu nhiên 1 luồng đang chờ. nếu đen đủi thì thread mới đc giải phóng kia sẽ trượt hàng chục lần do các threads khác nhảy vào chiếm chỗ
3. thuật toán điều phối (scheduling) bị lỗi: g/s thread A cần tài nguyên X, nhưng tài nguyên X luôn bị chiếm dụng bởi 1 chuỗi các threads nối đuôi nhau khiến A cứ chờ mãi mà kh bao giờ đến lượt

## 📝 Note


