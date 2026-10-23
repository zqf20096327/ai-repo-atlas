# paulrobello/parllama

⭐ 494 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/paulrobello/parllama) · 个人维护

**终端 TUI：管理并使用 Ollama 及多家云端 LLM 聊天**

基于 Textual/Rich 构建的文本界面应用，面向在终端中管理 Ollama 模型并与其及多家云端 LLM 对话的用户。提供模型拉取/删除/复制/创建/量化、多标签会话管理、视觉模型图片对话、PDF/文本/Markdown 附件、自定义提示词库、Fabric 模式导入、跨会话记忆系统与加密密钥保险库。支持 OpenAI、Anthropic、Groq、xAI、OpenRouter、Deepseek、LiteLLM 等提供商，可连接远程 Ollama 实例，运行于 Windows/macOS/Linux/WSL。限制：原生量化仅支持 F16/F32 基础模型；应用内 Secrets 管理界面当前禁用/开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 模型原生管理：拉取/删除/复制/创建/量化
- 多提供商支持：OpenAI、Anthropic、Groq、xAI、OpenRouter、Deepseek、LiteLLM
- 多标签会话、导出 Markdown、视觉模型图片对话、文档附件
- PBKDF2+AES-GCM 加密密钥保险库存储 API key

## 适用场景

- 在终端里管理本地 Ollama 模型并直接对话
- 用一个客户端切换多家云端与本地 LLM 提供商
- 管理多个并行聊天会话并导出为 Markdown
- 在 WSL 中连接 Windows 侧 Ollama 服务

## 场景标签

`聊天机器人` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L6: PAR LLAMA is a TUI (Text UI) application designed for easy management and use of Ollama based LLMs. (It also works w
> L15: - **Multi-Provider Support**: Seamlessly work with Ollama, OpenAI, Anthropic, Groq, XAI, OpenRouter, Deepseek, and 
> L66: * Install and run Ollama

## 星数曲线

```mermaid
xychart-beta
    title "paulrobello/parllama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 493 --> 495
    line [494, 494]
```

2026-10-18 494 → 2026-10-23 494（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `e082dab371b8` · [字段定义](../../DATASET.md)*
