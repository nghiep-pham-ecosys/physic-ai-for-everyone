# Physical AI for Everyone

[English](#english) · [Tiếng Việt](#tiếng-việt)

## English

### Vision

An open-source Physical AI curriculum that combines theory, hands-on practice
and simulation, so anyone can learn how intelligent robots perceive, decide and
act. Lessons are written in English first, with a Vietnamese translation.

Planned stack: ROS 2 Jazzy and Gazebo Harmonic on Ubuntu 24.04, with an Astro
Starlight documentation site.

### Website

Read the course at <https://nghiep-pham-ecosys.github.io/physic-ai-for-everyone/>.
The site in `site/` is built and deployed to GitHub Pages by
`.github/workflows/pages.yml` on every push to `main`.

### Status

**Phase 0 is done (`v0.1.0`).** The repository, development environment, CI
and site are in place; there are no lessons yet.

### What is in this repository

| File | Purpose |
| --- | --- |
| `README.md` | This overview |
| `LICENSE` | Apache License 2.0 — applies to source code |
| `LICENSE-CONTENT` | CC BY 4.0 — applies to lesson text, figures and videos |
| `CONTRIBUTING.md` | How to contribute |
| `CODE_OF_CONDUCT.md` | Contributor Covenant 2.1 |
| `CLAUDE.md` | Working rules for the Claude Code assistant |
| `.github/` | CI workflows, pull request and issue templates |
| `docker/`, `.devcontainer/` | CPU development image and VS Code devcontainer |
| `justfile` | Task runner: `just build`, `just test`, `just site-dev`, `just site-build` |
| `ros2_ws/` | ROS 2 workspace |
| `site/` | Astro Starlight website (EN/VI) |

### Setup

The development environment is a Docker image with ROS 2 Jazzy, Gazebo
Harmonic (via `ros_gz`), `just` and Node.js LTS. It needs only a CPU.

1. Install [Docker](https://docs.docker.com/get-started/get-docker/) and
   [VS Code](https://code.visualstudio.com/) with the
   [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
   extension. On Windows, use WSL 2 and enable Docker Desktop's WSL integration.
2. Clone this repository and open it in VS Code.
3. Run **Dev Containers: Reopen in Container**. The first build downloads the
   base image and takes a while.
4. In the container terminal, check the environment:

   ```bash
   printenv ROS_DISTRO   # jazzy
   ros2 pkg list
   gz sim --version
   ```

The repository is mounted at `/workspace`. Without VS Code, build the image
with `docker build -f docker/Dockerfile -t pai-dev:cpu .`.

### Licenses

- Code: [Apache License 2.0](LICENSE).
- Lesson content (text, figures, videos): [CC BY 4.0](LICENSE-CONTENT).

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Tiếng Việt

### Tầm nhìn

Một giáo trình Physical AI mã nguồn mở, kết hợp lý thuyết, thực hành và mô
phỏng, để ai cũng có thể học cách robot thông minh cảm nhận, ra quyết định và
hành động. Bài học được viết bằng tiếng Anh trước, kèm bản dịch tiếng Việt.

Nền tảng dự kiến: ROS 2 Jazzy và Gazebo Harmonic trên Ubuntu 24.04, cùng trang
tài liệu Astro Starlight.

### Website

Đọc giáo trình tại <https://nghiep-pham-ecosys.github.io/physic-ai-for-everyone/>.
Site trong `site/` được build và deploy lên GitHub Pages bởi
`.github/workflows/pages.yml` mỗi lần push lên `main`.

### Trạng thái

**Phase 0 đã xong (`v0.1.0`).** Repo, môi trường phát triển, CI và site đã sẵn
sàng; chưa có bài học nào.

### Repo này có gì

| File | Mục đích |
| --- | --- |
| `README.md` | Tổng quan này |
| `LICENSE` | Apache License 2.0 — áp dụng cho mã nguồn |
| `LICENSE-CONTENT` | CC BY 4.0 — áp dụng cho nội dung bài học, hình và video |
| `CONTRIBUTING.md` | Hướng dẫn đóng góp |
| `CODE_OF_CONDUCT.md` | Bộ quy tắc ứng xử Contributor Covenant 2.1 |
| `CLAUDE.md` | Quy tắc làm việc cho trợ lý Claude Code |
| `.github/` | Workflow CI, mẫu pull request và issue |
| `docker/`, `.devcontainer/` | Image phát triển CPU và devcontainer cho VS Code |
| `justfile` | Công cụ chạy lệnh: `just build`, `just test`, `just site-dev`, `just site-build` |
| `ros2_ws/` | Workspace ROS 2 |
| `site/` | Website Astro Starlight (EN/VI) |

### Cài đặt

Môi trường phát triển là một Docker image có sẵn ROS 2 Jazzy, Gazebo Harmonic
(qua `ros_gz`), `just` và Node.js LTS. Chỉ cần CPU.

1. Cài [Docker](https://docs.docker.com/get-started/get-docker/) và
   [VS Code](https://code.visualstudio.com/) kèm extension
   [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
   Trên Windows, dùng WSL 2 và bật WSL integration trong Docker Desktop.
2. Clone repo này và mở bằng VS Code.
3. Chạy **Dev Containers: Reopen in Container**. Lần build đầu phải tải image
   gốc nên sẽ mất một lúc.
4. Trong terminal của container, kiểm tra môi trường:

   ```bash
   printenv ROS_DISTRO   # jazzy
   ros2 pkg list
   gz sim --version
   ```

Repo được mount tại `/workspace`. Nếu không dùng VS Code, build image bằng
`docker build -f docker/Dockerfile -t pai-dev:cpu .`.

### Giấy phép

- Mã nguồn: [Apache License 2.0](LICENSE).
- Nội dung bài học (văn bản, hình, video): [CC BY 4.0](LICENSE-CONTENT).

### Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
