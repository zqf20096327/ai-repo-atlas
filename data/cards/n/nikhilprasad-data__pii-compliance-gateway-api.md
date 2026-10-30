# nikhilprasad-data/pii-compliance-gateway-api

⭐ 15 · Python · 推送 2026-09-19 · [GitHub](https://github.com/nikhilprasad-data/pii-compliance-gateway-api) · [官网](https://pii-compliance-gateway-client.vercel.app/) · 个人维护

**检测并脱敏 PII 的 FastAPI 网关，供后端在数据入库前拦截敏感信息**

基于 FastAPI 的中间件网关：接收文本后经 LangGraph 工作流调用 LLM 识别姓名、邮箱、电话、信用卡号等 PII 实体，由 Python 执行确定性字符串替换脱敏，原始输入不落盘。配套 Redis 缓存（SHA-256 键、24 小时过期）与 Lua 原子限流（50 次/IP/分钟）、PostgreSQL 审计日志（仅存脱敏文本）、Pydantic 校验，提供 Next.js 仪表盘与线上演示。README 自述非认证合规系统，缺认证授权与保留策略。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 识别 + Python 确定性替换的脱敏分工设计
- Redis 缓存与 Lua 原子限流（50 请求/IP/60 秒）
- 审计日志仅存脱敏文本，原始输入不落库
- 本地 Docker Compose 一键起 Postgres/Redis，生产部署于 Render/Vercel/Neon/Upstash

## 适用场景

- 在后端入库前拦截并脱敏表单、工单、聊天中的敏感信息
- 为 API 流量加一层 PII 扫描与限流网关
- 保留脱敏后的审计记录用于调试与追溯

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A FastAPI middleware gateway that detects and sanitizes PII before it hits anything downstream. Send it text, it tel
> L37: - LangGraph-driven PII detection with structured LLM output
> L111: 7. LLM identifies PII entities (structured output)

## 星数曲线

```mermaid
xychart-beta
    title "nikhilprasad-data/pii-compliance-gateway-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9f0c60cb514e` · [字段定义](../../DATASET.md)*
