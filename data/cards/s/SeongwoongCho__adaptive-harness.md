# SeongwoongCho/adaptive-harness

⭐ 10 · Python · MIT · 推送 2026-03-16 · [GitHub](https://github.com/SeongwoongCho/adaptive-harness) · 个人维护

**Claude Code 插件：按任务自动路由工作流并自我演进**

以 Claude Code 插件形式安装的元编排层：对每个任务按 6 轴分类（类型/不确定性/影响面/可验证性等），从 23 个内置与实验性工作流（harness）中自动路由选择，结果按 6 维加权评分；每 2 次评估触发演进管理器，通过 A/B 测试改写 agent 人设与 skill.md、组合生成新 harness，提案先进实验池，5 次连续成功才转正。高不确定性且难验证的任务自动触发双 harness 并行加合成器合并。依赖 Claude Code 会话与 Anthropic Sonnet/Opus 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 6 轴 LLM 分类任务并自动路由到 23 个内置/实验性 harness
- 6 维固定权重评分（correctness 0.25 等）驱动路由权重调整
- 演进系统：A/B 测试改写 harness 内容并按模式库生成新 harness
- 复杂任务支持自适应 harness 链与双 harness ensemble 模式

## 适用场景

- 让 Claude Code 在不同类型的编码任务中自动选择合适工作流
- 积累评估数据后自动优化团队的工作流配置
- 为高风险任务并行运行两种方案再合并结果

## 场景标签

`提示工程` `工作流自动化` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A self-improving harness router for Claude Code.
> L45: claude plugin install adaptive-harness@adaptive-harness


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7a05b43e902f` · [字段定义](../../DATASET.md)*
