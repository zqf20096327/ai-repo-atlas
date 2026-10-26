# haddock-development/claude-reflect-system

⭐ 383 · Python · 推送 2026-01-17 · [GitHub](https://github.com/haddock-development/claude-reflect-system) · [官网](https://huggingface.co/mindchain) · 个人维护

**让 Claude Code 从用户纠正中持久学习、不再重犯的技能系统**

面向 Claude Code CLI 用户的自学习技能系统：通过 /reflect 命令或 Stop 钩子分析会话中的纠正、认可与建议，按 HIGH/MEDIUM/LOW 三级置信度提取信号，自动更新 ~/.claude/skills/ 下的技能文件，实现跨会话的持久记忆。每次变更带时间戳备份、YAML 校验、人工审批与自动回滚，并通过 Git 记录全部学习历史。纯 Python 实现，依赖仅 PyYAML，数据全部本地存储；需 Python 3.8+、Git 与 Claude Code，macOS/Linux 下运行（Windows 未测试）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级置信度信号检测：纠正→Critical Corrections，认可→Best Practices，建议→Considerations
- 安全更新机制：时间戳备份、YAML 校验、人工审批、自动回滚
- Git 集成记录全部学习历史，技能可经 Git 在团队间共享
- 支持手动 /reflect 与 Stop 钩子自动反思两种模式

## 适用场景

- 教 Claude Code 记住我的工具偏好（如用 uv 替代 pip、pytest 替代 unittest）
- 把团队编码规范沉淀为可共享的技能，新成员直接继承
- 对 AI 助手重复犯同样的错感到疲惫时建立持久纠正记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: **Reflect** is a revolutionary **self-learning AI system** for Claude Code that enables **automatic skill improveme
> L82: The core learning engine with:
> L88: - ✅ Auto-reflection via hooks

## 星数曲线

```mermaid
xychart-beta
    title "haddock-development/claude-reflect-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 382 --> 384
    line [383, 383]
```

2026-10-18 383 → 2026-10-26 383（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `8964f96467a2` · [字段定义](../../DATASET.md)*
