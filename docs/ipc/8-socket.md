---
title: "8. Socket"
sidebar_position: 8
---

# 8. Socket

## 🧾 Content

1. Đặc điểm
- Là cơ chế mạnh và linh hoạt nhất trong IPC
- Có thể chạy trên cùng máy hoặc khác máy
- Thiết kế theo kiểu client-server
- Có 2 loại socket liên quan đến IPC là: Unix Domain Socket (UDS)

2. UDS
- IPC trong cùng máy
- Truyền qua file special trong file system (ví dụ: /tmp/my_socket)
- Nhanh hơn TCP vì không qua mạng và truyền trong kernel spcace
- Hỗ trợ 2 chiều: datagram (UDP-like) hoặc stream (TCP-like)
-&gt; IPC mạnh nhất khi cần giao tiếp nhiều process độc lập trong cũng hệ thống. 

3. Network Socket (TCP/UDP)
- Dùng khi process chạy trên máy khác nhau
- Cũng dùng được khi cùng máy
- Chậm hơn UDS, shared mem
- Phù hợp khi cần nhiều client &lt;-&gt; 1 server, khi cần mở rộng sang máy khác, khi thiết kế service based,...

## 📝 Note


