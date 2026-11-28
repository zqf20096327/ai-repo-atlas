# gravion-ux/agent-skills

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/gravion-ux/agent-skills) · 个人维护

**面向 agent 开发者的 1,224 条技能目录与 BM25 路由库**

一个包含 1,224 条手工编写技能的目录，覆盖 42 个领域，每条技能为九节固定结构的 SKILL.md（用途、适用/不适用场景、输入、流程、输出契约、校验清单、安全说明等）。核心机制是三层路由：零依赖 Python 包提供无网络、无模型调用的确定性 BM25 评分器，42 个领域路由器列出各域技能的 use-when 条款，主技能据此选出一条主技能加至多三条支撑技能并排序。明确声明不是托管服务、API 或运行时，技能是指令而非可执行程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,224 条手工编写技能覆盖 42 个领域
- 确定性 BM25 路由：无网络调用、无模型调用、同查询同结果
- 每条技能为九节固定结构的 SKILL.md，含输出契约与校验清单
- 零依赖 Python 包与 CLI（list/route/export/pack）

## 适用场景

- 为 agent 从目录中按任务描述挑选合适的技能与技能链
- 按领域浏览技能清单而不加载整个目录
- 按固定格式贡献并生成新技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: A library of **1,224 agent skills** across **42 domains**, with a deterministic router that
> L36: - Not a runtime that executes anything for you. The skills are instructions for an agent;
> L104: 1. **Deterministic scorer (`agentskills route`).** BM25 over five weighted fields —


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ab170426f03f` · [字段定义](../../DATASET.md)*
