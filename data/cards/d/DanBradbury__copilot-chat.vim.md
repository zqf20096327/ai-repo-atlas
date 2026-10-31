# DanBradbury/copilot-chat.vim

⭐ 134 · Vim Script · MIT · 推送 2026-01-17 · [GitHub](https://github.com/DanBradbury/copilot-chat.vim) · 个人维护

**在 Vim 内使用 GitHub Copilot Chat 的对话插件**

面向 Vim 9.0+ 用户的 Copilot Chat 客户端插件，需有效的 GitHub Copilot 订阅，通过设备码流程完成注册后即可在 Vim 分屏窗口中与 Copilot 对话。提供模型选择、聊天历史保存/加载（JSON 文件）、选区代码发送、`#file:` 文件路径补全与 `/tab all` 标签展开宏、`config.json` 提示模板及窗口位置等配置项。安装支持 vim-plug、Vundle、Pathogen、Vim 8+ 原生包等方式。

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

- 在 Vim 分屏窗口内与 GitHub Copilot 对话，支持模型选择
- 聊天历史保存/加载，以 JSON 存储于 ~/.vim/copilot-chat/history/
- 选区代码添加到聊天、#file: 文件补全与 /tab all 宏
- config.json 提示模板与多项全局变量配置

## 适用场景

- 在 Vim 中直接向 Copilot 提问而不切换窗口
- 把选中的代码片段发给 Copilot 解释或修改
- 用提示模板复用常用提问

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Copilot Chat functionality without having to leave Vim.
> L80: 4. Start chatting with Copilot (`:CopilotChatOpen`, `:CopilotChat simple question`, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "DanBradbury/copilot-chat.vim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-31 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0081f733088e` · [字段定义](../../DATASET.md)*
