---
title: "Vấn đề của multiple inheritance? diamond problem?"
---

# 19. Vấn đề của multiple inheritance? diamond problem?

## 🧾 Content

Multiple inheritance issues
1. Naming conflicts: nếu 2 lớp cha có cùng 1 method trùng tên, lớp con sẽ không biết gọi method của ông bố nào.
2. Độ phúc tạp tăng cao: cấu trúc phân lớp trở nên rối rắm, khó bảo trì, và dễ gây nhầm lẫn cho lập trình viên
3. Lãng phí bộ nhớ: nếu không xử lý khéo, các thành phần của lớp tổ tiên có thể bị nhân bản nhiều lần trong bộ nhớ. (xem thêm diamond problem)

Diamond problem
1. Lớp A: Có một phương thức display().
2. Lớp B và Lớp C: Cùng kế thừa từ A và ghi đè (override) phương thức display().
3. Lớp D: Kế thừa từ cả B và C.
Câu hỏi đặt ra: Khi bạn gọi D.display(), chương trình sẽ chạy code của B hay của C? (answer: compiler báo lỗi)

Tại sao nó nguy hiểm?
1. Sự nhập nhằng: có 2 con đường dẫn từ D về A, nếu không có quy tắc ưu tiên rõ ràng thì compiler sẽ báo lỗi ngay khi biên dịch.
2. Nếu lớp A có 1 biên id, thì D có thể chứa tới 2 bản sao của id gây lãng phí bộ và mất đồng bộ dữ liệu.

Solution: sử dụng virtual inheritance, để đảm bảo chỉ có duy nhất 1 thực thể của lớp tổ tiên tồn tại.

## 📝 Note

Tại sao Virtual Inheritance (Kế thừa ảo) lại giải quyết được?
Để hiểu cách nó hoạt động, hãy tưởng tượng sự khác biệt về "sơ đồ bộ nhớ":
Khi KHÔNG dùng Virtual Inheritance:
- Lớp D giống như một cái thùng chứa hai cái hộp riêng biệt: hộp B và hộp C. Trong mỗi hộp đó lại chứa một bản sao riêng của lớp A.
- Hậu quả: D có tới 2 bản sao của A. Khi gọi display(), nó thấy 2 "ông nội" A khác nhau nên nó bối rối.

Khi DÙNG Virtual Inheritance (class B : virtual public A):
1. từ khóa virtual giúp trình biên dịch đảm bảo chỉ tồn tại duy nhất 1 bản sao của A trong D. 
2. thay vì bê nguyên cả lớp A, B, C, trinh biên dịch sẽ để lại 1 con trỏ (vptr) trỏ về vùng nhớ chung của A.
