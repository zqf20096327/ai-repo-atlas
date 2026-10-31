# frankroeder/parrot.nvim

⭐ 793 · Lua · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/frankroeder/parrot.nvim) · 个人维护

**面向 Neovim 的 LLM 文本生成插件：补全、改写与聊天**

Neovim 插件，将 LLM API 集成到文本编辑工作流中，功能为按需的代码补全/改写/追加（PrtRewrite、PrtAppend、PrtPrepend 等）以及以原生 Neovim Markdown buffer 承载的聊天会话，会话以 .md 文件持久化。提供统一 provider 系统，支持任何 OpenAI 兼容 API（OpenAI/Anthropic/Gemini/xAI/ollama 本地服务等），另经 Agent Client Protocol (ACP) 接入 Grok Build CLI 等代理后端。不提供自动 ghost-text 补全与后台隐藏请求，用户对发送内容保有控制。需 Neovim 0.11+，基于 gp.nvim 的早期 fork。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 provider 系统支持任意 OpenAI 兼容 API 与本地 ollama 服务
- PrtRewrite/PrtAppend/PrtPrepend 等命令对选区做内联生成
- 聊天以原生 Markdown buffer 进行并以 .md 文件持久化
- 经 Agent Client Protocol 接入 Grok Build CLI 等代理后端

## 适用场景

- 在 Neovim 内按需触发 LLM 改写、追加或注释选中代码
- 在编辑器内的 Markdown buffer 中与 LLM 进行持久化会话
- 通过统一配置在多家 API provider 与本地模型间切换

## 场景标签

`代码生成` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L11: parrot.nvim offers a seamless out-of-the-box experience, providing tight integration of current LLM APIs into your 
> L21: - Unified provider system supporting any OpenAI-compatible API:
> L15: The user is always under **full control** of what will be sent to the LLM (or agent) endpoint. Parrot does **not** 

## 星数曲线

```mermaid
xychart-beta
    title "frankroeder/parrot.nvim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 791 --> 794
    line [792, 793, 793]
```

2026-10-18 792 → 2026-10-31 793（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e2f08f00e808` · [字段定义](../../DATASET.md)*
