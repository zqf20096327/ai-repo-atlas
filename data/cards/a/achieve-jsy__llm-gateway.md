# achieve-jsy/llm-gateway

⭐ 6 · Go · 推送 2026-11-04 · [GitHub](https://github.com/achieve-jsy/llm-gateway) · 个人维护 · 中文 README

**给开发团队的多厂商大模型统一接入网关**

可自托管的大模型统一接入层，由 Go 网关、控制面与 Vue3 管理台组成。客户端走单一 OpenAI 兼容接口，网关完成鉴权、限流、按模型组的 round_robin/priority/weighted 调度与 fallback，流式转发到 20+ 厂商上游。控制面基于 PostgreSQL 持久化渠道、Key、配额与调用日志，经 Redis 下发配置热更新，模型目录从 LiteLLM 同步。README 注明以现状开源，仅供学习参考，生产前需自行审计安全配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 /v1 入口，收敛 OpenAI/Claude/Bedrock/Gemini/通义/DeepSeek/vLLM 等上游
- 模型组调度：round_robin / priority / weighted 分流与 fallback
- Key 签发吊销、配额管理与按用户/部门/模型的用量看板
- Redis snapshot + pub/sub 实现配置热更新，无需重启

## 适用场景

- 多个团队共用一批模型 Key，需要统一入口和配额管理
- 业务代码不想绑定单一厂商，换上游不改代码
- 需要按部门统计模型调用成本与 token 用量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: 一套可自托管的多模型统一接入层：客户端只认一个 **OpenAI 兼容接口**，网关负责鉴权、限流、模型组调度、上游转发与流式回传；管理台负责渠道、模型、Key、模型组、配额与调用分析。
> L17: 1. **入口统一**：OpenAI / Claude / Bedrock / Gemini / 通义 / DeepSeek / 自建 vLLM 等上游收敛成一个 `/v1` 接口，换厂商不改业务代码。

## 星数曲线

```mermaid
xychart-beta
    title "achieve-jsy/llm-gateway 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-26"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-08 5 → 2026-11-26 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `bc1b2643aed2` · [字段定义](../../DATASET.md)*
