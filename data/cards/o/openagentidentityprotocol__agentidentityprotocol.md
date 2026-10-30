# openagentidentityprotocol/agentidentityprotocol

⭐ 38 · Apache-2.0 · 推送 2026-03-05 · [GitHub](https://github.com/openagentidentityprotocol/agentidentityprotocol) · [官网](https://github.com/openagentidentityprotocol/openagentidentityprotocol#readme) · 个人维护

**AI agent 的零信任身份与授权协议及 MCP 策略执行代理**

面向 MCP 与自主 agent 的开源安全标准与 Go 参考实现。两层设计：Layer 1 用密码学身份（AID 与签名令牌 AAT）标识 agent 身份，Layer 2 作为客户端（Cursor/Claude 等）与 MCP 工具服务器之间的透明代理，按 YAML 策略对每次工具调用做允许/拒绝/人工审批，含 DLP 扫描、吊销检查与 JSONL 审计日志。目标提交 IETF 作为 Internet of Agents 身份标准。Go SDK 标注 Stable，Rust 计划中；Layer 1 状态标注 IN PROGRESS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 密码学身份（AID + 签名 AAT 令牌 + 注册表吊销列表）
- 工具调用级策略代理：per-tool/per-argument 校验与 Human-in-the-Loop 审批
- 请求与响应双向 DLP 扫描与不可变审计日志
- aip wrap / aip --generate-cursor-config 命令行快速接入

## 适用场景

- 在 agent 与 MCP 工具服务器之间拦截未授权或被注入的危险调用
- 为企业 agent 操作生成满足 SOC 2/GDPR/HIPAA 的审计记录
- 对 agent 访问数据库、文件等系统资源做细粒度授权

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: AIP (Agent Identity Protocol) is an open-source standard for **authentication, attestation, authorization, and gove
> L74: ### Layer 2 — Policy Enforcement (Runtime)
> L76: AIP also operates as a transparent proxy between the AI client (Cursor, Claude, VS Code) and the MCP tool server. E

## 星数曲线

```mermaid
xychart-beta
    title "openagentidentityprotocol/agentidentityprotocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cd6c15775b17` · [字段定义](../../DATASET.md)*
