# xCodeWraith/GoogleMapAIagent

⭐ 382 · 推送 2025-12-28 · [GitHub](https://github.com/xCodeWraith/GoogleMapAIagent) · 个人维护

**对话式 AI 代理：从 Google Maps 抓取并整理 B2B 销售线索**

基于 n8n 工作流的对话式系统，由两个需分别导入并互相链接的 JSON 工作流组成：主工作流提供聊天界面，由 GPT-4o 解析自然语言请求并调用 Serper.dev 的 Google Maps API 抓取商家数据；子工作流负责生成 UUID 并写入 Google Sheets。同时通过 Perplexity AI 查找企业邮箱并做背景研究，实现数据富化。需自备 n8n（自托管或付费）、OpenAI、Serper.dev、Perplexity API 密钥及 Google 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言下发抓取请求，支持多轮对话
- 两阶段工作流：地图数据采集 + 邮箱与背景信息富化
- 结果结构化写入 Google Sheets（UUID/地址/评分/营业时间等字段）
- 通过 n8n 导入两个 JSON 工作流文件部署

## 适用场景

- 按城市和行业生成销售线索名单
- 为冷呼叫收集商家电话与地址
- 为邮件营销补全企业联系邮箱

## 场景标签

 · 领域:销售/营销自动化

## 证据(README 行号)

> L10: > **A conversational AI agent that extracts, enriches, and organizes business leads from Google Maps using natural 
> L84: |**Automation**|n8n|Workflow orchestration|
> L85: |**AI Agent**|OpenAI GPT-4o|Natural language understanding & task execution|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `c0a06b0eb649` · [字段定义](../../DATASET.md)*
