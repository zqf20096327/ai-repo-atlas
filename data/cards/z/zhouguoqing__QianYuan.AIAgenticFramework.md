# zhouguoqing/QianYuan.AIAgenticFramework

⭐ 37 · C# · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/zhouguoqing/QianYuan.AIAgenticFramework) · 个人维护 · 中文 README

**C# .NET 的 ReAct Agentic 框架，含 Skill 体系与 MCP 支持**

用 C# 13 / .NET 10 实现的 Agentic 框架：ReAct 循环（Thought-Action-Observation）配合 Loop Engineering 治理（上下文压缩、工具调用预算、重复调用拦截）；抽象 ISkill 体系支持渐进式加载，来源含代码 Skill、Markdown SKILL.md 目录与外部 MCP Server；模型 Provider 覆盖 OpenAI 兼容协议、Azure OpenAI、Anthropic、Gemini、DashScope 等。附带流式 WebAPI（SSE/SignalR）、React 19 WebUI、Electron 桌面壳与钉钉机器人集成。运行依赖 .NET 10 SDK 与 Node.js（>=18）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 循环 + Loop Engineering：上下文压缩、工具调用总预算、重复调用拦截
- 三类 Skill 来源统一注册：代码 ISkill / Markdown SKILL.md / MCP Server 工具
- MCP 双向支持：作为 Client (stdio) 挂载外部工具，也作为 Server 通过 HTTP/SSE 暴露本地 Skill
- 多 Provider 支持：OpenAI 兼容（DeepSeek/OpenRouter/Qwen 等）、Azure OpenAI、Anthropic、Gemini

## 适用场景

- 用 .NET 技术栈构建多轮工具调用的智能体应用
- 挂载现有 Claude/Cursor 生态的 SKILL.md 技能目录复用提示资产
- 通过 Agent Store 可视化创建和编排企业智能体
- 把本地 Skill 通过 MCP 协议提供给 Claude Desktop 等外部客户端

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: 一个用 C# .NET 10 写的 Agentic 框架，参考 ReAct 范式，支持渐进式技能 (Skill) 加载、
> L11: |Agent 模式|ReAct (Thought-Action-Observation) 循环；Loop Engineering；Agent-as-Tool 嵌套调用|
> L14: |模型 Provider|OpenAI 兼容 (GPT/Kimi/MiniMax/Qwen-compat/DeepSeek/OpenRouter/NEWAPI)、Azure OpenAI、Anthropic Claude、Goog

## 星数曲线

```mermaid
xychart-beta
    title "zhouguoqing/QianYuan.AIAgenticFramework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0f0da12d7d60` · [字段定义](../../DATASET.md)*
