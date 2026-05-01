---
title: "mutex & lock"
---

# 2. mutex & lock

## 🧾 Content


```cpp
- là cơ chế dùng để bảo vệ các vùng dữ liệu dùng chung
- thay vì phải mutex.lock() / mutex.unlock() thủ công thì các lock wraper sẽ tuân theo RAII (tự giải phóng khi out of scope)
1. std::lock_guard: Là loại đơn giản nhất. Nó khóa mutex ngay khi được khởi tạo và tự động mở khóa khi đối tượng bị hủy (kết thúc dấu ngoặc nhọn &#123;&#125;).
2. std::unique_lock: Linh hoạt hơn lock_guard. Nó cho phép bạn chủ động khóa/mở khóa nhiều lần, trì hoãn việc khóa hoặc thiết lập thời gian chờ (timeout).
3. std::shared_lock: Thường dùng với std::shared_mutex (C++17). Nó cho phép nhiều luồng cùng đọc dữ liệu đồng thời, nhưng chỉ một luồng duy nhất được ghi
4. std::mutex: Loại cơ bản nhất, không cho phép khóa đệ quy.
5. std::recursive_mutex: Cho phép một luồng đã giữ khóa có thể khóa thêm nhiều lần nữa mà không bị tự khóa chính mình (deadlock).
6. std::timed_mutex: Hỗ trợ thử khóa trong một khoảng thời gian nhất
```


## 📝 Note

giống như 1 key
- Giả sử trong công ty có 1 nhà vệ sinh
- Ai muốn dùng → phải cầm chìa khóa
- Nếu người khác đang cầm chìa → phải đợi
- Khi xong → trả chìa khóa
- Luôn đảm bảo chỉ 1 người bên trong
→ Mutex = chỉ cho 1 đơn vị truy cập, đảm bảo mutual exclusion
