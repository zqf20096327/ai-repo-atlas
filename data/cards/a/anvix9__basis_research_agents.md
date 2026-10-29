# anvix9/basis_research_agents

⭐ 64 · Python · MIT · 推送 2026-05-06 · [GitHub](https://github.com/anvix9/basis_research_agents) · 个人维护

**本地运行的多 agent 深度学术研究管线，产出可溯源论证树**

SEEKER 是一个由 10 个 agent 组成的研究管线：从研究问题出发，经概念映射、问题分解、跨 10+ 学术数据源（OpenAlex、Semantic Scholar、arXiv 等）检索，构建持久化论证树，其中每条声明附可验证证据；设三次人工介入中断点由用户确认方向，最终产出 Understanding Map 与研究简报。面向跨学科研究者，明确声明不代写论文、只绘制知识版图。支持 Anthropic API 或本地 Ollama 作为模型后端（小模型输出质量下降、JSON 解析失败更频繁），仅需 4 个依赖，MIT 许可，自标 BETA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 10-agent 流水线构建持久化论证树，声明逐条溯源到论文/法律文书等证据
- 三次 human-in-the-loop 中断点由用户决定研究方向
- 10+ 免 key 学术数据源（OpenAlex/Semantic Scholar/arXiv/PubMed 等）
- Ollama 本地模型可作无 API key 后端，含降级解析与容错

## 适用场景

- 跨学科学者探索一个研究问题的知识版图与证据脉络
- 在关键节点亲自介入决定研究的走向与产出形式
- 无云 API 条件下用本地模型跑完整研究管线

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L12: **SEEKER** is a 10-agent research pipeline that conducts deep, traceable academic research by orchestrating special
> L25: **Three human-in-the-loop breaks** where you read, learn, and decide the trajectory. The pipeline stops and waits f
> L78: 7. Produce an Understanding Map, research brief, and whatever else you requested

## 星数曲线

```mermaid
xychart-beta
    title "anvix9/basis_research_agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-29 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a33ad5fe7a62` · [字段定义](../../DATASET.md)*
