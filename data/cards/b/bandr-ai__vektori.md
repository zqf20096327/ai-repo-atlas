# bandr-ai/vektori

⭐ 138 · Python · Apache-2.0 · 推送 2026-06-18 · [GitHub](https://github.com/bandr-ai/vektori) · [官网](https://vektori.cloud) · 组织维护

**给 AI agent 的三层记忆库：事实/情节/原句一层图存储**

面向构建有记忆能力 agent 的 Python 库：以三层句图（事实 L0 / 情节 L1 / 原句 L2）组织对话记忆，检索命中事实层，经图遍历自动发现情节层模式，并可回溯原始句子；支持三档检索深度控制 token 开销。默认 SQLite 零配置，可切换 Postgres/Neo4j/Qdrant/Milvus；兼容 10 家模型提供方（含 OpenAI、Gemini、NVIDIA NIM、Ollama 本地运行）。README 附与 Mem0/Zep/Letta 等的长程记忆基准对比数据，并自述 66% 与 95% 检索命中间的合成差距仍在改进。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三层句图（Facts/Episodes/Sentences）结构与三档检索深度
- 默认 SQLite 零配置，可切换 Postgres/Neo4j/Qdrant/Milvus 后端
- 支持 10 家模型提供方，含 Ollama 全本地零 API key 示例
- 提供 CLI 与 Docker Compose 多后端启动

## 适用场景

- 给聊天或客服 agent 加长期用户记忆与偏好轨迹分析
- 跨会话追踪用户情绪与行为模式的变化
- 本地零配置起步、按需扩展到向量/图数据库后端

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L30: Vektori solves this with a **three-layer sentence graph**. Agents don't just recall preferences — they understand h
> L42: Search hits Facts, graph discovers Episodes, traces back to source Sentences. SQLite by default — swap to Postgres,
> L110: Three lines to wire memory into any agent loop:

## 星数曲线

```mermaid
xychart-beta
    title "bandr-ai/vektori 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 136 --> 139
    line [137, 138, 138]
```

2026-10-18 137 → 2026-10-31 138（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `74a62c8491ef` · [字段定义](../../DATASET.md)*
