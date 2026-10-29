# pic-standard/pic-standard

⭐ 69 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/pic-standard/pic-standard) · [官网](https://madeinpluto.com/pic) · 组织维护

**AI agent 工具调用前的意图与证据验证标准及参考实现**

开放协议 PIC：在 agent 执行高危工具调用（支付、隐私、不可逆操作）前插入验证门。Action Proposal 以结构化合约携带 intent、impact、provenance、claims、evidence 与 action；验证器校验签名证据（Ed25519/SHA-256）、规范证明与提案绑定、信任清洗与过期。本地运行，无需托管账户或模型 API key。提供 Python 参考实现（pip 安装）、CLI、TypeScript 实现、91 个一致性测试向量，以及 MCP 守卫、LangGraph 节点、OpenClaw 插件与 HTTP API 集成。规范在 v1.0 冻结前仍为草案。

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

- Action Proposal 合约：intent/impact/provenance/claims/evidence/action 七类字段
- Ed25519 规范证明绑定工具、参数摘要与声明摘要，支持过期与撤销密钥
- Python MCP 守卫与 HTTP 桥接做实时参数与已验证提案比对，不符即拒绝
- 91 个共享一致性测试向量，Python/TypeScript 双实现差分 CI

## 适用场景

- 在 agent 执行支付、数据导出、删除等不可逆操作前核验签名批准
- 防止 agent 基于伪造签名或被篡改的证据执行工具调用
- 为多语言服务通过 HTTP API 统一接入 PIC 验证

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L21: PIC adds a verification gate before tool execution. It checks the action proposal, verifies supporting evidence aga
> L138: |Python MCP server|Synchronous and asynchronous tool guards, evidence verification, live-argument binding, decisio
> L40: PIC gives your application a contract for checking the proposed action and its supporting evidence before execution

## 星数曲线

```mermaid
xychart-beta
    title "pic-standard/pic-standard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-29 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d7b3f8daa4ef` · [字段定义](../../DATASET.md)*
