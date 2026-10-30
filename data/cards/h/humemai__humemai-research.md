# humemai/humemai-research

⭐ 15 · Python · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/humemai/humemai-research) · [官网](https://humemai.github.io/humemai-research/) · 组织维护

**AI 类人记忆研究库：情景与语义记忆的图存储与推理**

HumemAI 的研究代码库，探索 AI 的人类式记忆机制：将对话与经验表示为时序属性图（情景记忆），把用户提供或外部数据（如 Wikidata、Wikipedia）整合进图、表与向量格式（语义记忆），并研究记忆管理（记忆/摘要/遗忘）与符号-神经混合记忆的图上查询推理；另涉及用强化学习诱导层级与探索知识结构。以 Python 库形式通过 pip 安装，支持 rdflib 与 JanusGraph 两种图后端导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 情景与语义双记忆模型，基于时序属性图
- 支持 rdflib 与 JanusGraph 两种图存储后端
- 整合 Wikidata/Wikipedia 等外部数据为图、表、向量格式
- 研究跨时间的记忆管理（记住/摘要/遗忘）

## 适用场景

- 构建带类人记忆结构的 AI agent 记忆层
- 研究情景与语义记忆的存储、检索与推理
- 探索知识图谱上的强化学习与层级归纳

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: HumemAI Research explores **human-like memory** for AI — combining **episodic** (experience-based) and **semantic** 
> L23: - **Episodic Memory:** Representing conversations and experiences as temporal property graphs.
> L24: - **Semantic Memory:** Integrating user-provided or external data (e.g. Wikidata, Wikipedia) into graph, table, and

## 星数曲线

```mermaid
xychart-beta
    title "humemai/humemai-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f4ee15c7a450` · [字段定义](../../DATASET.md)*
