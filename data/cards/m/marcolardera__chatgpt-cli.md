# marcolardera/chatgpt-cli

⭐ 475 · Python · MIT · 推送 2025-11-02 · [GitHub](https://github.com/marcolardera/chatgpt-cli) · 个人维护

**终端里与 ChatGPT 对话的 Python 命令行客户端**

Python 编写的命令行 ChatGPT 客户端，通过官方 OpenAI API（或 Azure 作为可选供应商）对话。提供 API Key 三种配置方式（命令行/环境变量/config.yaml）、多模型选择（默认 gpt-4o）、Markdown 渲染含代码块高亮、会话保存与恢复、多文件上下文注入、UNIX 管道非交互模式、JSON 模式、多行输入与代码块复制命令。安装需 Python 3.10+，通过 pip 从 GitHub 仓库安装，Linux 受限环境可用 pipx。面向在终端使用 ChatGPT 的终端用户与脚本编写者。

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

- 支持 OpenAI 与 Azure 两种 API 供应商，默认 gpt-4o，可配置多种模型
- Markdown 渲染、代码块标记与 /copy 复制命令
- 会话历史保存与 --restore 恢复，多文件 --context 上下文注入
- --non-interactive 管道模式可嵌入 shell 脚本，--json 强制 JSON 输出

## 适用场景

- 在终端直接与 ChatGPT 对话并跟踪 token 花费
- 把代码或文本文件作为上下文让模型解释、改写或翻译
- 在 shell 脚本管道中调用 ChatGPT 处理文本

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: Simple script for chatting with ChatGPT from the command line, using the official API (Released March 1st, 2023). It
> L60: You can set the supplier as `openai` (the default) or `azure` in the config.yaml. Remember to set the parameters co
> L64: ChatGPT CLI, by default, uses the standard `gpt-4o` model. In order to use other ChatGPT models, edit the `model` p

## 星数曲线

```mermaid
xychart-beta
    title "marcolardera/chatgpt-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 474 --> 476
    line [475, 475]
```

2026-10-18 475 → 2026-10-27 475（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8a60239ee0c0` · [字段定义](../../DATASET.md)*
