# Michal1993r/ai-helper.wezterm

⭐ 39 · Lua · MIT · 推送 2026-03-13 · [GitHub](https://github.com/Michal1993r/ai-helper.wezterm) · 个人维护

**WezTerm 插件：在终端里向 AI 询问 CLI 命令帮助**

面向 WezTerm 用户的 Lua 插件：按快捷键唤起输入框，用自然语言询问 CLI 问题，AI 返回解释与可直接执行的命令。支持四种提供方：LM Studio（本地默认）、Google Gemini、Ollama（本地/远程）及任意 OpenAI API 兼容的 HTTP 服务。可配置自定义系统提示词、快捷键、超时，并可把终端 pane 历史共享给 AI 以获得上下文感知的建议。Google Gemini 路线需 luarocks 安装 dkjson 库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种提供方：LM Studio / Gemini / Ollama / OpenAI 兼容 HTTP 服务
- AI 回复由解释文本与可执行命令组成，命令直接出现在终端
- 可选共享 pane 历史给 AI，提升上下文感知与命令修正能力
- 可配置系统提示词、快捷键、超时、共享行数等选项

## 适用场景

- 终端里忘记命令时快速询问 AI 获得可执行命令
- 把终端上下文交给 AI 修正或解释之前的命令
- 在公司 AI 政策限制下用本地模型（LM Studio/Ollama）获得 CLI 帮助

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L4: And so here it is: a very simple WezTerm plugin that lets you ask an AI for CLI help using multiple providers: LM St
> L60: Press `Cmd+I` (default keybinding), type your question, get help.

## 星数曲线

```mermaid
xychart-beta
    title "Michal1993r/ai-helper.wezterm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b0b516580465` · [字段定义](../../DATASET.md)*
