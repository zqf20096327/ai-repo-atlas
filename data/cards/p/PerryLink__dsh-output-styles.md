# PerryLink/dsh-output-styles

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/PerryLink/dsh-output-styles) · [官网](https://perrylink.github.io/plugins/dsh-output-styles/) · 个人维护 · 中文 README

**DeepSeek Harness 插件：运行时切换模型输出风格并会话级持久化**

Claude Code outputStyles 在 DeepSeek Harness（DSH）中的对应实现：提供 /style 命令在会话内切换输出风格，选择持久化于 output_style 存储域（按 sessionId 键控），通过 systemPrompt.section() 注入在每次提示词组装时生效。内置 concise、explanatory、formal、learning、proactive、step-by-step 六种风格（Markdown 文件+frontmatter），兼容 Claude Code outputStyles JSON，支持分层 stylesDir、热重载、按工具/会话的渲染规则与 /transcript 会话导出。通过 dsh plugin 命令安装，Node ≥22.19 或 ≥24。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /style 命令运行时切换风格，按 sessionId 会话级持久化并跨重启保留
- 系统提示注入（systemPrompt.section），风格体按 maxStyleChars 预算截断
- Claude Code 对齐：outputStyles JSON 兼容、分层 stylesDir、热重载、项目默认风格回退
- 渲染器注册表（output.render.*）与 /transcript 会话导出（Markdown/HTML）

## 适用场景

- 在 DSH 会话中让模型回答更简洁或更详尽而不改代码
- 按工具类型自动应用渲染规则（如 bash 输出用 concise）
- 把会话渲染导出为 Markdown/HTML 文档

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L63: `dsh-output-styles` is the Claude Code `outputStyles` equivalent for DeepSeek Harness: a `/style` command that swit
> L7: **Claude Code `outputStyles` for DeepSeek Harness** — switch the model's output style at runtime, per session, durab

## 星数曲线

```mermaid
xychart-beta
    title "PerryLink/dsh-output-styles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `961174be1b62` · [字段定义](../../DATASET.md)*
