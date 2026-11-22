# YeStarOne/feiyuos-memory-graph

⭐ 3 · JavaScript · MIT · 推送 2026-11-07 · [GitHub](https://github.com/YeStarOne/feiyuos-memory-graph) · 个人维护 · 中文 README

**给 DSH QQ 机器人加会遗忘的长期记忆图谱插件**

面向 DSH（DeepSeek Harness）QQ 机器人框架的记忆插件：后台将对话经四阶段 LLM 抽取为事件/实体/概念的知识图谱，回复时用向量召回加图遍历（沿边走 4 跳）混合检索，按相似度、重要度、新近度加权取 top 5 注入提示词；记忆带 30 天半衰期衰减与钉住机制，每聊天独立分库，数据为 JSONL 纯文本。零 npm 依赖，纯 Node ≥18 运行，经 git clone 加安装器补丁部署，依赖已装好的 dsh-onebot-qq。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段 LLM 抽取：事实→概念→实体关系→时序/因果（后两步可选）
- 向量+图混合检索，恒定 top 5 注入，30 天半衰期自动遗忘
- QQ 内管理指令直接应答，不消耗模型回合
- 零依赖纯本地，JSONL 存储，附力导向图谱可视化面板

## 适用场景

- 给 QQ 机器人补上跨会话的长期记忆
- 避免把全部聊天记录塞进提示词导致上下文膨胀
- 角色扮演场景下防止虚构内容污染真实记忆

## 场景标签

`Agent 记忆` `知识图谱` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L7: 给 DSH（DeepSeek Harness）QQ 机器人装上一套**会遗忘的长期记忆图谱**：
> L67: - 🪶 **零依赖**：纯 Node ≥18，没有原生模块、没有数据库；LLM/向量走任意 OpenAI 兼容端点（SiliconFlow 免费档 bge-m3、本地 Ollama 都行）

## 星数曲线

```mermaid
xychart-beta
    title "YeStarOne/feiyuos-memory-graph 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `97f3c9a8e1b5` · [字段定义](../../DATASET.md)*
