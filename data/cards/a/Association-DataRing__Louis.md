# Association-DataRing/Louis

⭐ 26 · TypeScript · AGPL-3.0 · 推送 2026-08-11 · [GitHub](https://github.com/Association-DataRing/Louis) · [官网](https://louis.data-ring.net) · 组织维护 · 中文 README

**面向法律职业的自托管开源 AI 编排平台（BYOK）**

由法国 Association DataRing 开发的法律行业 AI 应用原型（AGPL-3.0，Alpha，v0.2）：自托管 Web 应用，多 agent 编排（Maestro/Recherche/Légifrance/Rédacteur/Relecteur/Citateur，可按角色分配模型），支持 BYOK 接入 Mistral、Anthropic、OpenAI、OpenRouter、Albert/Etalab 及 Ollama/vLLM 自托管模型。内置 pgvector RAG、PDF→Markdown 转换、可插拔 OCR、文档信封加密（XChaCha20+AES-256-GCM）、DOCX 生成与编辑、N×M 尽调表格分析。项目自述为无商业承诺的探索性原型，mono-cabinet 单租户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent 编排（6 个专业 agent + Board，4 个预设配置，每回答附 agent 审计日志）
- BYOK 聚合多家 FR/EU/US 模型供应商及 Ollama/vLLM 自托管模型
- RAG pgvector + markdown-aware 分块 + 可点击引用（高亮定位）
- 文档信封加密（DEK XChaCha20 + master key AES-256-GCM），可插拔 OCR 链
- DOCX 生成/编辑与 N×M 尽调表格分析

## 适用场景

- 律所自托管 AI 助手处理客户案卷，数据不出自有基础设施
- 用法语对 Légifrance/Pappers 及自有文档做带引用的法律问答
- 批量导入合同做尽调表格提取，生成与修订法律文书

## 场景标签

`多智能体` `文档问答` `文档解析` · 领域:Agent 开发

## 证据(README 行号)

> L196: **orchestrateur** : une architecture où plusieurs agents IA — chacun
> L220: Posez une question en français à n'importe lequel des grands modèles
> L243: Demandez « rédige une mise en demeure pour... » : Louis appelle

## 星数曲线

```mermaid
xychart-beta
    title "Association-DataRing/Louis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1c61b7ff8734` · [字段定义](../../DATASET.md)*
