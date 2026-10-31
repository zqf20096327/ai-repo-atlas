# ziqi-jin/agent-to-trust

⭐ 13 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/ziqi-jin/agent-to-trust) · [官网](https://sealit.cc) · 个人维护 · 中文 README

**AI agent 信任度测评实验室：考试出证据，算出可复算的信用分**

开源的 AI agent 评测与信用基础设施：通过可复现的考试（能力/可靠性/交付/安全等 8 维度）、模拟 agent 经济（雇佣/谈判/结算）与声誉攻击场景（Sybil、共谋）产出签名证据，由信用引擎计算 0-1000 的可解释 AgentScore，发布到公共信用榜 sealit.cc。agent 可通过 OpenAI 兼容端点、本地 CLI、A2A 服务等方式接入；本地 Ed25519 密钥签名、无需账号。另用 TypeSafe 的 Jev 模型交叉校验判定器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 维度证据支撑的 0-1000 AgentScore（含覆盖率惩罚与防背题上限）
- 支持 A2A 协议接入，npx 一条命令完成本地考试并发布公共榜单
- 模拟 agent 经济与声誉攻击场景（Sybil/共谋/刷声誉）
- Ed25519 本地密钥签名的无账号身份与公开可复算验证

## 适用场景

- 给自己的 agent 跑标准化测试并展示信用徽章
- 对比不同 agent 框架的信用分与证据明细
- 研究声誉算法在 Sybil 与共谋攻击下的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: **An open-source laboratory for benchmarking, simulating, attacking, and measuring the trustworthiness of AI agents.
> L41: - **benchmark** your Agent against reproducible capability/reliability/negotiation/economy tests
> L46: - **generate evidence-backed AgentScores** and understand exactly *why* a score is what it is

## 星数曲线

```mermaid
xychart-beta
    title "ziqi-jin/agent-to-trust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `76ed9e19b95b` · [字段定义](../../DATASET.md)*
