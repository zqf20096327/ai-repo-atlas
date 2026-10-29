# togettoyou/zke

⭐ 107 · Go · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/togettoyou/zke) · 个人维护 · 中文 README

**AI 原生的多集群 Kubernetes 操作环境与受控 AIOps Agent**

ZKE 把数据中心、私有云、公有云与边缘的多个 Kubernetes 集群收敛为一个统一操作环境：每集群部署 Agent 主动向 Server 建立 QUIC/mTLS 出向连接，无需开放 API Server 入口；浏览器中的桌面式 Console 以窗口和 Dock 组织集群接入、容器服务、Helm 应用、终端、监控与审计。AIOps 作为常驻运维 Agent，与用户共用同一套 RBAC 权限和审计通道，变更先 DryRun 预演再提交，全程 append-only 留痕。Server 为单二进制，可一条 Docker 命令启动（含 PostgreSQL 与 VictoriaMetrics）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 主动出向 QUIC/mTLS 连接，只需一条出向通道接入内网/边缘集群
- AIOps Agent 与人共用 RBAC 权限与审计，模型不持有 kubeconfig
- 变更先服务端 DryRun 预演、按 preview_id 提交、幂等键防重复写入
- 桌面式多窗口 Console，集群接入、终端、Helm、监控、审计以独立应用组织

## 适用场景

- 统一管理分散在私有云、混合云和边缘的多个 Kubernetes 集群
- 在内网集群不开放 API Server 入口的前提下远程运维
- 让 AI Agent 在受权限约束和审计下执行伸缩、回滚与 Manifest 变更
- 多窗口并行排查工作负载：资源详情、事件、日志与终端同屏

## 场景标签

 · 领域:云原生/K8s 运维平台

## 证据(README 行号)

> L14: ZKE（Z Kubernetes Engine）是一个 AI 原生的 Kubernetes 云操作环境，把分散在数据中心、私有云、公有云和边缘的 Kubernetes 集群，收敛成一个可以直接操作的云环境：Agent 从每个集群主
> L108: > **AIOps：** 在「平台配置 → AI 模型」中填写 OpenAI Responses 或 Chat Completions 兼容端点并启用，再把

## 星数曲线

```mermaid
xychart-beta
    title "togettoyou/zke 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-29 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dbbeceedb1e3` · [字段定义](../../DATASET.md)*
