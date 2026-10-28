# jnamaya/SAFi

⭐ 63 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/jnamaya/SAFi) · [官网](https://selfalignmentframework.com/) · 个人维护

**面向 AI agent 的开源治理引擎：实时执行策略并审计每次决策**

SAFi 是一个 Python 编写的 AI agent 治理引擎，供需要在运行时执行组织政策的机构使用。机制：将组织章程与政策编译为带权重的价值集（默认章程权重 40%），对每条回复逐值评估后在送达前批准/阻断/重定向；工具调用须经允许列表授权；每个治理回合生成草稿、评估账本、决策与政策版本的审计记录，写入哈希链审计轨迹，并附带 Audit Hub 分析与人工监督队列。模型无关，支持多家 LLM 提供商 API key。本地运行需 Docker、Python 3 与约 8GB 磁盘，内置 MySQL；也提供 GHCR 预构建镜像与裸机 systemd 部署文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 政策编译为带权重的价值集，回复送达前逐值评估并批准/阻断/重定向
- 工具调用按 allow-list 授权，读写区别对待并记录
- 哈希链审计轨迹 + Audit Hub 分析 + 人工监督队列
- 模型无关：支持 Groq/Anthropic/Gemini/OpenAI/Mistral/DeepSeek/Cerebras/智谱等多家 API key

## 适用场景

- 机构在运行时强制执行自身 AI 政策并留存完整审计证据
- 治理 agent 的工具调用，阻断未授权操作
- 应对 SEC/FINRA/EU AI Act/HIPAA/GDPR 等合规审查（文档区分现有功能与规划）
- 通过 /evaluate 网关治理已有 agent 的输出而不重建技术栈

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: > SAFi is an open source governance engine for AI agents. It lets institutions enforce their policies in real time,
> L56: - **Evaluate an existing agent** — Use the /evaluate gateway to govern the output of an agent you have already buil
> L42: **Model Independence** — Your charter, policies, and audit trail live in your database, not the provider's. Switch 

## 星数曲线

```mermaid
xychart-beta
    title "jnamaya/SAFi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-28 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `de18b724498a` · [字段定义](../../DATASET.md)*
