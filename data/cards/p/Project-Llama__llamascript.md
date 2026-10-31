# Project-Llama/llamascript

⭐ 28 · Python · Apache-2.0 · 推送 2025-11-14 · [GitHub](https://github.com/Project-Llama/llamascript) · [官网](https://pypi.org/project/llamascript/) · 个人维护

**基于 Ollama 的无代码 AI 聊天 DSL：用 .llama 脚本描述对话**

面向不写代码的用户的 AI 聊天工具：用户在 .llama 文件中用 use/prompt/system/chat/save 等函数声明所选模型（如 llama3）、提示与对话流程，再通过 llamascript 命令运行脚本，由 Ollama 后端提供模型推理。以 pip 包形式安装，另有 VS Code 扩展提供下载（徽章可见），采用 Apache 2.0 许可。README 较简短，仅展示基础语法与一个示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .llama 脚本语法：use/prompt/system/chat/save 等函数
- 通过 llamascript 命令运行脚本
- pip 安装，配套 VS Code 扩展

## 适用场景

- 用脚本描述模型选择与提示词，快速搭建 AI 对话
- 保存配置以便复用模型对话流程

## 场景标签

`提示工程` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L10: LlamaScript is a no-code AI chatbot using Ollama.
> L23: To use LlamaScript, create a `.llama` file and write your script. Here are a few functions you can use:

## 星数曲线

```mermaid
xychart-beta
    title "Project-Llama/llamascript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4c3aebb43950` · [字段定义](../../DATASET.md)*
