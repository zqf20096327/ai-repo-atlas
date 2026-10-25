# doublewordai/control-layer

⭐ 96 · Rust · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/doublewordai/control-layer) · [官网](https://doublewordai.github.io/control-layer/) · 组织维护

**AI 模型网关：统一路由、鉴权与管理多端点模型访问**

Doubleword 维护的开源 AI 模型网关（dwctl），为跨模型提供商（开源与专有、自托管或托管）的推理流量提供单一接口，功能包括模型间切换、API key 生成、用户管理与额度/计价体系、请求日志与审计。部署依赖 Docker 与 PostgreSQL：可通过 Docker Compose 一键启动（自动附带容器化 Postgres），或 Docker Run 接入自有数据库；通过 config.yaml 与 DWCTL_ 前缀环境变量配置，支持原生认证（JWT、SMTP 邮件重置）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接入多模型提供商的单一接口与认证层
- API key 生成、用户管理与额度/计价体系
- 请求日志、监控与审计推理活动
- config.yaml + DWCTL_ 环境变量两级配置，Docker Compose/Run 两种部署方式

## 适用场景

- 团队统一网关接入多家 LLM 提供商并集中管理密钥
- 为自托管模型套上带鉴权与额度控制的 API 层
- 对推理请求做日志记录与审计

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6: The Doubleword Control Layer (dwctl) is the world’s fastest AI model gateway (450x less overhead than LiteLLM). It p
> L9: - Turn any model (self-hosted or hosted) into a production-ready API with full auth and user controls

## 星数曲线

```mermaid
xychart-beta
    title "doublewordai/control-layer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 95 --> 97
    line [96, 96]
```

2026-10-18 96 → 2026-10-25 96（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `087fc0cf4cb0` · [字段定义](../../DATASET.md)*
