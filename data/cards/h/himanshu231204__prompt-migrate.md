# himanshu231204/prompt-migrate

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/himanshu231204/prompt-migrate) · 个人维护

**为 LLM 提示词与 agent 配置提供版本化迁移的 Python CLI**

以 Alembic 的迁移协议方式管理提示词与 agent 配置：配置以 JSON 存于 Git，diff 生成有序修订链，upgrade/downgrade 基于 before/after 快照可逆执行，状态存于本地 SQLite 并通过校验和检测手工改动导致的漂移（check 命令返回稳定退出码）。仅用 Python 标准库、零运行时依赖、无需 API key 与网络调用；环境均为本地 SQLite 文件，v0.1 不部署到任何运行时，作者明确不建议用于生产提示词管理。

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

- 有序线性修订链，每条修订保存完整前后快照，downgrade 确定可逆
- 修订应用带校验和，手工改动环境或修订会被报为 drift
- 纯 JSON 修订不执行代码，秘密值被启发式拒绝与脱敏
- CI 集成：稳定退出码、--output json、validate/check 用于流水线校验

## 适用场景

- 把提示词变更纳入 Git 评审与有序迁移流程
- 在 CI 中重放全部修订验证迁移历史可从头干净应用
- 检测环境配置是否偏离已应用的历史修订
- 多 agent 系统中管理 planner/reviewer 等多份配置草稿

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: **Alembic-style migrations for LLM prompts and AI agent configuration.** Keep prompts and agent configs as Git-trac
> L33: - **Declarative and safe:** revisions are pure JSON, never executable code. The runtime uses only the Python standa


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `17d69d194af2` · [字段定义](../../DATASET.md)*
