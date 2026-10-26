# renefichtmueller/claude-sync

⭐ 29 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/renefichtmueller/claude-sync) · [官网](https://claude-sync-demo.pages.dev) · 个人维护

**跨设备同步 Claude Code 记忆、技能与设置的 CLI 工具**

面向使用 Claude Code 的开发者，解决多台机器间 `~/.claude/` 目录（记忆、技能、项目上下文、设置）不同步的问题。机制：以 git 三向合并同步（Git/Gitea 为推荐后端，另有 iCloud/Dropbox/Syncthing/rsync 等实验后端），凭据等敏感文件永不同步，settings.json 与 plugins 变更需人工确认后才应用，每次同步前做本地快照。1.1.0 起停止同步凭据文件；静态加密与实时文件监听未实现。Node.js >= 18，从源码 git clone 后 npm 全局安装。

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

- git 三向合并处理多设备变更与冲突（同文件追加用 union 合并）
- 凭据/SSH 密钥等敏感文件永不同步，可执行命令的变更需 --accept-incoming 确认
- 每次同步前本地快照，可 claude-sync restore 回滚
- 支持 Git/Gitea/云盘/Syncthing/rsync/自定义命令 6 类后端

## 适用场景

- 在家用台式机、外出用笔记本时保持 Claude Code 上下文连续
- 新机器上一条命令接入已有记忆与技能
- 自托管 Git/私有远端保存并版本化 Claude Code 状态

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Switch machines, keep the context.** Your Claude Code memory, skills, and settings follow you everywhere.
> L41: Claude Code's `.claude/` directory stores everything — your memory, your skills, your project context, your prefere
> L70: Git and Gitea are the recommended backends. Every sync:

## 星数曲线

```mermaid
xychart-beta
    title "renefichtmueller/claude-sync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6620eb7899cc` · [字段定义](../../DATASET.md)*
