# mashhq/mash

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/mashhq/mash) · [官网](https://getmash.io/) · 组织维护

**给编码 agent 用户聚合检索多工具聊天历史的本地搜索工具**

Mash 读取本机上 Claude Code、Codex、Copilot、Cursor、OpenCode、Antigravity 等编码 agent 已保存的聊天记录，基于嵌入建立索引，支持按词或精确短语跨 agent、跨机器检索，可跳转到原始消息上下文，并将决策连同出处引文保存为记忆供 agent 经 MCP 查询。默认索引与搜索留在本机、无需账号，不修改原始历史；提供桌面应用、CLI 安装脚本、Raycast 扩展与可选 Mashy 助手（自带模型服务与 API key）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨多个 agent 保存的聊天记录统一索引与搜索
- 经 MCP 让 agent 查找决策并引用原始消息
- 可选 Mash 服务器实现多机器共享索引，单机可离线搜索
- 嵌入推理支持 DirectML/Core ML/GPU 加速，可配置远程 worker

## 适用场景

- 找回某个决定是在哪个 agent 对话中做出的
- 换一个编码 agent 时延续之前的工作上下文
- 将整段对话导出为 Markdown/HTML/PDF 存档
- 在 Raycast 中边输入边检索历史聊天

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L16: decision, and pick up work in another agent. Mash is open source and self-hosted.
> L28: - **Pick up work in another agent.** Ask an agent connected over MCP to find
> L51: - **GPU acceleration for semantic search.** Optional embeddings use DirectML


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `80360a9e2dc1` · [字段定义](../../DATASET.md)*
