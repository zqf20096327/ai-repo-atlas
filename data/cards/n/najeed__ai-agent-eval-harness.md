# najeed/ai-agent-eval-harness

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/najeed/ai-agent-eval-harness) · [官网](https://najeed.github.io/ai-agent-eval-harness/) · 个人维护

**企业 AI agent 的评测与验证框架：核验行为、状态与合规**

AgentV 是面向企业业务工作流的多 agent 评测与验证 harness（MultiAgentOps）。它在 agent 执行环路内验证状态一致性、策略遵循与业务结果，机制包括 Ed25519 签名轨迹、Environmental/Behavioral/Forensic DNA 遥测、验证证书 VC v3.0.0 与 NIST AI-100-1 对齐。自带 5,000+ 场景语料覆盖 50+ 行业，支持 HTTP/SSE/Local/Socket/OpenAPI 五种 agent 通信协议，提供 Flask REST API 与 React 可视化调试台。快速入门无需 API key 与 LLM，使用 mock agent 离线运行。Apache 2.0 许可，另提供 Enterprise Edition。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5,000+ 开箱场景、50+ 行业评测语料（AES v1.4 规范）
- Ed25519 签名轨迹与 WORM 日志的取证级验证
- 支持 HTTP/SSE/Local/Socket/OpenAPI 五种 agent 接入协议
- 零 key 快速入门：mock agent 离线运行并生成 HTML 报告

## 适用场景

- 上线前验证 agent 是否执行了正确操作、改变正确状态并遵循策略
- 金融/医疗/电信等受监管行业做 agent 合规评测
- CI/CD 中对 agent 做回归与红队测试

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: **88% of enterprise AI agents fail to reach production.** Not because the model is wrong. Because no one verified th
> L11: AgentV sits inside the execution loop and verifies state parity, policy adherence, and business outcomes before you
> L104: - `/eval_runner`: Modular Core Engine (Multi-turn loop, Sandbox, Metrics, Simulators, Mutator).

## 星数曲线

```mermaid
xychart-beta
    title "najeed/ai-agent-eval-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0b72c2377b3f` · [字段定义](../../DATASET.md)*
