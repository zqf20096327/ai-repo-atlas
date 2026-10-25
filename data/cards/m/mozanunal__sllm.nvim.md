# mozanunal/sllm.nvim

⭐ 113 · Lua · Apache-2.0 · 推送 2026-02-08 · [GitHub](https://github.com/mozanunal/sllm.nvim) · 个人维护

**Neovim 内与 LLM 聊天与补全的 lua 插件**

基于 Simon Willison 的 llm CLI 封装的 Neovim 插件（纯 Lua）：在编辑器内进行流式聊天、光标处代码补全，管理文件/选区/URL/诊断/命令输出作为上下文，提供 agentic 模式（bash、read、write 等 Python 函数工具）、YAML 模板/模式系统、斜杠命令、历史浏览与 token/成本统计。需先安装 llm CLI 并配置 provider 的 API key，插件本身经 lazy.nvim 安装，默认模型如 claude-3-5-sonnet。

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

- 流式聊天与光标处行内补全
- 多来源上下文管理（文件、选区、URL、诊断、shell 输出）
- agentic 模式提供 bash/read/write/edit/grep 函数工具
- 模式为 YAML 文件、工具为 Python 函数，可自定义

## 适用场景

- 在 Neovim 中直接向 LLM 提问并引用多文件上下文
- 在编辑器内运行带工具调用的 agentic 工作流
- 查看 token 用量与成本并继续历史会话

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L6: A lightweight Neovim wrapper for Simon Willison's
> L7: `llm` CLI. Chat with LLMs, run agentic
> L8: workflows, and complete code without leaving your editor.

## 星数曲线

```mermaid
xychart-beta
    title "mozanunal/sllm.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-25 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `c7d0365d7ff9` · [字段定义](../../DATASET.md)*
