# gostak-dd/second-look-code-review

⭐ 5 · HTML · MIT · 推送 2026-11-01 · [GitHub](https://github.com/gostak-dd/second-look-code-review) · 个人维护

**面向编码 Agent 的技能：把分支或 PR 变成浏览器中的代码审查指南**

一个 Agent Skill：让支持 skills 的编码代理（Claude Code、Codex、Cursor 等）读取分支 diff，按行为而非目录分章、为每章标注风险，并运行一份 AI 代码检查清单（如层层重试、吞错、只测 mock 的测试等），把发现钉到具体行。Agent 只写一个 guide.json，由零依赖的 Node 脚本渲染成单一自包含 HTML 页面。支持键盘浏览、逐行评论、导出评论回贴给 Agent 修复，并做增量复审。需 Node.js 18+ 与 git，GitHub CLI 为可选；一切本地运行，页面无网络请求。

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

- 按行为分章 + 每章风险等级，指导审查节奏
- AI 代码常见错误检查清单，发现钉到具体行
- 评论导出回贴 Agent 修复，复审只显示上次审查后的变更
- Agent 仅生成 guide.json，渲染脚本零依赖、页面无网络请求

## 适用场景

- 让编码代理帮我审查一个待合并的分支
- 审查 AI 生成的代码，按检查清单捕捉代理常犯的错误
- 标记已读文件后增量复审，只看新变更并跟踪评论处理结果

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: An Agent Skill that turns a branch or pull request into an interactive code review guide in your browser. Works with
> L7: - **An AI-code checklist** that catches the mistakes coding agents keep making: runaway LLM output, stacked retries,
> L15: - A coding agent that supports Agent Skills and can run shell commands

## 星数曲线

```mermaid
xychart-beta
    title "gostak-dd/second-look-code-review 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-19", "2026-11-25"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-25 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d48c6813069f` · [字段定义](../../DATASET.md)*
