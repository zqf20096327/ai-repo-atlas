# Echo-Smith/LuminWrite-OSS

⭐ 16 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Echo-Smith/LuminWrite-OSS) · [官网](https://app.luminwrite.com) · 个人维护 · 中文 README

**面向中文内容创作者的自托管 AI 写作工作台**

自托管的中文 AI 写作平台：素材检索 → 提纲确认 → 风格化成稿 → 写后自检 → 记忆沉淀的流程化写作，关键节点由创作者确认。基于 Go + React + PostgreSQL（pgvector + ParadeDB BM25）实现单库 RAG，模型走 OpenAI 兼容协议并支持 BYOK 个人密钥。提供分层长期记忆、质量门版本化交付、编辑部多 Agent 协作、WABench 评测流水线。OSS 版付费搜索 Provider 仅以 stub 形式公开；AR-012 的 sidecar 为私有组件不随仓库分发。Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 素材检索→提纲确认→成稿→自检→记忆沉淀的流程化写作
- PostgreSQL 单库内 BM25 + pgvector + RRF + GraphRAG，零外部向量库
- 三层长期记忆 + 注入遥测，记忆注入效果可查询
- BYOK：用户自带 API 密钥，加密存储、连通测试、实例默认回退

## 适用场景

- 中文长文创作、多材料综合、忠实改写、深度研究四类写作流程
- 自托管知识库并沉淀个人写作偏好与反馈
- 通过订阅/选题/知识库管理素材并用 AI 完成调研成稿

## 场景标签

`AI 写作` `RAG` `Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: **把写作拆成可观察、可干预、可迭代的工程流程** —— 面向中文内容创作的
> L11: 自托管 AI 写作工作台。不追求「一键生成」的魔法：素材检索 → 提纲确认 →
> L122: - **四大核心写作流程**：长文创作 / 多材料综合 / 忠实改写 / 深度研究——写作入口的

## 星数曲线

```mermaid
xychart-beta
    title "Echo-Smith/LuminWrite-OSS 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 17
    line [14, 15, 16, 16]
```

2026-10-18 14 → 2026-10-31 16（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `22dcfe611880` · [字段定义](../../DATASET.md)*
