# Lesson 02 exercises / Bài tập Bài 02

Start the frame tree in one terminal, and run the exercises in a second one. /
Khởi động cây frame ở một terminal, rồi làm bài ở terminal thứ hai.

```bash
source ros2_ws/install/setup.bash
ros2 launch pai_basics frames.launch.py
```

## 1. Compose by hand / Ghép bằng tay

- EN: `odom` is 2.0 m along x of `map`. `base_link` is at (1, 0) in `odom`, turned 90 degrees left. `sensor` is 0.2 m along x of `base_link`. Where is `sensor` in `map`? Work it out on paper, then check it with `rigid2d`.
- VI: `odom` cách `map` 2.0 m theo trục x. `base_link` ở (1, 0) trong `odom`, quay trái 90 độ. `sensor` cách `base_link` 0.2 m theo trục x. `sensor` ở đâu trong `map`? Tính trên giấy, rồi kiểm tra bằng `rigid2d`.

## 2. Add a frame / Thêm frame

- EN: From the command line, add a frame `bumper` 0.1 m to the left of `sensor`. Predict its position relative to `base_link`, then check with `tf2_echo`.
- VI: Từ dòng lệnh, thêm frame `bumper` cách `sensor` 0.1 m về bên trái. Dự đoán vị trí của nó so với `base_link`, rồi kiểm tra bằng `tf2_echo`.

## 3. The silent failure / Lỗi im lặng

- EN: While the system runs, stop only `circle_broadcaster`. What does `sensor_locator` log? Why is that dangerous on a real robot? How could the code detect it?
- VI: Khi hệ thống đang chạy, chỉ dừng `circle_broadcaster`. `sensor_locator` ghi gì? Vì sao điều đó nguy hiểm trên robot thật? Code có thể phát hiện bằng cách nào?

## 4. Two parents / Hai parent

- EN: Publish a static transform `map` -> `base_link` while the system runs. Does `base_link` move to the new place? Use `tf2_echo map sensor` and `view_frames` to find out.
- VI: Phát transform tĩnh `map` -> `base_link` khi hệ thống đang chạy. `base_link` có chuyển đến chỗ mới không? Dùng `tf2_echo map sensor` và `view_frames` để tìm hiểu.
