# compforge/case-code-review

⭐ 10 · Go · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/compforge/case-code-review) · 个人维护 · 中文 README

**面向开发者的轨迹评估驱动 agentic 代码审查流水线**

ccr 是一个 agentic 代码审查流水线：将代码变更组织为最小可解释行为的 Unit，先由 Review 1 探索生成 Hypothesis，再由 Review 2 独立核验源码、diff、基线、影响与归因，最后经确定性的 Trial 门槛输出带证据的 Finding。基于 CodeGraph 追踪调用关系形成审查上下文，支持 spec/case/rule 等自撰知识注入、token 预算限制、JSON/JSONL 输出接入 CI，以及会话录制与 Viewer 观测。以 Go 工具形式分发，安装为 ccr 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段流水线：发现（Review 1）→核验（Review 2）→确定性交付门槛（Trial）
- 基于 CodeGraph 的调用关系追踪与跨文件 Unit 组织
- 支持 token 预算、超时控制、--preview/--dry-run 先检视后消耗
- 会话 JSONL 录制、自动轮转与 Viewer 运行观测

## 适用场景

- 对分支/提交/暂存变更做仓库级证据审查
- 在 CI/bot 中以 JSON 输出接入持续 PR/MR 审查
- 结合需求背景说明（--background）与自撰 spec 知识审查业务约束

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: > A trajectory-evaluation-driven agentic code review pipeline that turns code changes into evidence-backed Findings.
> L96: ### Review 1 discovers; Review 2 verifies; Review 3 gates
> L104: The analogy explains separation of duties; these are code-review stages, not legal simulations. Review 1 is encour


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `db075c9ea1cf` · [字段定义](../../DATASET.md)*
