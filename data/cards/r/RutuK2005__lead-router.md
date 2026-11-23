# RutuK2005/lead-router

⭐ 3 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/RutuK2005/lead-router) · 个人维护

**线索分发前的清洗去重与 LLM 打分服务**

FastAPI webhook 服务：接收 Meta 广告线索、网站表单或任意扁平 JSON webhook，经 HMAC-SHA256 签名与时间戳校验后，做电话 E.164 清洗、邮箱校验、24 小时窗口去重，再以 hot/warm/cold/spam 打分并写入 SQLite outbox，由内置 worker 每 2 秒投递到 CRM 或 n8n，带指数退避重试与 Idempotency-Key。LLM 打分需 ANTHROPIC_API_KEY，缺省回退到关键词评分器。作者称面向 n8n 诊所线索自动化场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HMAC-SHA256 签名校验与 5 分钟时间窗防重放
- LLM 结构化输出打分，API 失败时回退关键词评分器
- outbox 模式投递：指数退避重试、幂等键、死信与手动重投
- docker compose --profile n8n 可同时启动配套 n8n 工作流

## 适用场景

- 把 Meta 广告和网站表单线索清洗打分后转进 n8n 流程
- 诊所等场景防止重复表单提交与 CRM 宕机期间线索丢失
- 统一各种格式混乱的电话与姓名数据后再入库 CRM

## 场景标签

 · 领域:营销自动化/线索路由

## 证据(README 行号)

> L5: A small FastAPI service that receives leads from Meta lead ads, website forms or any flat JSON webhook, cleans them 
> L57: 5. The lead is scored as hot, warm, cold or spam, with a treatment category, a one-line summary and a suggested fol


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `e04a99825ca8` · [字段定义](../../DATASET.md)*
