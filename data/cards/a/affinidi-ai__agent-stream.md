# affinidi-ai/agent-stream

⭐ 4 · Rust · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/affinidi-ai/agent-stream) · 组织维护

**面向 Agent 多厂商 LLM 流量的 Rust 治理网关**

Rust 实现的 AI 网关，位于 Agent 与模型提供方之间：解析 OpenAI Chat Completions/Responses 与 Anthropic Messages 格式的请求，逐调用执行路由、故障转移、负载均衡、熔断、缓存、护栏、预算与计量，并生成可验证的签名哈希链治理记录；内置 Prompt Guard 对敏感数据掩码/阻断，策略用 OPA Rego 进程内求值，支持按阶段成本控制与基于回放的漂移检测。由 Affinidi 维护，属于 Affinidi Trust Fabric 的一部分，尚在活跃开发期，官方提示接口与存储配置可能随版本变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 解析模型 API 语义而非转发字节，可检查、转换、计量、缓存并路由每个调用
- Fail-closed 护栏、PII 掩码/假名化/阻断与 LLM Judge/Jury 阶段审查
- 签名哈希链 Governance Record，可验证与导出供审计
- 单一 Rust 二进制 + 同进程 React 仪表盘，无数据库无 sidecar，状态存内存缓存与 JSON 文件

## 适用场景

- 为多厂商模型调用统一配置认证、护栏、限流与预算
- 在不改 Agent 代码的情况下切换或混合多个模型提供方
- 为合规审计留存可验证的调用证据链
- 按团队归属计量支出并在调用前校验预算

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L9: Agent Stream sits between agents and the model providers they call. It routes each call
> L13: It understands the model APIs rather than forwarding bytes: it reads OpenAI Chat
> L184: |OpenAI Chat Completions|On by default on every LLM Surface; a Surface can restrict it|

## 星数曲线

```mermaid
xychart-beta
    title "affinidi-ai/agent-stream 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-19", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f4958c4efb6f` · [字段定义](../../DATASET.md)*
