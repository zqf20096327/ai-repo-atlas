# yicheng47/runner

⭐ 362 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/yicheng47/runner) · [官网](https://runnersh.dev/) · 个人维护 · 中文 README

**让多个终端 CLI 编码 agent 在一个任务中协作的桌面应用**

Runner 是原生 macOS/Windows 桌面应用，把 Claude Code、Codex、Copilot CLI 等 CLI 编码 agent 组织成可复用的 crew（角色编队），在真实 PTY 终端中并行运行同一任务，通过共享 mission feed 协调并向用户提问。支持分屏、桌面通知、后台服务 runnerd 保持会话、统一管理各 agent 的 MCP 与 skills，并提供 `runner` CLI 供脚本和其他 agent 驱动。自身不安装 agent CLI，需用户预先安装并登录。默认 crew 为 coder/reviewer 结对编程循环。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent crew 编排：共享 mission feed、每槽位独立真实 PTY 终端
- `runner` CLI 可从外部/其他 agent 驱动完整 mission（含 --json 输出）
- runnerd 后台服务：应用关闭或崩溃后重开可恢复原终端会话
- 统一管理各 agent 的 MCP servers 与 skills 开关

## 适用场景

- 让 coder/reviewer/QA 多 agent 协作完成编码任务
- 跨厂商（如 codex + claude-code）结对编程互相审查
- 通过 CLI 脚本化启动和跟进 agent mission

## 场景标签

 · 领域:开发者工具/agent 编排

## 证据(README 行号)

> L16:  Claude Code, Codex, Antigravity CLI, Copilot CLI and pi on the same task, in one mission. Each agent keeps its own
> L38: Runner brings CLI coding agents together in reusable crews, with real terminals and a shared mission feed. Your ses
> L89: Runner runs the agent CLIs you already use; it does not install them. Install and sign in to at least one of Claude

## 星数曲线

```mermaid
xychart-beta
    title "yicheng47/runner 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 333 --> 342
    line [334, 341, 341]
```

2026-10-18 334 → 2026-10-21 341（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2dc205a0a6c3` · [字段定义](../../DATASET.md)*
