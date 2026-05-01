---
title: "Pipe & Name Pipe (FIFO)"
---

# 4. Pipe & Name Pipe (FIFO)

## 🧾 Content

1. Pipe: là 1 cơ chế IPC dạng stream, truyền dữ liệu 1 chiều giữa các process (parent-child), nếu muốn truyền 2 chiều thì phải có 2 pipe.
pip có đặc điểm: 
- không tồn tại dưới dạng file trong hệ thống, mà chỉ tồn tại trong kernel
- chỉ các process có quan hệ họ hàng mới dùng đc  
- buffer size thường từ vài KB đến và chục KB tuỳ hệ thống -&gt; có giới hạn -&gt; có thể bị block khi full

behavior:
- nếu read mà pipe rỗng -&gt; block
- nếu wirte mà pipe đầy -&gt; block
- nếu đầu đọc đóng mà vẫn ghi -&gt; nhận SIGPIPE
- nếu đầu ghi đóng và đọc -&gt; nhận EOF

2. Named pipe
- Named pipe = Pipe nhưng có tên, tồn tại dưới dạng 1 file trong filesystem. Chính vì nó có tên, nên bất kể process nào (ko cần họ hàng) cũng có thể mở giao tiếp.
- chính vì nó là pipe nên ngoài ra nó sẽ có đầy đủ đặc tính của pipe
- dùng khi mà 2 process độc lập cần giao tiếp, muốn dùng kiểu producer - consumer đơn giản, k cần hiệu năng cao và không cần đồng bộ phức tạp

## 📝 Note


