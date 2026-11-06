# Lesson 01 exercises / Bài tập Bài 01

Start the system in one terminal, and run the exercises in a second one. /
Khởi động hệ thống ở một terminal, rồi làm bài ở terminal thứ hai.

```bash
source ros2_ws/install/setup.bash
ros2 launch pai_basics heartbeat.launch.py rate_hz:=10.0
```

## 1. Measure the rate / Đo tốc độ

- EN: Predict the rate of `/heartbeat`, then measure it with `ros2 topic hz`.
- VI: Dự đoán tốc độ của `/heartbeat`, rồi đo bằng `ros2 topic hz`.

## 2. Fake a gap / Giả lập mất nhịp

- EN: Without changing any code, make `monitor` report missed beats. Then read the counters through the service.
- VI: Không sửa code, hãy làm `monitor` báo mất nhịp. Sau đó đọc bộ đếm qua service.

## 3. The parameter that changes nothing / Parameter đổi mà không có tác dụng

- EN: Run `ros2 param set /heartbeat rate_hz 1.0`, then measure the rate again. Explain the result, and change `heartbeat.py` so the new value takes effect.
- VI: Chạy `ros2 param set /heartbeat rate_hz 1.0`, rồi đo lại tốc độ. Giải thích kết quả, và sửa `heartbeat.py` để giá trị mới có tác dụng.

## 4. Separate networks / Tách mạng

- EN: Run `heartbeat` with `ROS_DOMAIN_ID=59`. Try to read `/heartbeat` from domain 60, then from domain 59. Explain the difference.
- VI: Chạy `heartbeat` với `ROS_DOMAIN_ID=59`. Thử đọc `/heartbeat` từ domain 60, rồi từ domain 59. Giải thích sự khác nhau.
