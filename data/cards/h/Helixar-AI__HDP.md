# Helixar-AI/HDP

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/Helixar-AI/HDP) · [官网](https://helixar.ai/about/labs/hdp/) · 组织维护

**AI 代理人类委托的密码学审计协议与 SDK**

HDP 是一个开放协议，对 agentic AI 中人类向代理、代理向代理的委托链生成 Ed25519 签名、RFC 8785 规范化的防篡改令牌，验证完全离线且仅依赖签发者公钥。以 TypeScript/Python 多包形式提供，覆盖 CrewAI、Grok/xAI、AutoGen、LangChain、LlamaIndex、MCP 及机器人（Physical AI）等框架的中间件。边界明确：不是授权协议，仅记录与核验完整性；规范以 IETF 个人 Internet-Draft 形式提交。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ed25519 签名 + RFC 8785 规范化的委托链令牌，离线验证
- 12 个 SDK 包覆盖 CrewAI/Grok/AutoGen/LangChain/LlamaIndex/MCP/机器人
- HDP-P 面向机器人：执行前核验 EDT、不可逆性上限与力/速度限制
- IETF Internet-Draft 规范化（draft -03，record-only 语义）

## 适用场景

- 为多代理系统的委托与活动建立可审计的防篡改记录
- MCP 服务或代理框架中附加委托来源追踪
- 机器人动作执行前做签名与安全边界检查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L36: HDP (Human Delegation Provenance) is an open protocol that captures, structures, cryptographically signs, and verif
> L40: **Who it is for:** developers building AI agents with Grok/xAI, CrewAI, MCP servers, or any OpenAI-compatible API w
> L52: |Package|Registry|Language|Framework|Description|

## 星数曲线

```mermaid
xychart-beta
    title "Helixar-AI/HDP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aef7abf41abb` · [字段定义](../../DATASET.md)*
