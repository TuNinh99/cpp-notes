---
title: "Socket"
---

# 8. Socket

## 🧾 Content

1. Đặc điểm
- Là cơ chế mạnh và linh hoạt nhất trong IPC
- có thể chạy trên cùng máy hoặc khác máy
- thiết kế theo kiểu client-server
- có 2 loại socket liên quan đến IPC là: Unix Domain Socket (UDS)

2. UDS
- IPC trong cùng máy
- truyền qua file special trong file system (ví dụ: /tmp/my_socket)
- nhanh hơn TCP vì không qua mạng và truyền trong kernel spcace
- hỗ trợ 2 chiều: datagram (UDP-like) hoặc stream (TCP-like)
-&gt; IPC mạnh nhất khi cần giao tiếp nhiều process độc lập trong cũng hệ thống. 

3. Network Socket (TCP/UDP)
- dùng khi process chạy trên máy khác nhau
- cũng dùng được khi cùng máy
- chậm hơn UDS, shared mem
- phù hợp khi cần nhiều client &lt;-&gt; 1 server, khi cần mở rộng sang máy khác, khi thiết kế service based,...

## 📝 Note


