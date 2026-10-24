# GetBusbar/busbar

⭐ 213 · Rust · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/GetBusbar/busbar) · [官网](https://getbusbar.com) · 组织维护

**自托管的 AI 执行边界网关：治理模型、MCP 工具与 A2A 调用**

用 Rust 编写的单二进制自托管网关，部署在 AI 应用与模型/MCP 工具/A2A 代理之间，充当策略执行点：凭据留在边界、虚拟密钥、组预算与花费追踪、加权路由、逐通道并发上限、故障归因熔断、请求内故障切换、TLS/mTLS、Prometheus/OTLP 遥测与审计 webhook。支持 6 种模型线路协议（OpenAI、OpenAI Responses、Anthropic、Gemini、Cohere、Bedrock Converse）进出共 36 种组合，同协议路由按字节转发。面向运维/平台团队，提供安装脚本、Docker 镜像与 Helm 图表；README 中 MCP 与 A2A 治理仅声明沿用同一执行边界模型，为设计方向。

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

- 6 进 6 出共 36 种线路协议组合，同协议路由按原始字节转发
- 请求内故障切换与故障归因熔断：坏密钥只停用单通道
- 虚拟密钥、组预算与花费追踪、审计 webhook
- 单 Rust 二进制（12.39 MiB），容器镜像 5.74 MiB，无需数据库或 sidecar

## 适用场景

- 统一管控多家模型供应商的凭据、路由与预算
- 在应用与模型之间加一层合规审计与花费控制
- 为 Kubernetes 环境部署轻量 LLM 治理网关

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L19: Busbar sits between AI applications and the destinations they can reach:
> L29: Busbar is a self-hosted, customer-operated static Rust binary. It keeps
> L41: Six model wire protocols, first class on both sides: OpenAI, OpenAI

## 星数曲线

```mermaid
xychart-beta
    title "GetBusbar/busbar 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 196 --> 213
    line [197, 204, 211, 212]
```

2026-10-18 197 → 2026-10-24 212（+15）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `27be5b8ca375` · [字段定义](../../DATASET.md)*
