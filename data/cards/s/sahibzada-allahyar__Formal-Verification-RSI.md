# sahibzada-allahyar/Formal-Verification-RSI

⭐ 2,852 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/sahibzada-allahyar/Formal-Verification-RSI) · 个人维护

**Lean 4/Dafny 证明检查器：拦截 AI 假证明并支持验证式自改进**

面向 AI 生成形式化证明与代码的验证工具：Millennium Harness 锁定任务的冻结规格，检查求解是否走逃生通道（sorry、assume、重定义运算符、篡改规格等），输出 PROVED/CHEAT_REJECTED 等 JSON 判定，可直接嵌入 agent 循环作为无法作弊的门控；Millennium RSI 是在該奖励下改进自身 harness 的 agent，新引理须通过内核检查方可入库。附基准审计、96 个红队作弊用例与 agent 实验复现脚本。需要 Python 3.10+ 与 pinned 的 Lean 4.23/Dafny 4.11 工具链；检查器本身不调用模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 冻结规格 + 逃生通道检查（sorry/assume/{:axiom}/实例重定义/内核重放）
- JSON 判定输出（PROVED/CHEAT_REJECTED/SPEC_TAMPERED 等），可作 agent 循环门控
- Millennium RSI：自改进 agent 的奖励不可作弊，引理须内核检查后入库
- 提供基准审计、红队与 agent 实验的复现脚本与测试

## 适用场景

- 在 agent 训练或评测循环中拦截伪装为已验证的假证明
- 审计已发布为 verified 的 AI 证明方案是否含作弊
- 研究以形式化验证为奖励的递归自改进（RSI）

## 场景标签

 · 领域:形式化验证/AI安全

## 证据(README 行号)

> L33: **Millennium Harness** is a model-free gate: a solution counts only if the frozen specification kept its meaning an
> L82: Millennium RSI is an agent that improves its own harness, and keeps a change only if Millennium Harness certifies m
> L154: Each prints a JSON verdict (`PROVED`, `UNPROVED`, `CHEAT_REJECTED`, `SPEC_TAMPERED` or `CHECK_ERROR`) whose `feedb


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `16158c150167` · [字段定义](../../DATASET.md)*
