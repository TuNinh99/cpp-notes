---
title: "Obsever"
---

# 3. Obsever

## 🧾 Content

Observer là cơ chế “khi có sự kiện xảy ra thì tự động thông báo cho nhiều đối tượng quan tâm”, giúp giảm sự phụ thuộc giữa bên phát sự kiện và bên nhận thông báo.

1. Mục đích
- Cho phép 1 object (Subject) tự động thông báo cho nhiều object khác (Observers) khi có thảy đổi mà không bị phụ thuộc cứng vào chúng
- ví dụ: GUI event (button click -&gt; notify listeners), Data model update -&gt; UI refresh.

2. Ý tưởng thiết kế
- Subject giữ danh sách observers
- Observer đăng kí (Subscribe)
- Khi Subject thay đổi -&gt; gọi notify()
Ex: 
- class Subject giữ danh sách các observer (IObserver): có Subscribe/Unsubscribe để cho các observer đăng kí, huỷ đăng kí và notify() để call đến hàm update của các observer
- ConcreteObserver kế thừa từ IObserver, khi có thay đổi Subject chỉ cần call notify() là đc

3. Vấn đề thường gặp?
- Memory leak / dangling pointer: Nếu observer bị destroy mà không unsubscribe → Subject giữ pointer rác → crash.
&lt; xem kỹ hàm notify trong ví dụ để biết cách fix&gt;
- Thread-safety: Nếu Observer/Subject chạy khác thread thì phải bảo vệ bằng mutex
- Notification storm: Quá nhiều notify liên tục → performance problem → patch update

## 📝 Note

Ưu điểm
- Liên kết lỏng lẻo (Loose Coupling): Subject không cần biết chi tiết về các lớp Observer. Nó chỉ giao tiếp qua interface IObserver, giúp mã nguồn linh hoạt và dễ bảo trì hơn.
- Nguyên lý Đóng/Mở (Open/Closed Principle): Bạn có thể thêm các loại Observer mới (ex: EmailObserver, LoggingObserver) vào hệ thống mà không cần sửa đổi mã nguồn của lớp Subject.
- Thiết lập quan hệ tại Runtime: Các đối tượng có thể đăng ký (subscribe) hoặc hủy đăng ký (unsubscribe) nhận thông báo bất cứ lúc nào khi chương trình đang chạy.
- Hỗ trợ truyền tin Broadcast: Một thay đổi duy nhất trong Subject có thể tự động cập nhật đến hàng loạt Observer cùng lúc.

Nhược điểm
- Rò rỉ bộ nhớ: Nếu một Observer không tự hủy đăng ký trước khi bị xóa, Subject vẫn sẽ giữ con trỏ tới vùng nhớ đó, dẫn đến crash hoặc leak.
- Thứ tự thông báo không xác định: Thông thường, các Observer sẽ nhận thông báo theo thứ tự ngẫu nhiên hoặc tùy thuộc vào cấu trúc danh sách (như std::list), điều này có thể gây ra lỗi nếu logic của bạn yêu cầu Observer A phải chạy trước Observer B.
- Gây tốn tài nguyên (Performance Overhead): Nếu danh sách Observer quá lớn hoặc hàm update xử lý quá nặng, việc gọi notify() có thể làm chậm chương trình đáng kể.
