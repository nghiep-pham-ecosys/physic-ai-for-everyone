# Lesson 02 solutions / Lời giải Bài 02

Every result below was run in the devcontainer. /
Mọi kết quả dưới đây đều đã được chạy thật trong devcontainer.

## 1. Compose by hand / Ghép bằng tay

- EN: Start from the sensor and walk up the tree. In `base_link` it is at (0.2, 0). The robot is turned 90 degrees left, so forward means +y of `odom`: the sensor is at (1, 0.2) in `odom`. Adding the `map` offset gives (3, 0.2).
- VI: Bắt đầu từ sensor và đi ngược lên cây. Trong `base_link` nó ở (0.2, 0). Robot quay trái 90 độ, nên hướng trước của robot là +y của `odom`: sensor ở (1, 0.2) trong `odom`. Cộng thêm độ lệch của `map` được (3, 0.2).

```python
import math
from pai_basics.rigid2d import apply, transform

whole = transform(2, 0, 0) @ transform(1, 0, math.pi / 2) @ transform(0.2, 0, 0)
print(apply(whole, (0, 0)))  # (3.0, 0.2), up to rounding
```

## 2. Add a frame / Thêm frame

```bash
ros2 run tf2_ros static_transform_publisher --y 0.1 --frame-id sensor --child-frame-id bumper
ros2 run tf2_ros tf2_echo base_link bumper
```

- EN: REP-103 says +y is left. The result is `Translation: [0.200, 0.100, 0.000]`.
- VI: REP-103 quy định +y là bên trái. Kết quả là `Translation: [0.200, 0.100, 0.000]`.

## 3. The silent failure / Lỗi im lặng

```bash
pkill -INT -f circle_broadcaster
```

- EN: `sensor_locator` keeps logging exactly the same position, with no warning. `Time()` asks for the latest transform available, and the last one is still stored. On a real robot, the software would believe the robot stands still in an old place while it may be moving.
- EN: To detect it, compare the `header.stamp` of the result with the current time, and warn when it is too old. A new `tf2_echo map sensor` started after the stop could not connect the frames, because it never received `odom` -> `base_link`.
- VI: `sensor_locator` vẫn ghi đúng một vị trí cũ, không có cảnh báo nào. `Time()` nghĩa là lấy transform mới nhất đang có, và giá trị cuối vẫn được lưu lại. Trên robot thật, phần mềm sẽ tưởng robot đứng yên ở chỗ cũ trong khi nó có thể đang chạy.
- VI: Để phát hiện, hãy so `header.stamp` của kết quả với thời gian hiện tại, và cảnh báo khi quá cũ. Một `tf2_echo map sensor` mới mở sau khi dừng không nối được các frame, vì nó chưa từng nhận `odom` -> `base_link`.

## 4. Two parents / Hai parent

```bash
ros2 run tf2_ros static_transform_publisher --x 5.0 --frame-id map --child-frame-id base_link
ros2 run tf2_ros tf2_echo map sensor
```

- EN: In our run, `sensor` kept following the circle around (2, 0), and `view_frames` still showed `odom` as the parent of `base_link`. The static message was overwritten by the steady stream from `circle_broadcaster`. No error appears, so this mistake is easy to miss. REP-105 allows each frame only one parent.
- VI: Trong lần chạy của chúng tôi, `sensor` vẫn đi theo vòng tròn quanh (2, 0), và `view_frames` vẫn cho thấy `odom` là parent của `base_link`. Message tĩnh bị luồng dữ liệu liên tục từ `circle_broadcaster` ghi đè. Không có lỗi nào hiện ra nên sai lầm này dễ bị bỏ sót. REP-105 chỉ cho phép mỗi frame có một parent.
