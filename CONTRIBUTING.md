# Contributing

[English](#english) · [Tiếng Việt](#tiếng-việt)

## English

Thank you for your interest in Physical AI for Everyone.

### Branches and pull requests

- Never push to `main`. All changes go through a pull request.
- After cloning, run `git config core.hooksPath .githooks` once to enable the
  pre-push hook (gitleaks blocks a push that contains a secret).
- Branch name: `<type>/<n>-<slug>`, where `<n>` is the issue number
  (for example `chore/17-hook-checks`).
- Pull request title: `<type>: <summary>`, lower case, imperative, no trailing
  period (for example `docs: add lesson 03 outline`). Types: `feat`, `fix`,
  `chore`, `refactor`, `docs`, `test`, `ci`. The `pr-title` check enforces it.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, …).
- The maintainer reviews and merges pull requests.

### Content rules

- Lessons are written in English first; a Vietnamese translation is required
  before a lesson is published.
- Do not invent numbers (dimensions, masses, sensor specs, timings). Mark
  unknown values as OPEN.
- Cite official documentation for technical claims.
- Do not copy text or figures from sources licensed BY-SA, BY-NC or BY-NC-SA.
  Link to them and rewrite in your own words.

### Licensing of contributions

By contributing, you agree that your contributions are licensed under this
repository's licenses: source code under the [Apache License 2.0](LICENSE), and
lesson text, figures and videos under [CC BY 4.0](LICENSE-CONTENT).

### Code of conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Tiếng Việt

Cảm ơn bạn đã quan tâm đến Physical AI for Everyone.

### Nhánh và pull request

- Không push thẳng lên `main`. Mọi thay đổi đều đi qua pull request.
- Sau khi clone, chạy `git config core.hooksPath .githooks` một lần để bật hook
  pre-push (gitleaks chặn push có chứa secret).
- Tên nhánh: `<type>/<n>-<slug>`, với `<n>` là số issue
  (ví dụ `chore/17-hook-checks`).
- Tiêu đề pull request: `<type>: <tóm tắt>`, viết thường, thể mệnh lệnh, không
  có dấu chấm cuối (ví dụ `docs: add lesson 03 outline`). Các type: `feat`,
  `fix`, `chore`, `refactor`, `docs`, `test`, `ci`. Check `pr-title` kiểm tra
  quy tắc này.
- Commit message theo [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, …).
- Maintainer review và merge pull request.

### Quy tắc nội dung

- Bài học viết bằng tiếng Anh trước; phải có bản dịch tiếng Việt trước khi
  xuất bản.
- Không bịa số liệu (kích thước, khối lượng, thông số cảm biến, thời gian).
  Giá trị chưa biết ghi là OPEN.
- Trích dẫn tài liệu chính thức cho các khẳng định kỹ thuật.
- Không chép văn bản hoặc hình từ nguồn có giấy phép BY-SA, BY-NC hoặc
  BY-NC-SA. Hãy dẫn link và viết lại bằng lời của mình.

### Giấy phép cho phần đóng góp

Khi đóng góp, bạn đồng ý rằng phần đóng góp được cấp phép theo giấy phép của
repo: mã nguồn theo [Apache License 2.0](LICENSE), còn nội dung bài học, hình
và video theo [CC BY 4.0](LICENSE-CONTENT).

### Quy tắc ứng xử

Dự án tuân theo [Contributor Covenant](CODE_OF_CONDUCT.md).
