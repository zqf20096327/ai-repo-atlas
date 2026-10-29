# cloud-barista/cb-tumblebug

⭐ 82 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/cloud-barista/cb-tumblebug) · 组织维护 · 中文 README

**多云基础设施统一管理框架，供运维在 AWS/Azure/GCP 等上开通资源**

Cloud-Barista 项目的多云基础设施管理系统：通过统一接口在 AWS、Azure、GCP、阿里云等 CSP 上开通、管理与编排资源，底层由 CB-Spider 提供云 API 抽象，附带 MC-Terrarium（VPN 等）、OpenBao 凭据加密、ETCD/PostgreSQL 存储与 CB-MapUI 地图式 GUI，以 Docker Compose 全栈启动，另提供 Helm/Kubernetes（Beta）部署。云凭据经加密文件注册并混合加密传输。AI 部分为 MCP Server，可通过 Claude/VS Code 等 AI 助手用自然语言控制基础设施。README 声明未达 1.0、功能尚不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一平台编排 AWS/Azure/GCP/阿里云等多 CSP 资源
- Docker Compose 一键启动全栈，另提供 Helm/Kubernetes 部署（Beta）
- 凭据加密存储（OpenBao）与混合加密传输
- MCP Server 支持经 Claude/VS Code 等用自然语言管理基础设施

## 适用场景

- 跨多个云厂商统一开通和管理计算、网络资源
- 在多个云上部署 GPU 实例运行 AI/LLM 工作负载
- 通过 AI 助手以自然语言操作多云基础设施

## 场景标签

 · 领域:云计算/多云基础设施管理

## 证据(README 行号)

> L23: **CB-Tumblebug (CB-TB)** is an advanced **multi-cloud infrastructure management system** that enables seamless prov
> L31: - **🤖 AI-Powered Management**: NEW! Control infrastructure using natural language via our MCP Server
> L66: - Control CB-Tumblebug through AI assistants like Claude and VS Code

## 星数曲线

```mermaid
xychart-beta
    title "cloud-barista/cb-tumblebug 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-29 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6aa6688d73cc` · [字段定义](../../DATASET.md)*
