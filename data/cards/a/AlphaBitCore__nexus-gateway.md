# AlphaBitCore/nexus-gateway

⭐ 25 · Go · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/AlphaBitCore/nexus-gateway) · [官网](https://alphabitcore.com/nexus) · 组织维护

**企业级 LLM 流量网关：统一合规、路由 20+ 提供商、缓存配额与审计**

在三个层面截获企业 LLM 流量并统一处理：SDK 层 AI 网关（应用以 OpenAI SDK 形态接入，归一化后经 20 个适配器路由至 Anthropic/Gemini/Bedrock 等 20 家提供商）、网络层透明 TLS MITM 合规代理、OS 层桌面 Agent（macOS/Linux/Windows GA）。提供多级配额与预算、精确/语义缓存（Valkey）、PII 检测与内容安全合规管线、RBAC/ABAC IAM、虚拟密钥与凭证保险库、SIEM 转发与三级熔断。架构为 5 个 Go 服务 + React 控制台，依赖 PostgreSQL 16、Valkey 8、NATS JetStream；可经 Packer 构建 AWS AMI 单机装置或 docker-compose 本地开发。源码构建的 Vectorscan 扫描器二进制不可跨 CPU 代际移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 20 个 in-tree 提供商适配器（11 个一等编解码 + 9 个 OpenAI 兼容透传）
- SDK/网络/OS 三层独立截获，Agent 流量经 Ed25519 证明头可免 MITM 直通
- PII 检测、内容安全、配额、审计与 SIEM 转发的合规管线
- 精确/语义向量缓存与多轴配额（组织/密钥/提供商/模型）

## 适用场景

- 企业统一接入多家 LLM 提供商并做成本与配额管控
- 对员工 AI 流量做合规审计、PII 检测与 SIEM 转发
- 通过桌面 Agent 在终端操作系统层截获并管控 AI 流量

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L20: Nexus Gateway intercepts enterprise LLM traffic at three layers and runs all of it through one compliance engine, o
> L24: |🔑 **AI Gateway**|SDK layer — virtual keys on `/v1/chat/*`, `/v1/responses`, `/v1/embeddings`, `/v1/messages`|`pack
> L48: Applications speak the OpenAI SDK. Nexus normalises every request to a canonical OpenAI shape, then translates wire

## 星数曲线

```mermaid
xychart-beta
    title "AlphaBitCore/nexus-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `51b43ae30dd2` · [字段定义](../../DATASET.md)*
