# mnemosyne-oss/mnemosyne

⭐ 3,694 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/mnemosyne-oss/mnemosyne) · [官网](https://mnemosyne.site) · 组织维护

**给 AI Agent 提供零云端本地记忆层的 SQLite 记忆库**

Mnemosyne 是一个通用记忆层（Hermes-first），通过 pip 安装并以单个 SQLite 数据库存储，无需外部服务。核心架构 BEAM 包含三层：工作记忆（调用 LLM 前自动注入、TTL 驱逐）、情景记忆（sqlite-vec + FTS5 混合检索）和 TripleStore 时序知识图谱。混合评分由 50% 向量相似度、30% FTS5 关键词、20% 重要度构成；嵌入经二值化压缩为 48 字节，全部检索在 SQLite 内完成。通过 MCP 服务器（stdio/SSE）、Python SDK、桥接文件等方式接入 Cursor、Claude Code、Codex、Windsurf、OpenWebUI 等 8+ 平台；支持可选双向同步与客户端加密，默认不向 OpenRouter 之外发送数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BEAM 三层记忆：工作记忆自动注入、情景记忆混合检索、时序知识图谱
- 内置 MCP 服务器（stdio/SSE），覆盖 8+ agent 平台接入方式
- 嵌入二值化（384 维 → 48 字节），无外部向量数据库，检索全在 SQLite 内
- 可选端到端同步，支持客户端加密（Fernet / PyNaCl）

## 适用场景

- 给自建 agent 加长期记忆而不引入云服务
- 在 Cursor/Claude Code 等 MCP 客户端中保留用户偏好与历史事实
- 本地优先、需控制数据不出机的记忆存储

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Mnemosyne** is a universal, Hermes-first memory layer that works with any agent framework (Claude Code, Cursor, C
> L164: **BEAM** (Bilevel Episodic-Associative Memory):
> L179: |**MCP server**|✅ Built-in|❌|❌|❌|✅|✅|❌|

## 星数曲线

```mermaid
xychart-beta
    title "mnemosyne-oss/mnemosyne 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 3459 --> 3712
    line [3480, 3496, 3503, 3513, 3516, 3523, 3524, 3535, 3547, 3554, 3563, 3568, 3513, 3608, 3617, 3625, 3632, 3638, 3643, 3653, 3662, 3666, 3673, 3678, 3684, 3688, 3691, 3691]
```

2026-10-22 3,480 → 2026-11-24 3,691（+211）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `d3ebceffed68` · [字段定义](../../DATASET.md)*
