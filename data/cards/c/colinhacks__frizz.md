# colinhacks/frizz

⭐ 29 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/colinhacks/frizz) · [官网](https://www.npmjs.com/package/frizz) · 个人维护

**本地运行的 Claude Code / Codex 编排控制台与任务队列**

运行在 localhost 的 agent 控制台：以浏览器面板驱动用户已订阅登录的 Claude Code 与 Codex CLI（自带固定版本副本），自身不带模型。核心机制包括：按项目分板的多项目单服务器（端口 9393）、agent 需要用户决策时生成问题卡片的任务队列、每线程独立后台进程（关闭浏览器或停止 Frizz 后线程仍在运行）、Snooze 定时唤醒、Goal 周期性重发目标、GitHub issue/PR 只读集成与 CI/PR 观察器。仅绑定 127.0.0.1，无云端/账号/遥测。要求 Node 22.13+ 与 Claude Code 或 Codex 订阅，支持 macOS/Linux/Windows，通过 npx frizz 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 驱动 Claude Code 与 Codex 订阅，可逐线程选择后端并同时运行
- 任务队列以问题卡片呈现 agent 待决策事项，支持多选项与备注
- 线程为独立分离后台进程，重启后自动重连仍在运行的会话
- 本地运行：绑定 127.0.0.1，无账号与遥测，审计日志记录于本地 JSONL

## 适用场景

- 在一个面板里同时管理多个仓库的多个 coding agent 会话
- 把 agent 的提问、阻塞集中成待办队列逐个处理，替代轮询终端
- 设置定时目标让 agent 持续推进（如直到 CI 变绿）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L40: - 🤖 **Claude Code *and* Codex.** Pick the backend per thread and run both against the same repo at once. Frizz supp
> L35: Frizz is a browser tab, a queue, and the agent CLIs you already pay for. It brings no model of its own, automates n

## 星数曲线

```mermaid
xychart-beta
    title "colinhacks/frizz 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 25 --> 30
    line [26, 28, 29]
```

2026-10-18 26 → 2026-10-29 29（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `593e52f68460` · [字段定义](../../DATASET.md)*
