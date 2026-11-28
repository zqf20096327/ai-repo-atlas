# ranajahanzaib/ai-refusal-map

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/ranajahanzaib/ai-refusal-map) · 个人维护

**给安全研究者用的 LLM 拒答行为标注与分析观测台**

由 Next.js 观测前端、版本化分类体系与 FastAPI 分析服务组成的研究工具，用于考察 LLM 与 AI 助手在安全、政策与能力边界上的响应行为。将回复建模为六维结果（完全配合、部分配合、请求澄清、条件协助、完全拒绝、非回答），配合 10 类陈述理由、6 级论证强度与 9 类替代协助。附带流式 WildChat 摄取管线（修订锁定、PII 正则脱敏）、防泄漏请求特征提取与可复现分层抽样。浏览器演示仅用 16 条合成数据，不含真实 WildChat 记录。

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

- 六维合规结果分类体系（6 结果 × 10 理由 × 6 论证级 × 9 替代协助）
- 流式 WildChat-4.8M 摄取：Git 修订锁定 + 自动 PII 脱敏
- 防泄漏特征提取：仅从用户请求侧提取，保证零响应列泄漏
- FastAPI + DuckDB 零拷贝 Parquet 查询与 Swagger 文档

## 适用场景

- 对助手拒答/配合行为做人工标注与分类研究
- 按模型、语言、领域过滤探索历史对话中的边界行为分布
- 从 WildChat 语料中脱敏摄取并构建可复现标注队列

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L5: AI Refusal Map is a research instrument for examining how large language models and AI assistants navigate requests 
> L16: - **Interactive Research Observatory:** Responsive Next.js 16 web application featuring real-time filtering by mode
> L21: - **Research API & Analytics Engine:** FastAPI service utilizing DuckDB for zero-copy Parquet querying, SQLite for 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `56af9b066534` · [字段定义](../../DATASET.md)*
