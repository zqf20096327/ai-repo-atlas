# promptshieldhq/promptshield

⭐ 20 · TypeScript · MIT · 推送 2026-05-08 · [GitHub](https://github.com/promptshieldhq/promptshield) · [官网](https://promptshield-docs.vercel.app) · 组织维护

**自托管 LLM 安全网关：检测 PII 与密钥并执行策略**

开源 LLM 安全平台，由三个仓库组成：网关负责策略执行、多提供商路由、限流、令牌预算与审计日志；检测引擎基于 Presidio 提供 6 种语言的 PII 扫描与注入检测；仪表盘提供策略编辑与运营可视化。网关内置 Gitleaks 密钥检测（150+ 规则），仅网关即可运行，引擎与仪表盘可选。提供 OpenAI 兼容 API，客户端无需更换 SDK，检测在自有基础设施内完成。通过 Docker Compose 或 uv 从源码部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网关内置 Gitleaks 密钥检测（150+ 规则，约 1-3ms/请求）
- Presidio PII 扫描支持 6 种语言（en/zh/fr/de/ko/ja）
- YAML 单文件策略，热重载不中断流量，PII 实体可 allow/mask/block
- 多提供商自动路由、API 密钥池轮转、SSE 流式支持与 Prometheus 指标

## 适用场景

- 在自有基础设施上拦截 LLM 流量中的 PII 与密钥泄露
- 按客户端实施限流与令牌预算控制
- 对 LLM 请求/响应做审计与合规留痕
- 统一管理多家 LLM 提供商的 API 密钥

## 场景标签

`模型网关` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L15: PromptShield is an open source LLM security platform. It places a gateway in front of your model traffic to detect 
> L19: - **Gateway**: policy enforcement, multi-provider routing, rate limiting, token budgets, audit logging

## 星数曲线

```mermaid
xychart-beta
    title "promptshieldhq/promptshield 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `50abea0d9f4e` · [字段定义](../../DATASET.md)*
