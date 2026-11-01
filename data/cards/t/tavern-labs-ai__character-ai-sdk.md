# tavern-labs-ai/character-ai-sdk

⭐ 166 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/tavern-labs-ai/character-ai-sdk) · [官网](https://www.npmjs.com/package/character-ai-sdk) · 组织维护

**TypeScript SDK：构建有持久记忆与一致人设的 AI 角色应用**

面向开发者的 TypeScript 库，提供八张预制人设卡、跨对话的持久记忆运行时（抽取、溯源、合并、召回、生命周期管理）与关系状态演化，并内置 Amazon Bedrock 与 OpenAI 适配器，抽取、嵌入与生成三个端口可混用不同提供商。持久化支持内存、原子 JSON 与可选 SQLite，另有 SillyTavern 卡片/聊天导入与框架无关的 HTTP 服务适配层。要求 Node.js 20 及以上，需 OpenAI API key 或 AWS 凭证。

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

- 八张预制 persona 卡（atlas/sage 等）与人设清单映射
- 持久角色记忆运行时：抽取、溯源、合并、召回与生命周期
- Bedrock 与 OpenAI 官方适配器，三个端口可混用提供商
- SillyTavern 卡片/聊天导入与框架无关 HTTP service 适配层

## 适用场景

- 为客服、销售或研究助手应用快速接入有记忆的 AI 角色
- 在 Bedrock 与 OpenAI 之间混搭抽取、嵌入与生成模型
- 将 SillyTavern 角色卡迁移到自有 Node.js 服务中

## 场景标签

`Agent 记忆` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L29: `character-ai-sdk` is a TypeScript SDK for applications where an AI character should remain
> L36: |Memory|Extraction, provenance, consolidation, visibility, recall, and lifecycle|✓|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ef31f4eca3bc` · [字段定义](../../DATASET.md)*
