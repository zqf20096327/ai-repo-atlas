# alberthild/vainplex-openclaw

⭐ 13 · TypeScript · 推送 2026-10-30 · [GitHub](https://github.com/alberthild/vainplex-openclaw) · 个人维护

**为 OpenClaw 自主 agent 提供治理、记忆与审计的六插件套件**

面向 OpenClaw agent 框架的插件套件，含六个生产运行中的插件：Governance（URL 威胁检测、提示注入扫描、Merkle Tree 审计、TOTP 2FA 审批）、Membrane（情景记忆）、Cortex（对话线程跟踪与决策提取）、Leuko（健康检查与自愈）、Knowledge Engine（实体关系抽取、无外部 API）、NATS EventStore（事件审计与回放）。各插件独立可用，可通过 Brainplex CLI 安装器或 npm 手动安装。声明与 NVIDIA NemoClaw 兼容，并给出网络端点白名单配置要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Governance 提供 Agent 防火墙、Merkle Tree 审计链与 TOTP 2FA 审批
- Cortex 跟踪对话线程、提取决策并生成抗压缩的引导上下文，支持 10 种语言
- 所有事件写入 NATS JetStream，支持回放与多 agent 关联审计
- 各插件零跨插件依赖，可单独选用或整套安装

## 适用场景

- 给长期运行的 OpenClaw agent 加装治理与审计能力
- 为 agent 增加情景记忆和对话结构化提取
- 运维人员追踪凭证泄露、状态漂移等运行风险

## 场景标签

`Agent 记忆` `网络安全` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L16: |**Governance**|The **Agent Firewall** (URL threat detection, prompt injection scans), **Proof-of-Guardrails** (Mer
> L73: Governance gates every message. Membrane injects episodic context before the agent responds. After the response, Co
> L136: - `register(api: OpenClawPluginApi)` hook pattern

## 星数曲线

```mermaid
xychart-beta
    title "alberthild/vainplex-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e89db2a101a7` · [字段定义](../../DATASET.md)*
