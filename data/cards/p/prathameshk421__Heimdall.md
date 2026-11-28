# prathameshk421/Heimdall

⭐ 3 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/prathameshk421/Heimdall) · [官网](https://heimdall-sage.vercel.app) · 个人维护

**为 AI 代码评审提供证明层的自托管 CI 门禁工具**

自托管的 PR 评审 harness：AI agent 审查每个 pull request，每条评审发现必须先产出失败的测试（在 PR 上失败两次、修复后通过）才能阻止合并；未证明的发现被隐藏并计数。提供 GitHub Action 模式（仓库内 CI，无服务器/数据库）与自托管团队模式（Docker、PostgreSQL、GitHub App，支持 Slack/Discord 等聊天命令）。合并决策由普通 Go 规则而非模型给出，需人类在指定 commit 上批准；测试在 rootless 容器隔离运行。安装需 Go 1.27 构建源码，模型端点为 OpenAI 兼容接口（默认 OpenRouter）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 证据分级机制：测试证明/确定性工具结果/团队记忆可阻断合并，模型推理单独不可
- GitHub Action 模式无需服务器与数据库，`action init` 生成工作流与配置
- team 模式测试在 rootless 容器（无网络、只读文件系统）隔离运行
- 提供供 Claude Code 等 coding agent 使用的安装 setup skill

## 适用场景

- 对高流量 PR 仓库引入 AI 评审并自动生成缺失的 CI 测试
- 过滤 CodeRabbit/Copilot 等评审机器人的无效评论，只放行有测试证明的发现
- 自托管团队以 Jira 票据驱动先写红测试再写代码的工作流

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L24: point at a real bug. **Heimdall** is an open-source harness that you run on your own infrastructure. It puts AI rev
> L32: - **Proof, not opinions.** A finding counts only when its test fails twice on the pull request and passes on the fi
> L34: - **A gate no model can talk past.** Plain Go rules decide the merge. Only a person can approve, on the exact commi


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `40d7bd7ce32f` · [字段定义](../../DATASET.md)*
