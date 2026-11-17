# Lesson 01 solutions / Lời giải Bài 01

Every result below was run in the devcontainer. /
Mọi kết quả dưới đây đều đã được chạy thật trong devcontainer.

## 1. Measure the rate / Đo tốc độ

```bash
ros2 topic hz /heartbeat
```

- EN: The launch argument sets 10 Hz, and the measured average was 9.998 to 10.000 Hz. A timer runs in software, so small differences are normal.
- VI: Tham số launch đặt 10 Hz, kết quả đo trung bình là 9.998 đến 10.000 Hz. Timer chạy bằng phần mềm nên sai lệch nhỏ là bình thường.

## 2. Fake a gap / Giả lập mất nhịp

```bash
ros2 topic pub --once /heartbeat std_msgs/msg/UInt32 "{data: 100000}"
ros2 service call /monitor/reset std_srvs/srv/Trigger
```

- EN: A topic can have several publishers, and a subscriber does not know which one sent a message. `monitor` sees a number far ahead of the last one and logs `Missed ... beat(s) before 100000`. The service reply shows the counters.
- VI: Một topic có thể có nhiều publisher, và subscriber không biết ai gửi. `monitor` thấy một số lớn hơn hẳn số trước đó nên ghi `Missed ... beat(s) before 100000`. Kết quả service cho biết bộ đếm.

## 3. The parameter that changes nothing / Parameter đổi mà không có tác dụng

- EN: `ros2 param set` reports success and `ros2 param get` returns 1.0, but the rate stays at about 10 Hz. The stored value changed, but `heartbeat.py` read it only once, to create the timer. React to the change with a callback:
- VI: `ros2 param set` báo thành công và `ros2 param get` trả về 1.0, nhưng tốc độ vẫn khoảng 10 Hz. Giá trị lưu đã đổi, nhưng `heartbeat.py` chỉ đọc nó một lần để tạo timer. Cần phản ứng với thay đổi bằng callback:

```python
# In __init__, keep the timer and register the callback:
self._timer = self.create_timer(1.0 / rate_hz, self._beat)
self.add_post_set_parameters_callback(self._on_parameters_set)

# New method:
def _on_parameters_set(self, parameters):
    for parameter in parameters:
        if parameter.name == 'rate_hz':
            self.destroy_timer(self._timer)
            self._timer = self.create_timer(1.0 / parameter.value, self._beat)
```

- EN: With this change, the measured rate became 1.000 Hz. This example does not reject a value of 0, which would raise an error.
- VI: Với thay đổi này, tốc độ đo được là 1.000 Hz. Ví dụ này chưa chặn giá trị 0, giá trị đó sẽ gây lỗi.

## 4. Separate networks / Tách mạng

```bash
ROS_DOMAIN_ID=59 ros2 run pai_basics heartbeat
ROS_DOMAIN_ID=60 timeout 5 ros2 topic echo --once /heartbeat std_msgs/msg/UInt32
ROS_DOMAIN_ID=59 timeout 8 ros2 topic echo --once /heartbeat std_msgs/msg/UInt32
```

- EN: Domain 60 receives nothing and `timeout` stops it (exit code 124). Domain 59 prints a message. Nodes on different domains cannot discover each other.
- VI: Domain 60 không nhận được gì và bị `timeout` dừng (mã thoát 124). Domain 59 in ra một message. Các node khác domain không tìm thấy nhau.

## Code exercises / Bài tập viết code

- EN: The answers to exercises 5 to 7 are in `ros2_ws/src/pai_basics/pai_basics/lesson01_solutions.py`. `test/test_lesson01_solutions.py` checks them, and `just test` runs it in CI on every pull request.
- VI: Lời giải bài 5 đến 7 nằm trong `ros2_ws/src/pai_basics/pai_basics/lesson01_solutions.py`. `test/test_lesson01_solutions.py` kiểm tra chúng, và `just test` chạy test này trong CI ở mọi pull request.

## 5. A safe period / Chu kỳ an toàn

- EN: The check is `not rate_hz > 0`, not `rate_hz <= 0`. Every comparison with `nan` is false, so `nan <= 0` is false and `nan` would slip through. `math.isinf` catches infinity, whose period would be 0.
- VI: Phép kiểm là `not rate_hz > 0`, không phải `rate_hz <= 0`. Mọi phép so sánh với `nan` đều sai, nên `nan <= 0` là sai và `nan` sẽ lọt qua. `math.isinf` chặn vô cùng, vì chu kỳ của nó sẽ bằng 0.

## 6. How much was lost / Mất bao nhiêu

- EN: Every expected beat was either received or missed, so the ratio is `missed / (received + missed)`. Before any beat, nothing was expected and the answer is 0.0, not a division by zero. Example: beats 0, 1, 2, 5 give 4 received and 2 missed, so the ratio is 2/6.
- VI: Mỗi nhịp mong đợi hoặc đã nhận, hoặc đã mất, nên tỉ lệ là `missed / (received + missed)`. Khi chưa có nhịp nào thì chưa mong đợi gì, kết quả là 0.0 chứ không phải lỗi chia cho 0. Ví dụ: các nhịp 0, 1, 2, 5 cho 4 nhịp nhận và 2 nhịp mất, nên tỉ lệ là 2/6.

## 7. Count the restarts / Đếm số lần khởi động lại

- EN: Two details matter. First, check for a restart before calling `super().update(seq)`, because the parent overwrites `last_seq`. Second, `BeatTracker.__init__` calls `reset()`, so overriding `reset()` to set `restarts = 0` also creates the counter. No `__init__` is needed.
- VI: Có hai chi tiết quan trọng. Thứ nhất, kiểm tra khởi động lại trước khi gọi `super().update(seq)`, vì lớp cha ghi đè `last_seq`. Thứ hai, `BeatTracker.__init__` gọi `reset()`, nên ghi đè `reset()` để đặt `restarts = 0` cũng tạo luôn bộ đếm. Không cần viết `__init__`.
