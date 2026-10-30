# btangonan/anima

⭐ 18 · JavaScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/btangonan/anima) · 个人维护

**macOS 原生 Claude Code 客户端：多会话面板与 ASCII 伙伴**

Tauri v2 + Rust 构建的 4MB macOS 桌面应用，将 Claude Code 作为子进程启动并渲染自有 UI，提供多会话面板、跨会话 Rust 守护进程（监测重试循环与高频读取模式）、会话历史回放、语音输入（可选，WebSocket 桥接）及每会话模型/力度切换。每个项目生成一个 ASCII 伙伴，token 消耗折算 nim 货币用于重掷。Oracle 评论通过 claude CLI 后台提示运行，本地处理。需自行从源码构建，无签名 dmg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以子进程方式运行 Claude Code 并自渲染多会话界面
- Rust 守护进程跨会话监测工具调用模式（重试循环/高频读取）
- 每项目持久化 ASCII 伙伴与 nim token 经济
- Oracle 评论经完整 Claude 模型生成，文本可选可粘贴

## 适用场景

- 在一个窗口中同时管理多个 Claude Code 会话
- 让守护进程提醒陷入循环或低效模式的会话
- 给常用项目保留一个陪伴型 ASCII 伙伴

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L22: Anima spawns Claude Code as a subprocess, pipes stream-json, renders messages in its own UI, and manages sessions. 
> L25: 2. **Cross-session watcher.** A Rust daemon monitors tool patterns across all sessions. Catches retry loops and rea
> L53: Commentary runs as short background prompts via the Claude CLI, capped at 2 concurrent calls. All processing is loc

## 星数曲线

```mermaid
xychart-beta
    title "btangonan/anima 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7fbe6e70917c` · [字段定义](../../DATASET.md)*
