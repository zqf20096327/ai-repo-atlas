# Stellenbosch-Technologies/rhebok

⭐ 4 · Rust · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/Stellenbosch-Technologies/rhebok) · [官网](https://stelltec.com/rhebok/) · 组织维护

**为 AI 编码 agent 提供本地检索与记忆的 MCP server**

以 Rust 编写的 MCP server，对用户本地知识库（笔记、论文、网页剪藏、历史 agent 会话记录）做语义检索，并在编码 agent 每次提问时自动注入置信度门控筛选后的相关片段；同时提供 rhebok_search MCP 工具供 agent 按需检索，并将完成的会话蒸馏为跨会话的记忆条目。检索融合向量、关键词与链接图三种结果，附本地 web dashboard 用于搜索与配置。嵌入模型经 Ollama 在本地运行，无遥测；支持加密备份到自有 S3 或 Google Drive。平台限 macOS（Apple silicon）与 Linux/WSL，Intel Mac 无发布版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量、关键词、链接图三路检索融合，注入前经置信度门控
- 索引 Claude Code 与 Codex 历史会话记录并蒸馏为 episode 记忆
- 嵌入经 Ollama 本地运行，无遥测、无云端 API
- 一个索引同时服务 Claude Code、Codex、Gemini CLI、Cursor 与 Claude Desktop

## 适用场景

- 让编码 agent 自动引用我的笔记和历史会话里的结论
- 在本地搭建不外传数据的 agent 知识库
- 跨多个 AI 编码工具复用同一份检索索引与记忆

## 场景标签

`RAG` `语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: MCP server
> L22: rhebok indexes the folders you point it at, embeds them with a small model
> L31: It works with Claude Code, Codex, Gemini CLI, Cursor and Claude Desktop. It


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9e0882abaa8d` · [字段定义](../../DATASET.md)*
