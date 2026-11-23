# Sweetienite/personal-agent-runtime

⭐ 4 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/Sweetienite/personal-agent-runtime) · 个人维护 · 中文 README

**本地任务运行时：协调多个 CLI 编码 Agent 并独立核验结果**

PAR 是一个开源的本地协作运行时，用于连接协调者、工作者与现有应用，方式包括原生 CLI 执行、MCP 协调或人工交接。持久化 Kernel 拥有任务状态、路径权限、私有克隆与验证：独立重跑验收检查、写入需逐项审批、事件追加式记录于 SQLite 账本。以 Python 标准库运行时加 CLI 及 21 工具 MCP 桥提供，需 Python 3.11+；macOS 为已验证宿主，Windows 原生不支持，自动集成目前仅 Codex 通过验证。

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

- Kernel 独立重跑 acceptance.checks，不采信工作者自报结果
- SQLite 账本保留任务、审批、diff 与交接状态，事件追加式
- 三种接入路径：原生 CLI worker、MCP 协调者、人工交接
- 21 工具 MCP 桥与协调者租约机制，无托管控制平面

## 适用场景

- 把编码任务分派给多个不同厂商的 AI 编码工具并保留证据
- 在已购各工具配额内委派兼容任务，由 Kernel 复核结果
- 通过 MCP 客户端（如 Claude Desktop）提交与审阅任务
- 零账号场景下用导出-人工编辑-导入的交接流程参与任意工具

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: PAR is an open-source, local collaboration runtime for AI coding tools. It connects a coordinator, workers and your 
> L54: - **Stay small and local.** A Python standard-library runtime, CLI and a 21-tool MCP coordinator bridge. No PAR acc
> L74: |**Protocol coordinator**|An MCP-capable client calls PAR's 21 tools over stdio to submit, follow and review tasks.

## 星数曲线

```mermaid
xychart-beta
    title "Sweetienite/personal-agent-runtime 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-23 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `be9734d15f5c` · [字段定义](../../DATASET.md)*
