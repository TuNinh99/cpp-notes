---
title: "9. Data race"
sidebar_position: 9
---

# 9. Data race

## 🧾 Content

```cpp
- Xảy ra khi ít nhất 2 thread/process cùng truy cập vào 1 vùng nhớ tại cùng 1 thời điểm
- Ít nhất 1 thread trong đó thực hiện thao tác ghi và không có cơ chế đồng bộ nào

Hiện tượng: 
- Undefined behavior (các giá trị ghi đè lẫn nhau, đọc sai giá trị,...)
- Nếu 2 threads cùng cố gắng ghi vào 1 vùng nhớ thì có thể crash chương trình

Solution: đảm bảo chỉ có 1 thread có quyền truy cập vào vùng nhớ tại 1 thời điểm
-&gt; dùng mutex, atomic, semaphore
```

## 📝 Note

Tại sao lại crash khi 2 threads/processes cố gắng khi vào 1 vùng nhớ tại 1 thời điểm?
1. Phá vỡ tính toàn vẹn của "Cấu trúc dữ liệu phức tạp" (Gây Segfault)
- Trong bộ nhớ, các giá giá trị ko chỉ là con số đơn giản
- Nếu 2 threads/processes cùng ghi vào 1 pointer/object, thì việc này sẽ tạo ra giá trị rác (garbage value)
- Kịch bản như sau: Thread A đang ghi đ/c vùng nhớ 0xAAAA... Thread B nhảy vào ghi đè 1 nửa thành 0x...BBBB.
- Kết quả: biến đó bây giờ trở thành 0xAAAABBBB - 1 địa chỉ không tồn tại hoặc không có quyền truy cập
tại sao lại crash?
- Khi chương trình đọc đ/c rác này để sử dụng, OS phát hiện ra bạn đang truy cập trái phép nên sẽ tung ra lỗi segmentation fault (Linux) &amp; access violation (Window) để bảo hệ thống
---&gt; chương trình crash ngay lập tức

2. Làm hỏng meta data của bộ nhớ
- Khi dùng malloc/new/các lệnh cấp phát, OS sẽ quản lý bộ nhớ thông qua các "nhãn" (metadata) ẩn ngay tại vùng nhớ đó.
- Nếu 2 thread cùng ghi đè lên nhau và lỡ ghi lấn sang vùng metadata này thì trình quảnh lý bộ nhớ memory managerment sẽ bị lú.
- Khi chương trình gọi free/delete để giải phóng bộ nhớ, hệ thống kiếm tra thấy meta data đã bị hỏng. để ngăn chặn việc hỏng lan ra toàn bộ nhớ. OS sẽ chủ động khai tử (abort) tiến trình đang gặp sự cố
