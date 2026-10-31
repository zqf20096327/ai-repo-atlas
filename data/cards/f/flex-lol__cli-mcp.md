# flex-lol/cli-mcp

⭐ 15 · Python · Apache-2.0 · 推送 2026-03-27 · [GitHub](https://github.com/flex-lol/cli-mcp) · 个人维护

**终端里的 LLM 提问与 MCP 客户端 CLI**

命令行程序，用于发送 LLM 提示并作为 Model Context Protocol (MCP) 客户端连接任意 MCP 兼容服务器，自称是 Claude Desktop 之外的替代客户端。支持配置任意 LLM 提供商（如 OpenAI、Groq 或经 llama 使用本地模型）。功能包括管道输入、图像输入、提示模板、工具调用确认、会话延续、剪贴板读写等。经 pip 安装，通过 ~/.llm/config.json 配置。剪贴板功能在 Linux 上依赖 xclip 等系统工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 作为 MCP 客户端在终端连接任意 MCP 兼容服务器
- 支持任意 LLM 提供商（OpenAI/Groq/本地 llama 模型）
- 管道输入图像文件配合多模态 LLM 分析
- 工具调用确认机制与提示模板、会话延续

## 适用场景

- 在终端向 LLM 提问并调用 MCP 服务器提供的工具
- 在 bash 脚本中调用 LLM 获取仅含结论的输出
- 把剪贴板文本或截图发给多模态 LLM 分析

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A simple CLI program to run LLM prompt and implement Model Context Protocol (MCP) client.
> L7: This act as alternative client beside Claude Desktop. Additionally you can use any LLM provider like OpenAI, Groq, o

## 星数曲线

```mermaid
xychart-beta
    title "flex-lol/cli-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `82c550280a47` · [字段定义](../../DATASET.md)*
