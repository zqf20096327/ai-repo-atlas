# malav2110/explain-diff-html

⭐ 16 · HTML · MIT · 推送 2026-10-27 · [GitHub](https://github.com/malav2110/explain-diff-html) · [官网](https://malav2110.github.io/explain-diff-html/) · 个人维护

**把 PR/代码 diff 生成为讲解逻辑流程的单页 HTML 的 agent 技能**

面向 Claude Code、Codex、Cursor 等 coding agent 的技能（SKILL.md 格式）：读取 pull request、分支或 commit 区间的 diff 及周边代码、调用方与提交记录，生成一个四段式（背景/直觉/按请求路径排序的代码走读/五题测验）的自包含 HTML 讲解页，含校验过的 file:line 锚点与 Mermaid 图（需 CDN）。通过 npx skills add 安装，可达 79 个 agent；也可手动复制目录。依赖 git、gh、node（Mermaid 校验），命令为 POSIX shell，Windows 需 WSL/Git Bash。仅讲解不评判，输出是 diff 的静态快照。给需要在评审前理解大型 PR、onboarding 或复盘的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按代码逻辑流（request→handler→service）而非 Git 文件顺序组织讲解
- 生成自包含 HTML 单页：CSS/JS 内联、离线可读（Mermaid 图除外）、适配明暗主题
- file:line 锚点在目标 ref 上经只读校验，附五题交互测验
- npx skills add 一次安装覆盖 79 个 agent（Claude Code/Codex/Cursor 等）

## 适用场景

- 评审大型或机器生成的 PR 前先读懂变更的连接方式
- 新人通过讲解历史关键 PR 的页面 onboarding 到代码库
- 配合事故报告/调查笔记，把故障与修复补丁关联成复盘材料

## 场景标签

 · 领域:开发者工具/代码理解

## 证据(README 行号)

> L3: An agent skill that turns a code change into one self-contained HTML page that
> L30: It was written as a Claude Code skill, and `SKILL.md` keeps that format. Other
> L211: `skills/explain-diff-html/SKILL.md`. It copies that directory and nothing else,

## 星数曲线

```mermaid
xychart-beta
    title "malav2110/explain-diff-html 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `97abd5ce9ec4` · [字段定义](../../DATASET.md)*
