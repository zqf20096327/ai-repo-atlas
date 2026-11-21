# agentsmith-tools/maintainer-agent

⭐ 13 · Shell · MIT · 推送 2026-11-20 · [GitHub](https://github.com/agentsmith-tools/maintainer-agent) · [官网](https://agentsmith-tools.github.io/maintainer-agent/) · 个人维护

**无人值守的开源仓库维护 agent：审查 PR、建 issue、按证据合并**

面向开源仓库的无人值守维护工具：定时调用 Claude Code/Codex/Cursor/opencode 等后端，对 pull request 做审查、建立与归档 issue、审计任务清单、加固 CI、清理已合并分支并提示应发版本，结果发布到 GitHub。安全机制包括默认 POST=off 只读试运行、生成的后端动词 deny 墙、基于变异测试回执（receipt）的合并门槛与身份门控。以 shell 脚本安装运行，当前维护 sysknife 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认 POST=off 的试运行模式：所有 GitHub 写操作在设置中被拒绝
- 合并需 mutation-proved 验证回执（observed/dependency/asserted 三类）
- 从 deny.json 生成覆盖各安装目录的 40 个拒绝动词墙
- Dependabot PR 专用路径：semver 分类、action pin 与 pip hash 校验

## 适用场景

- 让 agent 在定时任务中审查并处理仓库的 pull request
- 在无人值守场景下按验证回执自动合并已证明的修复
- 自动处理与分类 Dependabot 的依赖升级 PR

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: An unattended maintainer for an open-source repository. It runs Claude Code (or
> L14: Codex, Cursor, or opencode) on a timer to review pull requests, file and place


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `e5fd24f59532` · [字段定义](../../DATASET.md)*
