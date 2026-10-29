# DotHarness/dotcraft-unity

⭐ 24 · C# · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/DotHarness/dotcraft-unity) · 组织维护 · 中文 README

**让 AI agent 在 Unity Editor 内运行 C# 与自动化的集成工具**

面向 Unity 开发者的 AI agent 集成层：agent 可在运行中的 Unity Editor 里执行 C#、编译脚本并读取错误、跟踪 play mode 与重载状态，核心功能无需向项目安装任何内容。可选的 Unity 包（UPM）额外提供编辑器内聊天、面向其他编码 agent 的 MCP Gateway 及项目自定义工具。要求 Unity 2021.3 至 6.6 的 Mono 运行时，不支持 CoreCLR。支持 DotCraft、Codex 插件市场及其他带 Skills 目录的 agent 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 在运行中的 Unity Editor 内执行 C# 并读取编译错误
- 无需向项目安装内容即可使用的 CLI 路径
- 可选 Unity 包提供编辑器内聊天、MCP Gateway 与自定义工具
- 跟踪 play mode 与域重载状态

## 适用场景

- 让编码 agent 直接操作 Unity 场景与脚本
- 在编辑器内与 agent 对话完成开发任务
- 通过 MCP Gateway 接入其他编码 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Unified AI agent integration for Unity Editor—in-editor chat, CLI/MCP automation, and the option to use it without i
> L9: Your agent can run C# in a running Unity Editor, compile scripts and read the errors, and keep track of play mode an
> L11: Requires Unity 2021.3 to 6.6 on the Mono runtime. CoreCLR is not supported yet.

## 星数曲线

```mermaid
xychart-beta
    title "DotHarness/dotcraft-unity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `376811ab0546` · [字段定义](../../DATASET.md)*
