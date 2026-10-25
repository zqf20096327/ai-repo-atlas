# spleck/claw-dashboard

⭐ 122 · JavaScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/spleck/claw-dashboard) · [官网](https://www.npmjs.com/package/claw-dashboard) · 个人维护

**终端实时监控面板：监控 OpenClaw 实例与系统资源**

基于 Node.js 与 blessed 构建的终端 UI 仪表盘，用于监控 OpenClaw 实例：实时会话跟踪、agent 状态、安全审计与 token 用量，同时展示 CPU/内存/GPU（Apple Silicon）、进程、磁盘与网络等系统指标，默认 2 秒自动刷新。提供 9 种可拖拽排列/固定的小部件、4 套主题、命令面板、JSON/CSV 导出与快照导入导出，支持 screen/tmux/pm2/LaunchAgent 持久化运行。前置条件为 Node.js v22+ 与已安装的 OpenClaw，macOS（Apple Silicon 优化）环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenClaw 会话跟踪、agent 状态与安全审计
- CPU/内存/GPU（Apple Silicon）/进程等系统指标实时展示
- 小部件拖拽排列、固定与主题选择、命令面板
- JSON/CSV 导出、定时导出调度与快照配置导入导出

## 适用场景

- 在终端实时查看 OpenClaw 会话与 token 消耗
- 监控运行 OpenClaw 的机器的系统资源
- 通过 tmux/pm2 让仪表盘常驻后台运行

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A beautiful, real-time terminal dashboard for monitoring OpenClaw instances — inspired by modern system monitors lik
> L16: - **🤖 OpenClaw Integration**: Live session tracking, agent status, security audit

## 星数曲线

```mermaid
xychart-beta
    title "spleck/claw-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 121 --> 123
    line [122, 122]
```

2026-10-18 122 → 2026-10-25 122（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a239c38a54c1` · [字段定义](../../DATASET.md)*
