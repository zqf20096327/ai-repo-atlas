# goranai/try-professional

⭐ 3 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/goranai/try-professional) · 个人维护

**把多 Agent 组织成公司层级交付任务的多 Agent 编排框架**

以公司组织结构（CEO、经理、工人、QA）编排多个完整 Agent：每个角色有独立记忆与技能，技能可从 GitHub 拉取并检查。支持三种运行载体——Claude Code（主要测试路径）、Codex/Antigravity、自带引擎（任意 OpenAI 兼容 key），可按角色混用不同模型。提供审批门控、密钥过滤、审计日志、外部产出追踪与定时任务；普通一次性任务官方建议用单 Agent。以 Python 包发布，首次审批会下载约 0.22 GB 本地嵌入模型。

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

- CEO/经理/工人/QA 的公司式层级 Agent 组织，每角色独立记忆与技能
- 按角色混用运行时：Claude Code、Codex、Antigravity、自带引擎可逐角色配置
- 密钥不外泄、外部变更等待审批、审计日志等安全与追踪机制
- 支持 Telegram 对话入口与定时任务调度

## 适用场景

- 把一个业务任务拆解成多角色协作并生成交付文件
- 让 Agent 公司长期跟踪它对外发出的产出（PR、邮件、报价）
- 在终端或 Telegram 中与 Agent 团队持续对话派活

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: **An agent, but a company.** You talk to the CEO. Managers split the work, workers do it with real tools, QA and ma
> L23: - **Its own engine,** with any OpenAI-compatible key, such as DeepSeek, Grok, or OpenAI: `trypro chat`. Cheap model
> L25: **They can be mixed, role by role.** Say a company coordinates in Claude Code, its researchers look for bugs with G


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `421e80a979b6` · [字段定义](../../DATASET.md)*
