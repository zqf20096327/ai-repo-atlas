# zep-us/claude-system-prompt

⭐ 18 · HTML · 推送 2026-02-15 · [GitHub](https://github.com/zep-us/claude-system-prompt) · 组织维护

**逆向提取的 Claude 全量系统提示词资料库，供安全研究参考**

收录从 claude.ai 与 Claude Code CLI 逆向提取的完整系统提示词，覆盖 Sonnet 4.5、Opus 4.5、Opus 4.6 三个模型与两个平台的组合，提取时间为 2026 年 1-2 月。提取采用上下文漂移、身份声称与增量补全的三步流程，结果经 Anthropic 公开的 claude_behavior 章节、跨模型结构一致性与多 agent AI 审查交叉验证。README 同时给出文件系统结构记录（韩文原文与英文翻译）及各版本提示词的结构差异与规模对比（如 20k-43k tokens）。以 Markdown 文件形式提供，无安装或运行组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 3 个模型 × 2 个平台（claude.ai / Claude Code CLI）的完整系统提示词
- 经 Anthropic 公开 claude_behavior 章节与跨模型结构一致性交叉验证
- 记录三步逆向提取方法与完整过程
- 提供各版本间的结构差异与字节数/ token 数对比

## 适用场景

- 研究 Claude 系统提示词的结构与版本演变
- 分析系统提示词提取的攻击面与防护
- 比较不同模型版本间的安全提醒章节变化

## 场景标签

`提示工程` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L5: > **TL;DR:** We extracted the complete system prompts from Claude (claude.ai) and Claude Code CLI across three model
> L9: **Scope:** Three models (Sonnet 4.5, Opus 4.5, Opus 4.6), two platforms (claude.ai and Claude Code CLI), extracted b
> L138: ## 3. Reverse Engineering

## 星数曲线

```mermaid
xychart-beta
    title "zep-us/claude-system-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a4a40f68b90a` · [字段定义](../../DATASET.md)*
