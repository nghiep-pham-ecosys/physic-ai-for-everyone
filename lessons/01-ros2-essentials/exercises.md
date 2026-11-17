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

## Code exercises / Bài tập viết code

- EN: Exercises 5 to 7 need no running system. Write plain Python next to `beat_tracker.py` in `ros2_ws/src/pai_basics/pai_basics/`. The test `test/test_lesson01_solutions.py` checks the answers. To check yours, put your module's name in its import line, then run `just test`.
- VI: Bài 5 đến 7 không cần chạy hệ thống. Viết Python thuần cạnh `beat_tracker.py` trong `ros2_ws/src/pai_basics/pai_basics/`. Test `test/test_lesson01_solutions.py` kiểm tra lời giải. Để kiểm bài của bạn, đặt tên module của bạn vào dòng import của test, rồi chạy `just test`.

## 5. A safe period / Chu kỳ an toàn

- EN: Write `period_from_rate(rate_hz)`. It returns the timer period in seconds, and raises `ValueError` for a rate that is zero, negative, `nan` or infinite. Exercise 3 needs exactly this check.
- VI: Viết `period_from_rate(rate_hz)`. Hàm trả về chu kỳ timer theo giây, và báo `ValueError` khi tốc độ bằng 0, âm, `nan` hoặc vô cùng. Bài 3 cần đúng phép kiểm này.

## 6. How much was lost / Mất bao nhiêu

- EN: Write `loss_ratio(tracker)`. It takes a `BeatTracker` and returns the share of expected beats that never arrived, from 0.0 to 1.0. What should it return before any beat arrives?
- VI: Viết `loss_ratio(tracker)`. Hàm nhận một `BeatTracker` và trả về tỉ lệ nhịp mong đợi nhưng không đến, từ 0.0 đến 1.0. Hàm nên trả về gì khi chưa có nhịp nào?

## 7. Count the restarts / Đếm số lần khởi động lại

- EN: `BeatTracker` treats a number that is lower than or equal to the last one as a publisher restart, but it does not count restarts. Write `RestartTracker`, a subclass with a `restarts` counter that `reset()` clears. Do not copy the gap logic: call the parent class.
- VI: `BeatTracker` coi một số nhỏ hơn hoặc bằng số trước là publisher khởi động lại, nhưng không đếm số lần đó. Viết `RestartTracker`, lớp con có bộ đếm `restarts` được `reset()` xoá về 0. Đừng chép lại phần đếm nhịp mất: hãy gọi lớp cha.
