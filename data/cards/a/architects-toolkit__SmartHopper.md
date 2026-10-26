# architects-toolkit/SmartHopper

⭐ 33 · C# · LGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/architects-toolkit/SmartHopper) · [官网](https://smarthopper.xyz) · 组织维护

**给 Grasshopper3D 设计师的 AI 组件与助手插件（100+ 工具，8 家模型商）**

Rhino/Grasshopper 的 AI 插件：提供上下文感知的对话助手（可读取画布组件、搜索 McNeel/Ladybug 论坛与网页）与 100+ AI 组件，覆盖脚本生成（Python/C#/VB.NET/IronPython）、图像生成与分析、音频转录与合成、文件转 Markdown，以及用 GhJSON 纯文本格式对 Grasshopper 定义做 diff/patch。AI 返回原生 Grasshopper 数据类型。支持 OpenAI/Anthropic/Gemini/Mistral/DeepSeek/OpenRouter 及本地 Ollama/LocalAI，需 Rhino 8.0+ 与 API key 或本地服务器，经 Rhino Package Manager 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上下文感知 AI 助手可读取画布并搜索论坛/网页
- 生成 Python/C#/VB.NET/IronPython 脚本组件
- 创建并维护 GhJSON：Grasshopper 定义纯文本格式，可 diff/patch/版本控制
- AI 输出为原生 Grasshopper 数据类型（文本/数字/图像/音频/JSON）

## 适用场景

- 在 Grasshopper 参数化流程里直接调用 LLM、图像与音频模型
- 让 AI 代写脚本组件并搭建/整理 Grasshopper 定义
- 用 GhJSON 格式对设计定义做版本管理与 AI 编辑

## 场景标签

`AI 助手` `代码生成` `图像生成` · 领域:编码与开发

## 证据(README 行号)

> L17: SmartHopper brings a context-aware AI assistant and a suite of AI-powered components into Grasshopper3D. It gives d
> L26: - **Use the AI provider you prefer.** OpenAI, Anthropic, Google Gemini, Mistral, DeepSeek, OpenRouter, or run local

## 星数曲线

```mermaid
xychart-beta
    title "architects-toolkit/SmartHopper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5a416bc4761d` · [字段定义](../../DATASET.md)*
