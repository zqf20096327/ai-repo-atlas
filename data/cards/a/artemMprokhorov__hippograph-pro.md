# artemMprokhorov/hippograph-pro

⭐ 25 · Python · NOASSERTION · 推送 2026-04-10 · [GitHub](https://github.com/artemMprokhorov/hippograph-pro) · 个人维护

**面向个人 AI agent 的自托管图式联想记忆系统**

HippoGraph Pro 是单用户、自托管的图结构联想记忆系统，为个人 AI 助手提供跨会话、跨模型版本的记忆连续性。核心机制：扩散激活检索（嵌入 HNSW + BM25 + 重排）、情绪加权与生物式记忆衰减、后台 Sleep-Time 计算（PageRank、去重、冲突检测、快照回滚）。实体抽取用 GLiNER（零样本）+ spaCy，全程无 LLM API 调用（零 LLM 成本），支持 50+ 语言（中文用 jieba 分词）。通过 MCP 与 Claude/Gemini 等 agent 接入；README 声明不适用于企业 RAG、多租户或合规场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 扩散激活 + 情绪加权 + 时间衰减的联想记忆图
- 零 LLM 推理成本：GLiNER + sentence-transformers 全本地运行
- Sleep-Time 后台计算：轻/深睡眠周期的 PageRank、去重、冲突检测与快照
- 50+ 语言支持，中文经 jieba 分词处理

## 适用场景

- 让个人 AI 助手跨会话、跨模型版本记住我的偏好与历史
- 为 agent 维持长期一致的身份与关系上下文
- 将技能以带情绪权重的经验形式沉淀进记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **HippoGraph Pro** is a self-hosted, graph-based associative memory system for personal AI agents — built to give A
> L15: **Core thesis:** `model = substrate, personality = memory`. An AI agent's identity can persist across model version

## 星数曲线

```mermaid
xychart-beta
    title "artemMprokhorov/hippograph-pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bbe4ebb99d3d` · [字段定义](../../DATASET.md)*
