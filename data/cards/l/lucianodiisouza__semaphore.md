# lucianodiisouza/semaphore

⭐ 48 · Rust · MIT · 推送 2026-07-03 · [GitHub](https://github.com/lucianodiisouza/semaphore) · 个人维护

**悬浮红绿灯桌面小部件：显示 AI 编程代理的空闲/思考/写文件状态**

系统托盘常驻的桌面小部件（Tauri + Rust + TypeScript），通过向 AI 编程工具（Cursor、Claude Code、Codex CLI、Gemini CLI、Copilot CLI）安装 hooks 接收生命周期事件，经 sem-hook 与 semctl 以换行分隔 JSON 的 IPC 协议转发到状态机，按会话聚合并以红/黄/绿灯光显示代理当前状态。支持主题、i18n（英语/巴西葡语）、声音提示、隐身模式，并可把灯光显示到 Elgato Stream Deck 按键（每 500ms 刷新）。提供 macOS/Linux/Windows 预构建安装包，捆绑 semctl CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 hooks 接入 Cursor、Claude Code、Codex CLI、Gemini CLI、Copilot CLI 五种工具
- 按 session 聚合的状态机，红>黄>绿优先级，空闲会话按超时修剪
- semctl CLI 提供 set/status/install/uninstall/doctor/launch 命令
- Stream Deck 插件将灯光同步到实体按键

## 适用场景

- 在全屏写代码时无需切窗口即可知道 AI 代理是否在等我
- 多会话并行使用 AI 编程工具时统一查看各会话状态
- 状态变化时用声音提示提醒我代理已完成或开始写文件

## 场景标签

 · 领域:开发工具/AI 代理监控

## 证据(README 行号)

> L3: Floating traffic light for AI coding agents. Shows when your agent is idle, thinking, or writing files, without swit
> L209: 1. **Hooks fire** when an AI tool starts thinking, uses a tool, edits a file, or finishes a turn.
> L212: 4. **State machine** tracks one entry per session ID and picks the highest-priority color: **red > yellow > green*

## 星数曲线

```mermaid
xychart-beta
    title "lucianodiisouza/semaphore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1a8d43761c02` · [字段定义](../../DATASET.md)*
