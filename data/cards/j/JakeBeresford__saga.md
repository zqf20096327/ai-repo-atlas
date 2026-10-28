# JakeBeresford/saga

⭐ 20 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/JakeBeresford/saga) · [官网](https://jakeberesford.github.io/saga/) · 个人维护

**把 git diff 或 PR 生成分章叙述式审查文档的 CLI**

面向代码审查场景的 Python CLI 工具：读取本地分支 diff 或 GitHub PR，将整个变更切分为有序的章节故事，每章用自然语言叙述并附对应代码片段，输出为单文件内联 HTML（含 diff2html 与语法高亮），可离线打开、邮件发送或静态托管。LLM 提供方支持 Anthropic、OpenAI、OpenRouter、本地模型及 Claude Code CLI。通过 uvx 免安装运行，或用 uv/pipx 安装。

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

- 将 diff 或 PR 切分为分章叙述式审查导览
- 输出单文件内联 HTML（含 diff2html 与语法高亮），可离线打开
- 支持分支与 GitHub PR 两种输入
- LLM 提供方支持 Anthropic/OpenAI/OpenRouter/本地模型/Claude Code CLI

## 适用场景

- 审查大规模 AI 生成的 PR 时获得分章讲解
- 为团队的 PR 生成可离线分享的 HTML 审查文档
- 在 CI 中按 PR 自动生成审查导览

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L10: Saga turns that diff into a **chapter-by-chapter guided tour**. The whole change partitioned into an ordered story,
> L48: - Providers: Anthropic, OpenAI, OpenRouter, local LLMs, and the Claude Code CLI.

## 星数曲线

```mermaid
xychart-beta
    title "JakeBeresford/saga 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fbfdc16191c5` · [字段定义](../../DATASET.md)*
