# xsota/same

⭐ 4 · Rust · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/xsota/same) · 个人维护

**给开发者的本地多 provider AI agent 桌面工作区**

Rust 编写的本地优先 AI agent 桌面工作区：内置 ACP v1 stdio 客户端，并为无 ACP 包装的 agent 提供原生 CLI 适配器，接入 Claude Code、Codex、OpenCode、Antigravity 等。工作流按 Workspace→Project→Quest→Session 组织，提供流式输出、工具调用与审批卡片、用量仪表盘（读取 CLI 本地限额与历史，不消耗 token）、文件/Git 面板与 Windows/WSL 支持。配置（TOML）与对话历史（SQLite）全部存本地，零遥测。需经 cargo 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置 ACP v1 客户端及 Claude Code/Codex/OpenCode/Antigravity 原生 CLI 适配器
- 用量仪表盘读取本地 CLI 限额与 token 历史，不消耗 token
- 本地优先存储（TOML+SQLite），零遥测、无强制账号
- 跨 provider 统一的审批模式（Plan/Ask/Accept edits/Full access）

## 适用场景

- 在一个桌面界面统一管理 Claude Code、Codex 等编码 agent 会话
- 查看各 agent 订阅计划限额与每日 token 消耗统计
- Windows/WSL 混合环境下按项目位置选择 agent 运行环境

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: A lightweight, local-first, multi-provider AI agent desktop workspace written in Rust.
> L9: - **ACP First, Not ACP Only**: Built-in Agent Client Protocol (ACP) v1 client over stdio, plus native CLI adapters f
> L88: ├── same-agent/   # Provider-agnostic AgentRuntime, Capabilities, Provider adapters

## 星数曲线

```mermaid
xychart-beta
    title "xsota/same 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-27 4 → 2026-11-28 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f2dfa8c2ee11` · [字段定义](../../DATASET.md)*
