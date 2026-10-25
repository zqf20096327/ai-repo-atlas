# OuterSpacee/claude-emotion-prompting

⭐ 74 · MIT · 推送 2026-04-03 · [GitHub](https://github.com/OuterSpacee/claude-emotion-prompting) · 个人维护

**基于 Anthropic 情绪向量研究的 Claude 提示词与配置模板库**

将 Anthropic 2026 年 4 月论文《Emotion Concepts and their Function in a Large Language Model》的研究发现转化为可直接使用的提示词工具包：提供 7 条提示原则（如允许失败、分解检查点、邀请透明）、5 个系统提示词、4 个 CLAUDE.md 项目配置及自建模板。面向通过聊天、API 或 Claude Code 使用 Claude 的用户，无需机器学习背景。使用方式为复制粘贴或放入项目根目录，无需安装。研究仅基于 Claude Sonnet 4.5，作者声明结果未必适用于其他模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 条原则，每条映射到论文中的具体发现
- 提供 5 个场景化系统提示词（通用/编码/研究/创作/代码审查）
- 4 个 CLAUDE.md 配置变体供 Claude Code 项目使用
- 附论文摘要与详细批注文档

## 适用场景

- 在日常对话或 API 调用中直接套用系统提示词
- 为 Claude Code 项目选择合适的 CLAUDE.md 配置
- 按模板构建适合自己工作流的提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: This repo turns those findings into prompts, system configurations, and workflows you can use today.
> L9: **Who this is for:** Anyone who uses Claude — through chat, the API, or Claude Code — and wants more honest, reliabl
> L59: Grab one from `examples/system-prompts/` and paste it into your Claude conversation or API call:

## 星数曲线

```mermaid
xychart-beta
    title "OuterSpacee/claude-emotion-prompting 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 72 --> 75
    line [73, 74, 74]
```

2026-10-18 73 → 2026-10-25 74（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c0f01cae5ed1` · [字段定义](../../DATASET.md)*
