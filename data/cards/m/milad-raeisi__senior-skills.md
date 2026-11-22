# milad-raeisi/senior-skills

⭐ 4 · Python · MIT · 推送 2026-11-18 · [GitHub](https://github.com/milad-raeisi/senior-skills) · 个人维护

**为编码 Agent 安装 15 条资深工程师判断技能的命令行工具**

通过 npx 一条命令，检测本机的 Claude Code、Codex、Cursor、Gemini CLI、Copilot、OpenCode、Windsurf 等编码 Agent，并将 15 个 Agent Skills 格式的技能写入各 Agent 的 skills 目录，覆盖状态机排查、开源先例调研、Bug 分级、任务收尾、CI 审计等场景；安装不覆盖已有技能，更新前自动备份，无依赖、无网络调用。也提供 Claude Code plugin、open skills CLI、Gemini 扩展、安装脚本与纯 prompt 粘贴等替代方式。

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

- 15 个 Agent Skills 开放标准格式的技能，可按 --only 选择安装
- npx 一条命令检测并写入多个 Agent 的技能目录，update 前自动备份
- 安装器为单一可读文件，无依赖、不收集数据、无自身网络调用
- 无 Agent 时可直接粘贴 prompts/the-senior-five.md 中的 prompt

## 适用场景

- 给本机多个编码 Agent 一次性补齐资深工程师的判断类技能
- 团队通过 --dir 把技能装入项目目录并用 git 共享
- 用 ci-auditor 技能拆解仓库 CI 各阶段耗时并先出报告

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **15 Agent Skills that give Claude Code, Codex, Cursor, Gemini CLI, and Copilot the judgment of a staff engineer:**
> L10:  Agent Skills open standard
> L42:  Step 1, install: npx senior-skills. Step 2, update: npx senior-skills@latest update.

## 星数曲线

```mermaid
xychart-beta
    title "milad-raeisi/senior-skills 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-19", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-18 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `75084df21bb3` · [字段定义](../../DATASET.md)*
