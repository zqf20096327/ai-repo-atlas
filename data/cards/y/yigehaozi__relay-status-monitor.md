# yigehaozi/relay-status-monitor

⭐ 23 · TypeScript · MIT · 推送 2026-07-12 · [GitHub](https://github.com/yigehaozi/relay-status-monitor) · [官网](https://ssss.ss) · 个人维护 · 中文 README

**自托管的 AI API 中转站状态监控面板**

基于 Next.js 14 与 PostgreSQL 的自托管监控面板，统一管理多个 SUB2API 与 New API 上游：按 Key/分组采集余额、接口延迟、模型测速（含首 Token 延迟与流式 TPS），聚合在线/降级/离线状态，支持余额、延迟、连续失败与可用率告警规则，通过飞书 Webhook 通知。日常轻量采集只查余额与模型列表，重量采集会发送真实模型请求并消耗额度。凭证以 AES-256-GCM 加密存储，本地用户名密码登录。安装需 Node.js 20+、pnpm 9+、PostgreSQL 14+，通过 git clone 与 pnpm 命令运行。

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

- 统一管理多个 SUB2API 与 New API 上游，支持多 Key/分组
- 采集余额、延迟、首 Token 延迟与流式 TPS，轻重分层采集
- 余额/延迟/连续失败/可用率告警规则与飞书 Webhook 通知
- 上游凭证 AES-256-GCM 加密存储，适配器架构可扩展新上游类型

## 适用场景

- 自建 AI API 中转站的余额与可用率日常监控
- 模型测速对比不同上游的延迟与流式 TPS
- 中转站异常时通过飞书机器人接收告警

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: 一个面向 AI API 中转站的自托管状态监控面板。它可以统一管理多个 SUB2API 与 New API 上游，按 Key/分组采集余额、延迟、可用率和模型测速数据，并通过告警规则与飞书 Webhook 发送异常通知。
> L41: - 多上游管理：支持 SUB2API 与 New API，可为一个上游配置多个独立 Key/分组。
> L42: - 指标采集：记录余额、接口延迟、模型测试延迟、首 Token 延迟和流式 TPS。

## 星数曲线

```mermaid
xychart-beta
    title "yigehaozi/relay-status-monitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `1eb1cf69042d` · [字段定义](../../DATASET.md)*
