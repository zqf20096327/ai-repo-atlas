# CoplayDev/unity-mcp

⭐ 15,085 · C# · MIT · 推送 2026-10-17 · [GitHub](https://github.com/CoplayDev/unity-mcp) · [官网](https://coplaydev.github.io/unity-mcp/) · 组织维护

**给 Unity 开发者的 MCP 桥：让 AI 助手控制编辑器**

通过 Model Context Protocol 将 AI 助手（Claude、Cursor、VS Code、本地 LLM 等）接入 Unity Editor，提供 50 个 MCP 工具入口，支持自然语言创建场景与 GameObject、编辑 C# 脚本、管理资产、运行测试、性能分析与构建。要求 Unity 2021.3 LTS 至 6.x 及 Python 3.10+（经 uv）。安装方式为 Unity Package Manager 的 git URL 或 openupm，可在多个客户端自动配置，MIT 许可，另支持多实例路由、工具分组、远程服务器鉴权等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 9.5 天,年发版 64,82 位贡献者
- 涨星:近 1 天 **+43**(自 20261016 起算)
- 平台:— · 协议:MCP

## 能力要点

- 50 个 MCP 工具入口，任意 MCP 客户端可用
- 自然语言控制 Unity Editor：场景、脚本、资产、测试、构建
- 支持多 Unity 实例路由与按领域分组的工具组
- 提供远程托管服务器与鉴权选项

## 适用场景

- 用自然语言让 AI 在 Unity 中创建场景和 GameObject
- 让 AI 助手批量管理和整理项目资产
- 让 AI 编辑 C# 脚本并运行测试
- 自动化游戏开发中的构建与分析流程

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8:  Create your Unity apps with LLMs. MCP for Unity bridges AI assistants — Claude, Codex, VS Code, local LLMs, and mor
> L24: Control the Unity Editor in natural language from any MCP client — create scenes & GameObjects, edit C# scripts, ma
> L30: **Requirements:** Unity **2021.3 LTS → 6.x** · Python **3.10+** (via `uv`). Works with **any MCP client** — Claude 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `f4a60671d52b` · [字段定义](../../DATASET.md)*
