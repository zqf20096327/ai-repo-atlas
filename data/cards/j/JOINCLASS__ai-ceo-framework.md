# JOINCLASS/ai-ceo-framework

⭐ 61 · Shell · MIT · 推送 2026-11-17 · [GitHub](https://github.com/JOINCLASS/ai-ceo-framework) · [官网](https://joinclass.co.jp/?utm_source=github&utm_medium=repo&utm_campaign=dx-cta-2026-11) · 组织维护 · 中文 README

**基于 Claude Code 的一人公司多 agent 运营框架**

面向一人公司/独立创始人的运营框架：以单个 CLAUDE.md 作为编排器，路由自然语言请求到 15 个业务 agent（CTO/CMO/CFO/Legal 等），配 5 个可复用技能与权限分级、审批队列（对外动作需 CEO 批准）、6 阶段假设验证门、错误自动重试后升级机制。安装方式为复制目录文件并运行 setup.sh 回答配置问题，之后在 Claude Code 内对话或使用斜杠命令使用。子 agent 功能需 Claude Code Max 或 Anthropic API key；数据保存在本地 .company/ 目录。维护方 JoinClass LLC 另提供面向日本企业的付费咨询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个业务 agent + 5 个技能，编排器上下文占用保持在 10-15%
- 对外动作（邮件/社媒/发票/部署）经审批队列草稿-审核-执行
- 新项目须通过 6 阶段假设验证门（最多重试 2 次后生成撤退报告）
- setup.sh 5 分钟初始化，agent 以 .md 文件定义、编排器自动发现

## 适用场景

- 独立创始人用一套 Claude Code 配置驱动开发、营销、财务等日常业务
- 让 AI 起草对外内容后自行审批再执行，控制外发风险
- 小型团队按部门优先级裁剪使用部分 agent

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: **15 AI Agents + 5 Production Skills + Approval Pipeline. One-person company, mostly run by automation.**
> L36: ### 15 AI Agents (`agents/`)
> L70: ### Orchestrator (`CLAUDE.md`)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `b6f857a6dc62` · [字段定义](../../DATASET.md)*
