# tageecc/clawteam

⭐ 14 · TypeScript · MIT · 推送 2026-04-03 · [GitHub](https://github.com/tageecc/clawteam) · [官网](https://github.com/tageecc/pond) · 个人维护 · 中文 README

**OpenClaw 桌面控制中心：多实例编排、团队协作与实时监控**

基于 Tauri 2（Rust）+ React 19 的桌面应用，面向运行 OpenClaw 多个 agent 实例的用户：提供 Gateway 进程生命周期管理（启停/重启、端口内存 CPU 监控）、多实例编排（dev/test/prod 目录隔离、统一视图切换）、可视化编辑 openclaw.json、团队协作层（Leader/执行者角色、open→claimed→done/failed 任务状态机、WebSocket 实时通知）、流式聊天与工具执行时间线，以及 token 用量/成本/系统资源分析。技能安装更新、日志聚合、诊断工具与配置备份亦内置。提供 macOS/Windows/Linux 安装包，本地开发需 Node.js 20+、pnpm、Rust。

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

- 单机多 OpenClaw 实例编排（目录隔离、独立 Gateway 进程、统一监控视图）
- 团队协作层：角色管理、open→claimed→done/failed 任务状态机、实时通知
- WebSocket 流式聊天，含工具调用时间线与推理过程可视化
- token 用量/成本/会话/系统资源实时分析与 CSV 导出

## 适用场景

- 在一台机器上同时运行开发/测试/生产多个 OpenClaw 实例并统一监控
- 多人多 agent 团队分配任务并跟踪状态流转
- 可视化编辑 openclaw.json 配置，避免手写 JSON
- 查看各实例 token 消耗与成本趋势并导出报告

## 场景标签

`多智能体` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Desktop Control Center for OpenClaw — Unified Operations, Team Collaboration & Multi-Instance Orchestration**
> L37: - 🚀 **One-Click Gateway Control** — Manage process lifecycle per instance, monitor ports, memory, and logs in real-
> L145:   │  React UI   │────▶│ Tauri (Rust) │────▶│ OpenClaw Gateway │

## 星数曲线

```mermaid
xychart-beta
    title "tageecc/clawteam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `662fe0d5db1c` · [字段定义](../../DATASET.md)*
