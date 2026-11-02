# tavern-labs-ai/persona-ai-sdk

⭐ 192 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/tavern-labs-ai/persona-ai-sdk) · [官网](https://www.npmjs.com/package/persona-ai-sdk) · 组织维护

**给应用开发者的角色 AI SDK：人设卡+持久角色记忆+模型适配器**

TypeScript SDK，用于构建保持人设一致并跨对话记忆的 AI 角色应用。单包内含八张预制 persona 卡、记忆运行时（抽取、溯源、巩固、召回、生命周期管理）以及 Amazon Bedrock 与 OpenAI Responses API 适配器。单次调用完成记忆召回、提示编译、回复生成、对话摄取与关系状态演进。存储支持内存、原子 JSON 文件、SQLite（better-sqlite3，可选原生依赖），并可自定义 MemoryStore 对接 PostgreSQL/DynamoDB。兼容 SillyTavern 卡片导入。需 Node.js 20+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八张预制 persona 卡（prompts/traits/greetings/memorySeeds）
- 记忆运行时：抽取、溯源、巩固、可见性、召回与生命周期
- Bedrock Converse/Titan V2 与 OpenAI Responses/Embeddings 双适配器，可混用
- 内存/原子 JSON/SQLite 三种存储，兼容 SillyTavern 卡片与聊天导入

## 适用场景

- 为应用构建有持久记忆的 AI 角色或陪伴型助手
- 在 Bedrock 与 OpenAI 之间切换或混用模型能力
- 导入 SillyTavern 角色卡到自有应用

## 场景标签

 · 领域:LLM 应用开发/角色记忆

## 证据(README 行号)

> L29: `persona-ai-sdk` is a TypeScript SDK for applications where an AI character should remain
> L189: Extraction, embeddings, and generation are independent ports. An application can use Bedrock for
> L216: |`persona-ai-sdk/bedrock`|Bedrock Converse extraction, Titan V2 embeddings, character models|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `676e08ec6791` · [字段定义](../../DATASET.md)*
