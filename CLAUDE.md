# Physical AI for Everyone — instructions for Claude Code

Open-source Physical AI curriculum: theory + hands-on + simulation.
Stack: ROS 2 Jazzy + Gazebo Harmonic on Ubuntu 24.04 (ADR-1); Astro Starlight
site, English default + Vietnamese (ADR-2); code Apache-2.0, content CC BY 4.0
(ADR-3); devcontainer + just (ADR-4); Notion as source of truth (ADR-5).

## Roles
- Nghiep: owner. Decides, approves, merges, sets tasks to Done.
- You (Claude Code): write specs, briefs and ADRs, and execute them. Nghiep decides scope.

## Notion workflow (source of truth)
- Workspace: "Physical AI for Everyone" (id <notion-id>).
- Tasks DB: <notion-id>
  (data source collection://<notion-id>).
- Lessons DB: <notion-id> · Decisions DB:
  <notion-id> · References DB: <notion-id>.
- Architecture page: <notion-id>.
- Work only on a task or lesson Nghiep names.
- Read that page plus the Lesson / Decisions / Architecture / Templates pages it needs.
- Allowed Notion writes: Status (up to In Review, or → Blocked), Branch, PR, comments,
  and the body of task and lesson pages you own. Set Done or Published only when
  Nghiep says so.
- If the brief is wrong, ambiguous or missing information: comment the question
  on the task, set Status = Blocked, and stop.

## Scope discipline
- Do exactly what the brief lists. Anything else — even if helpful (installing
  tools, editing dotfiles, ~/.bashrc, ~/.claude/*, global git config) — ask first.
- Never modify files outside this repository.
- Never weaken .claude/settings.json or .mcp.json. Editing .claude/settings.json
  reloads MCP live: tell Nghiep to restart the session afterwards.
- Never authenticate any plugin:design:* MCP server in this repo.

## Truthfulness
- Never invent numbers (dimensions, masses, sensor specs, timings, sizes).
  Mark them OPEN and state what is needed to verify them.
- Every technical claim in lesson content cites official docs or an entry in
  the Notion References DB.
- Report honestly: what was done, what was not, what failed, and why.

## IP and licensing
- No material, names, data or designs from any employer or client — ever.
  pai_bot, its worlds and all content are original to this project.
- Do not copy text or figures from sources licensed BY-SA, BY-NC or BY-NC-SA
  (e.g. d2l.ai, "Robot Learning: A Tutorial"). Link and rewrite in our own words.

## Repository conventions
- Layout follows the Architecture page. ROS packages are named pai_*.
  Create directories only when a phase needs them.
- Branch: <type>/<n>-<slug>. PR title: "<type>: <summary>" (checked by pr-title). Conventional Commits.
- Never push to main. Never merge PRs — Nghiep merges.
- Every lesson must pass headless. GUI is optional, never required to pass.
- ROS 2 checks: use `printenv ROS_DISTRO` and `ros2 pkg list`; `ros2 --version`
  is not a valid command.

## Commands
- Task runner is `just` (defined in PAI-18): `just build`, `just test`,
  `just lesson NN`, `just site-dev`, `just site-build`.
- `just lesson NN` builds, then runs `lessons/NN-*/run.sh`, which must exit non-zero
  on failure and need no GUI.
- Until the devcontainer exists (PAI-17), state every command you run.

## Content rules
- Lesson pages: English is the source; Vietnamese translation is required
  before a lesson is published. Every lesson page has 4 sections:
  Theory · Terminology · Plain-language explanation · Hands-on.
- Embed code with raw imports from source files; never paste code that can drift.
- Human-facing repo docs (README, CONTRIBUTING) are bilingual: English first,
  then Vietnamese.

## Tóm tắt tiếng Việt
- Claude Code viết cả spec, brief, ADR và thực thi; Nghiệp quyết định phạm vi.
- Chỉ làm task hoặc bài Nghiệp chỉ định, đúng phạm vi.
- Notion: được đổi Status/Branch/PR, comment và sửa thân trang task, bài mình phụ trách; chỉ đặt Done hoặc Published khi Nghiệp bảo.
- Brief sai hoặc thiếu: comment, chuyển Blocked, dừng.
- Không bịa số liệu (ghi OPEN); không dùng tài liệu của công ty nào; không chép nguồn có license không tương thích.
- Không push thẳng main, không merge PR. Mọi bài phải chạy được headless.
