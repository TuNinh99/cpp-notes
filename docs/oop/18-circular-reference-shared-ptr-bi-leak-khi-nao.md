---
title: "Circular reference, shared_ptr bị leak khi nào?"
---

# 18. Circular reference, shared_ptr bị leak khi nào?

## 🧾 Content


```cpp
Khi 2 object giữ shared_ptr lẫn nhau → không release → cần weak_ptr.
struct Node &#123;
    std::shared_ptr&lt;Node&gt; neighbor;
    ~Node() &#123; std::cout &lt;&lt; "Da xoa Node\n"; &#125;
&#125;;

void leak_vi_du() &#123;
    auto A = std::make_shared&lt;Node&gt;();
    auto B = std::make_shared&lt;Node&gt;();

    A-&gt;neighbor = B; // A giữ B
    B-&gt;neighbor = A; // B giữ A (Vòng lặp!)
&#125; // Hết hàm, A và B vẫn giữ nhau -&gt; Không bao giờ bị xóa.
---&gt; solution: thay std::shared_ptr trong Node bằng weak_ptr
```


## 📝 Note

Hay hỏi follow-up
