# zachmueller/notor

⭐ 13 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/zachmueller/notor) · 个人维护

**Obsidian 内的透明 AI 笔记助手插件，读写笔记并可控审批**

面向 Obsidian 用户的桌面端 AI 助手插件：提供侧边栏聊天、附件与上下文注入、自动压缩长对话、38 个内置工具读写/搜索/移动笔记与管理 frontmatter，写入操作默认需审批并通过检查点回滚。支持多 LLM 提供商（Ollama、LM Studio、Anthropic、OpenAI、AWS Bedrock），无遥测。扩展性上支持 MCP 工具服务器、Markdown 编写的工作流与用户自定义扩展，Circuits 功能默认关闭。macOS 提供语音模式。需 Obsidian 1.11.4+ 桌面版与运行中的 LLM 提供商，经 BRAT 或源码编译安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 38 个内置工具读写/搜索/移动笔记、管理 frontmatter 与标签
- 写入操作默认需审批，diff 逐块接受/拒绝，检查点可回滚
- 多 LLM 提供商：本地 OpenAI 兼容端点（Ollama、LM Studio）、Anthropic、OpenAI、AWS Bedrock
- MCP 工具服务器与 Markdown 编写的自定义扩展、工作流、Circuits 流水线

## 适用场景

- 在 Obsidian 内通过 AI 对话读取、创建与精确编辑笔记
- 用本地 LLM 私有化处理个人知识库
- 通过工作流、Hooks 与 MCP 服务器扩展笔记自动化

## 场景标签

`AI 助手` `知识库管理` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **A transparent, extensible AI assistant for note-taking and knowledge management in Obsidian.**
> L5: Notor gives you a full AI chat panel inside Obsidian with the ability to read, search, create, and surgically edit n
> L11: - **Side-panel AI chat** with streaming responses, conversation history, model presets for quick switching between 

## 星数曲线

```mermaid
xychart-beta
    title "zachmueller/notor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a7e3ce88985f` · [字段定义](../../DATASET.md)*
