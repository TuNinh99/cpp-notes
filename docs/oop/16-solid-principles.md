---
title: "SOLID principles"
---

# 16. SOLID principles

## 🧾 Content

- Single (Đơn nhiệm): mỗi class chỉ nên đảm nhiệm 1 nhiệm vụ/chức năng
ex: vi phạm class CameraManager vừa làm nhiệm vụ điều khiển phần cứng, vừa giải mã ảnh, vừa lưu ảnh vào thẻ nhớ
→ Fix: chia làm 3 class CameraController, ImageDecoder, VideoRecorder

- Open/Closed (mở/đóng): mở rộng để phát triển, đóng để sửa đổi
ex: 1 class ImageRenderer đang chỉ renderer cho ảnh jpg, giờ sếp yêu cầu render cho cả ảnh jpg, bmp, png...thì việc sửa logic của ImageRender, dẫn đến logic render jpg có nguy cơ bị ảnh hưởng, ImageRenderer sẽ trở thành 1 class rất to
→ Fix: tạo 1 interface IImage, JpgImage kế thừa từ interface ImageRenderer, khi muốn thêm 1 định dạng khác chỉ cần kế thừa ImageRenderer 

- Liskov (Thay thế Liskov): các đối tượng của lớp con phải có khả năng thay thế lớp cha mà không làm thay đổi tính đúng đắn của chương trình
ex: interface Sensor có hàm getDistance(), class CameraSensor kế thừa Sensor. Nhưng vì Camera không đo được khoảng cách trực tiếp nên hàm getDistance() return hoặc ném ra 1 exception điều này làm hỏng tính đúng đắn của các class dùng sensor chung
→ Fix: tách thành 3 interface: ISensor, IDistanceMeasurable, IImageCapturable
UltrasonicSensor (cảm biến siêu âm) kế thừa sensor & IDistanceMeasurable
CameraSensor kế thừa Sensor & IImageCapturable

- Interface (Phân tách interface): thay vì dùng interface lớn hãy dùng nhiều interface nhỏ chuyên biệt
ex: ICamera có các hàm: capture(), zoom(), turnOnFlash(), 1 chiếc camera công nghiệp k có đèn flash, k có zoom vẫn phải ngậm ngùi implement 2 hàm đó
→ Fix: tách nhỏ thành ICapture, IZoom, IFlashable, Camera nào có chức năng nào thì kế thừa chức năng đó

- Dependency (Đảo ngược phụ thuộc): các module cấp cao không nên phụ thuộc vào các module cấp thấp, cả 2 nên phụ thuộc vào abstraction (interface)
ex: SmartHomeSystem (cấp cao) khởi tạo trực tiếp SonyCamera (cấp thấp) bên trong. Khi công ty đổi sang dùng Samsung camera thì lại phải sửa hết code bên trong SmartHomeSystem
→ Fix: SmartHomeSystem chỉ nên giữ con trỏ/tham chiếu đến abstraction (ICamera),  SonyCamera & SamSungCamera phải kế thừa từ ICamera

## 📝 Note

Senior gần như chắc chắn bị hỏi
