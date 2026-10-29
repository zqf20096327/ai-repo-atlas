# PiscesGameDev/UniAI

⭐ 31 · C# · Apache-2.0 · 推送 2026-05-06 · [GitHub](https://github.com/PiscesGameDev/UniAI) · 组织维护 · 中文 README

**Unity 的 AI 交互框架：统一 Chat/Agent/Tool/MCP 与多模态能力**

面向 Unity 开发者的 AI 交互框架，既可做 Editor 助手也可嵌入游戏 Runtime。内置 Claude Messages API 与 OpenAI Chat Completions 兼容协议，支持 DeepSeek、Gemini、Qwen、Grok 等服务；通过模型元数据 + adapter/dialect 机制处理模型差异。提供 Agent 多轮 tool loop、MCP Client（Stdio/Streamable HTTP）、上下文窗口管理（token 预估/滑动窗口/摘要压缩）、图片生成与 SSE 流式输出。要求 Unity 2022.3+ 并依赖 UniTask。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Claude 与 OpenAI 兼容双协议，模型差异由 adapter/dialect 处理
- `[UniAITool]` 反射注册工具，AIAgentRunner 支持多轮 tool loop 与 reasoning 回放
- MCP Client 支持 Stdio 与 Streamable HTTP，动态合并 Tools 与 Resources
- ContextPipeline 提供 token 预估、滑动窗口、AI 摘要压缩与外部上下文注入

## 适用场景

- 在 Unity Editor 中搭建带工具调用的 AI Chat 助手
- 游戏 Runtime 内集成多模型对话、多模态输入与图片生成
- 通过 MCP 接入本地或远程工具服务扩展 Agent 能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: UniAI 是面向 Unity 的 AI 交互框架，提供统一的 Chat、Agent、Tool、MCP、多模态、生成式资产和上下文窗口能力。框架既可用于 Unity Editor 助手，也可嵌入游戏 Runtime。
> L10: - **多协议 Provider**: 内置 Claude Messages API 与 OpenAI Chat Completions 兼容协议，支持 DeepSeek、Gemini、Qwen、Grok 等 OpenAI-com

## 星数曲线

```mermaid
xychart-beta
    title "PiscesGameDev/UniAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c915c2aa4cd9` · [字段定义](../../DATASET.md)*
