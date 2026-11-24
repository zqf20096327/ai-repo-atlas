# 0x471/provable-harness

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/0x471/provable-harness) · 个人维护

**可在 SP1 zkVM 中证明运行过程的 AI agent harness**

以 Rust 编写的研究原型（未审计）：agent 正常运行时记录模型响应与工具结果作为私有 witness，随后在 SP1 zkVM 中重放同一 harness 代码生成证明，验证者约两秒即可核对模型看到的内容、每次工具调用及其策略判定、文件变更与运行结局。模型与网页调用可经 TLSNotary（zkTLS）认证来源。默认信任模式依赖签名的模型网关；文档明示不覆盖模型内部计算过程、公证人串通等情形，Groth16 零知识模式已实现但未实际产出证明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- SP1 zkVM 重放运行记录并产出可验证证明
- 每次工具调用按实际参数对照策略检查
- 模型与外部调用经 TLSNotary（zkTLS）认证
- 脚本引擎计量操作与数据量以约束证明开销

## 适用场景

- 发布无需信任即可核验的安全评测报告
- 代替他人操作账户/邮箱的 agent 每次会话出具证明
- 事后审计 agent 事件且日志无法被篡改

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: The agent runs as usual. Afterwards, the SP1 zkVM replays the same harness code over a recording of the run and prod
> L36: **Evals that don't have to be taken on trust.** Today, a safety eval result is a number in a report: readers cannot
> L55: The harness core, `ph-core`, does no I/O of its own. Model and tool access go through two small interfaces, so the 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c777473606a4` · [字段定义](../../DATASET.md)*
