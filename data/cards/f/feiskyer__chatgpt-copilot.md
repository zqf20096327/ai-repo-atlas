# feiskyer/chatgpt-copilot

⭐ 163 · TypeScript · ISC · 推送 2026-06-20 · [GitHub](https://github.com/feiskyer/chatgpt-copilot) · [官网](https://marketplace.visualstudio.com/items?itemName=feiskyer.chatgpt-copilot) · 个人维护

**VS Code 中的多模型 ChatGPT 对话与代码辅助扩展**

面向 VS Code 用户的聊天扩展：侧边栏对话窗口中以流式方式获取模型回答，支持 GPT-5、Claude、Gemini、Ollama、GitHub Copilot、DeepSeek 等多种 API key 提供商与 OAuth 订阅登录（Google/Anthropic/OpenAI），并可接入 OpenAI 兼容的本地模型。功能包括多文件/图片上下文（@）、提示词管理（#）、MCP 工具接入、非原生工具调用模型的 prompt 解析式工具调用，以及生成代码、加测试、找问题、解释等右键命令与快捷键。不收集遥测数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 OpenAI/Anthropic/Google/Azure/Ollama/DeepSeek 等多家提供商与 OpenAI 兼容 API
- Gemini/Claude/ChatGPT OAuth 订阅登录，无需 API key
- MCP 接入自定义工具，支持 prompt 解析式工具调用
- 代码上下文命令：生成代码、加测试、找问题、优化、解释、加注释等

## 适用场景

- 在编辑器内与多种 LLM 对话并让模型修改选中的代码
- 用自己的 API key 或 ChatGPT/Claude/Gemini 订阅获得回答
- 通过 Ollama 在本地运行模型并接入编辑器

## 场景标签

`AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L19: - 🤖 Supports GPT-5, o1/o3, Claude, Gemini, Ollama, Claude Code, Github Copilot and other OpenAI-compatible local mo
> L45: ## Supported Models & Providers
> L289: To use OpenAI compatible APIs, you need to set a custom model name: set model to `"custom"` and then specify your 

## 星数曲线

```mermaid
xychart-beta
    title "feiskyer/chatgpt-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-24 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `31c8fa859d1e` · [字段定义](../../DATASET.md)*
