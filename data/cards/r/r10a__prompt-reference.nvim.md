# r10a/prompt-reference.nvim

⭐ 14 · Lua · MIT · 推送 2026-07-21 · [GitHub](https://github.com/r10a/prompt-reference.nvim) · 个人维护

**Neovim 插件：为多段代码各配提示词打包，粘贴给 LLM**

Neovim 插件，用于向 LLM 提问前的上下文整理：在可视模式选中代码，为每段选择输入一条指令，跨文件累积成一份 review，一次性复制为 XML 或 Markdown 格式的结构化消息粘贴到 LLM 对话。提供 review 面板查看与编辑已暂存条目，输出目标可选系统剪贴板或 tmux；后者可将整包粘贴进正在运行的 Claude Code 会话并回车发送（单向递交，不读取回复）。要求 Neovim 0.10+，通过 lazy.nvim/packer.nvim 安装。

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

- 跨文件选择代码并为每段附加提示词，合并为一条结构化消息
- XML 与 Markdown 两种输出格式
- tmux sink 可将 review 直接粘贴进运行中的 Claude Code 会话，找不到目标时回退剪贴板
- 提供 :PromptReferenceAdd/Review/Copy 命令与可自定义键位

## 适用场景

- 向 LLM 提问前一次性整理多处需要修改的代码与对应指令
- 把多文件的代码审查请求打包成单条消息发给 Claude Code
- 减少在编辑器与 LLM 对话间反复复制粘贴的操作

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Stage code references — each with its own **prompt** — into a review, then copy
> L8: *review*: select some code, jot the instruction for it, repeat across files, and

## 星数曲线

```mermaid
xychart-beta
    title "r10a/prompt-reference.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1cc13a402743` · [字段定义](../../DATASET.md)*
