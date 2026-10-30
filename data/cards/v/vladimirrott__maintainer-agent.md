# vladimirrott/maintainer-agent

⭐ 44 · Shell · MIT · 推送 2026-10-29 · [GitHub](https://github.com/vladimirrott/maintainer-agent) · [官网](https://vladimirrott.github.io/maintainer-agent/) · 个人维护

**无人值守的开源仓库维护 agent：审 PR、发 issue、修剪分支**

在定时器上运行 Claude Code（或 Codex、Cursor、opencode）对单个仓库做维护：审查 PR、归档与放置 issue、审计 tracker、加固 CI、修剪已合并分支、提示到期发布，并将结果发布到 GitHub。核心机制是合并闸门：仅凭验证回执（mutate 守卫并看到其变红）而非绿板放行，配合逐层遏制（38 个被禁动词的 deny 墙、身份门、screen、签名回执），并自述 deny 列表不是对抗性 agent 的边界。以 shell 脚本 + profile 脚手架形式安装运行，当前维护 lacs-project/sysknife。

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

- 合并仅凭验证回执：变更守卫须使其测试变红，`gh pr merge` 保持禁用，走 maintainer-merge
- Claude 后端 --settings 含 38 个被禁动词（git push、cargo publish、凭据目录读取等），deny 墙按实际安装目录逐一生成
- Dependabot PR 专属路径：semver 分类、rebase 委托 Dependabot、DEPS_AUTOMERGE 分级放行
- POST=off 干跑模式：完成整轮运行但拒绝所有 GitHub 写操作，仅写运行报告

## 适用场景

- 单人维护的开源仓库需要定时自动审 PR、整理 issue 与修剪分支
- 想让 agent 只凭可复核的守卫回执合并 PR，而非仅看 CI 绿板
- 处理 Dependabot 依赖 PR 的分类、验证与分级自动合并

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: An unattended maintainer for an open-source repository. It runs Claude Code (or
> L70: So `gh pr merge` stays denied and `maintainer-merge` is the only path. It


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4d6986dd259c` · [字段定义](../../DATASET.md)*
