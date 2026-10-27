# AICodeLion/agent-pack-n-go

⭐ 92 · Shell · 推送 2026-03-08 · [GitHub](https://github.com/AICodeLion/agent-pack-n-go) · [官网](https://clawhub.com) · 个人维护 · 中文 README

**把 OpenClaw AI Agent 一句话克隆到新 Linux 设备的 Skill**

面向 OpenClaw 框架的 agent 迁移技能（SKILL.md + 脚本）：通过自然语言触发，Agent 经 SSH 在旧设备上打包 ~/.openclaw/、~/.claude/、~/.ssh/、crontab 等内容，rsync 传输并做三重 SHA256 校验，在新设备（Ubuntu 22.04/24.04，2 核 2GB+）安装 nvm、Node.js 22、Claude Code 并恢复配置、自动修正路径与权限，全程约 25 分钟，无云依赖。传输纯走 SSH 加密通道，rsync 不可用时降级为 scp，无免密 sudo 时优雅跳过。macOS 与 Windows (WSL) 支持正在测试中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言触发，SSH 全自动克隆配置、记忆、技能、凭证等
- 三重 SHA256 校验与纯 SSH 传输，无云/第三方依赖
- 运行时自动安装（nvm、Node.js 22、Claude Code）与路径自动修正
- tarball 保留支持随时回滚，rsync 不可用时降级 scp

## 适用场景

- 把调教好的 Agent 迁移到更快的新机器
- 保存 Agent 时间点快照并分钟级恢复
- 将 Agent 一键克隆给多个团队成员
- 本地开发后部署到云端生产环境

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6:  OpenClaw
> L126: ├── SKILL.md                      # Agent 工作流与指令定义
> L133: - OpenClaw — 本 Skill 所基于的 AI Agent 框架

## 星数曲线

```mermaid
xychart-beta
    title "AICodeLion/agent-pack-n-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-27 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e2a565bf3123` · [字段定义](../../DATASET.md)*
