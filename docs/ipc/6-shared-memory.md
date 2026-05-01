---
title: "Shared memory"
---

# 6. Shared memory

## 🧾 Content

I. Shared memory là cơ chế nhanh nhất trong IPC cho phép nhiều process cùng truy cập 1 vùng nhớ chung, nằm trong kernel quản lý. các process đọc - ghi trực tiếp cùng 1 vùng.

II. các hoạt động chính:
- 1 process tạo shared memory (shmget())
- kernel cấp phát vùng shared memory
- process khác attach vào
- tất cả cùng đọc/ghi vùng đó

III. Lưu ý:
- Shared memory không tự đồng bộ, phải tự đồng bộ qua semaphore hoặc mutex
- Shared memory giải quyết vấn đề hiệu năng, không cần copy qua kernel nhiều lần
- Lifetime: tồn tại trong kernel, không phụ thuộc 100% vào process, chỉ mất khi shctl(IPC_RMID)/reboot

*Notes: 
- attach = kết nối vào vùng nhớ chung
- detach = ngắt kết nối

IV. Phân loại
1. Phân loại theo Giao thức Hệ điều hành (OS IPC)
- POSIX Shared Memory (shm_open, mmap): Chuẩn hiện đại, dùng cơ chế file-descriptor, dễ quản lý và phổ biến trên các hệ thống Linux/Unix mới.
- System V Shared Memory (shmget, shmat): Chuẩn cũ hơn, sử dụng key_t để định danh. Tuy cũ nhưng vẫn xuất hiện rất nhiều trong các hệ thống Legacy (hệ thống kế thừa).

2. Phân loại theo Kiến trúc Phần cứng (Hardware)
- UMA (Uniform Memory Access): Tất cả các CPU truy cập vào một thanh RAM chung với tốc độ như nhau.
- NUMA (Non-Uniform Memory Access): Mỗi CPU có vùng RAM riêng (local), việc truy cập RAM của CPU khác sẽ chậm hơn. Các hệ thống Server nhiều CPU thường dùng loại này.

3. Phân loại theo Mô hình Quản lý Buffer (Software Pattern)
- Single Buffer: Chỉ có 1 vùng nhớ, phải dùng Mutex/Semaphore để khóa (chậm vì bên này chờ bên kia).
- Double Buffer: Dùng 2 vùng nhớ để vừa ghi vào vùng này, vừa đọc từ vùng kia (tối ưu tốc độ).
- Ring Buffer (Circular Buffer): Vùng nhớ cuốn chiếu, phù hợp cho dữ liệu dạng luồng (Streaming) liên tục.

## 📝 Note


