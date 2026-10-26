# jduncan-rva/gemini-agent-creator

⭐ 39 · MIT · 推送 2025-11-21 · [GitHub](https://github.com/jduncan-rva/gemini-agent-creator) · 个人维护

**通过对话创建 Gemini CLI 自定义 agent 的扩展**

Gemini CLI 扩展，提供 /new-agent 命令，以 AI 辅助对话替代手写 TOML 来生成自定义 agent 定义。支持两种模式：Quick 模式根据一句描述自动生成含默认工具与系统提示词的完整 TOML 配置并经确认后保存；Interactive 模式分步引导定义行为、工具、输入参数。生成的 agent 可使用 8 种只读工具（read/grep/glob/web_search 等），保存到 ~/.gemini/agents/。要求 Gemini CLI 具备 user-defined agents 功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /new-agent 命令通过对话生成 agent 的 TOML 配置
- Quick 与 Interactive 两种生成模式，保存前需用户确认
- 生成的 agent 可使用 8 种只读工具（含 web_search、memory）
- 内置常见 agent 模式（代码审查、文档生成、测试编写等）

## 适用场景

- 不会写 TOML 的用户通过描述快速创建 Gemini CLI agent
- 为代码审查、文档生成等常见任务快速生成 agent 配置

## 场景标签

 · 领域:开发者工具/CLI 扩展

## 证据(README 行号)

> L7: This extension provides the `/new-agent` command that guides you through creating custom agent definitions using AI-
> L145: - Gemini CLI with user-defined agents support

## 星数曲线

```mermaid
xychart-beta
    title "jduncan-rva/gemini-agent-creator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e802441c47b0` · [字段定义](../../DATASET.md)*
