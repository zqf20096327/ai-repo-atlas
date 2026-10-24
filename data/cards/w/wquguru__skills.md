# wquguru/skills

⭐ 94 · HTML · 推送 2026-10-07 · [GitHub](https://github.com/wquguru/skills) · [官网](https://wquguru.github.io/skills) · 个人维护

**面向 Claude Code/Codex/Grok 的实用 Agent 技能合集**

自研 Agent Skills 的公开 monorepo，每个技能以 SKILL.md 文件夹形式提供，通过 `npx skills add` 单独安装，安装回路将技能链接进 Claude Code、Codex 与 Grok 的技能目录。收录技能包括 Claude 5 与 GPT-5.6 的模型路由/成本优化最佳实践、工程师日常英语训练、Pi Agent 配置（DeepSeek/Ant-Ling 提供商）、Linux 主机 CPU 审计、YouTube 下载与字幕烧制。第三方技能通过 external.yml + just vendor 单独引入，不入库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个技能为含 SKILL.md 的文件夹，可用 npx skills add 单独安装
- Justfile 自含：add/remove/status/vendor，将技能 symlink 到三类 agent 目录
- 第三方技能经 external.yml vendor 引入，仓库仅提交声明与锁定文件
- 覆盖模型路由最佳实践、英语训练、agent 配置、系统审计、视频处理等场景

## 适用场景

- 为 Claude Code/Codex/Grok 安装即用的实用技能
- 在 Claude 5 / GPT-5.6 任务中做模型选型与成本优化
- 下载 YouTube 视频并烧制翻译字幕

## 场景标签

 · 领域:AI agent 技能/开发者工具

## 证据(README 行号)

> L6: A small collection of practical Agent Skills.
> L12: **Catalog:** self-authored skills live under `skills/` (see also the

## 星数曲线

```mermaid
xychart-beta
    title "wquguru/skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-24 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1398715d6e93` · [字段定义](../../DATASET.md)*
