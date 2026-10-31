# yaoshu-open/yaoshu-token

⭐ 14 · Java · Apache-2.0 · 推送 2026-07-13 · [GitHub](https://github.com/yaoshu-open/yaoshu-token) · [官网](https://yaoshu.cc) · 组织维护 · 中文 README

**聚合 40+ 上游 AI 服务商的 Java 版 AI API 网关与计费系统**

受 new-api 启发、以 Java 17 + SpringBoot 3.3 + Vue3 独立重构的 AI API 网关：将 40+ 上游 AI 服务商聚合到统一 API 之后，提供用户管理、Token 分组、配额与计费（含 EPay/Stripe/Creem 充值、缓存命中计费）、限流、渠道加权路由与失败重试、管理控制台。支持 OpenAI Responses/Realtime、Claude Messages、Gemini、Rerank 等格式及相互转换，另有 Midjourney、Suno、Dify 上游支持。部署需 MySQL ≥ 8.0.28 与 Redis，提供 Docker Compose 与源码构建两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 40+ 上游 AI 服务商到统一 API
- OpenAI/Claude/Gemini 格式互转与 Rerank 支持
- 组织级按请求/用量/缓存命中的计费与限流
- Docker Compose 一键部署，多语言界面（中/繁/英/法/日）

## 适用场景

- 团队自建统一 AI API 入口做密钥与配额管理
- 企业内部多模型用量统计与成本核算
- 为授权客户场景搭建带计费能力的 API 网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L31: Yaoshu Token (爻枢 Token) is inspired by new-api and independently rebuilt with Java + Vue3. It is an AI API gateway 
> L81: |📡 API Documentation|OpenAI-compatible API|

## 星数曲线

```mermaid
xychart-beta
    title "yaoshu-open/yaoshu-token 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7bac3a44917a` · [字段定义](../../DATASET.md)*
