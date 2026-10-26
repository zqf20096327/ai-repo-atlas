# wwenj/zu-article-image-skill

⭐ 57 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/wwenj/zu-article-image-skill) · 个人维护 · 中文 README

**给 Markdown 文章自动配图的 Agent Skill：两步生成插图并回写正文**

面向 Claude Code / Codex 的技能包，分两层为 Markdown 文章生成语义配图：先依据文章结构在正文插入可检查、可编辑的 article-illustration Prompt 标签（含 preset/type/style/palette 等元数据，内置 8 组 preset 与 7 种画面风格），用户确认后按标签生成图片保存到 imgs/ 并把图片引用回插原位。文章 Markdown 是唯一状态源，不产生额外状态文件；脚本 article_tags.py 提供 scan/sync 命令做确定性扫描与回插，并定义四种插图状态。安装方式为复制目录到 Skill 目录或让 Agent 自动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段流程：先插入可编辑 Prompt 标签，确认后再生图回插
- 内置 8 组 preset、6 类信息结构、7 种画面风格与 6 套色彩语义
- article_tags.py 提供 scan/sync 命令，状态机含 needs_generation 等 4 种状态
- 文章 Markdown 是唯一状态源，不创建额外计划或状态文件

## 适用场景

- 给中文技术文章、教程、观点长文自动规划配图
- 在文章内直接维护配图 Prompt，按需更换 preset 或 style 重新生成
- 为 Markdown 草稿补充流程图、架构图、概念图、对比图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L123: ## 安装到 Claude Code / Codex
> L127: - Claude Code：复制到 `~/.claude/skills/zu-article-image-skill/`

## 星数曲线

```mermaid
xychart-beta
    title "wwenj/zu-article-image-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 56 --> 59
    line [58, 57, 57]
```

2026-10-18 58 → 2026-10-26 57（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c3606b581010` · [字段定义](../../DATASET.md)*
