# vishnupriyanpr/Terminal-pal

⭐ 21 · Python · Apache-2.0 · 推送 2026-02-05 · [GitHub](https://github.com/vishnupriyanpr/Terminal-pal) · 个人维护

**终端多 AI 助手：开发者在命令行提问、生成与分析代码**

基于 Python 的终端 AI 助手应用，面向开发者：在命令行中以 /ask、/chat、/generate、/explain 等命令获取 AI 回答，支持 @文件 附加上下文或自动扫描项目，并内置 /scan、/lint、/test、/docs 等项目分析与开发工具，以及主题系统、会话统计（token/成本/速度）和 PDF 导出。可接入 OpenAI、Claude、Gemini、Groq、Mistral 的 API key 或使用本地 Ollama 模型，通过 /setup 向导选择。以 git clone 加 pip 安装依赖的方式从源码运行，需配置 API key。

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

- 多提供商接入：OpenAI / Claude / Gemini / Groq / Mistral / Ollama（本地）
- @文件 附加上下文与项目自动扫描、tree/metrics/deps 分析命令
- 会话统计 token、成本、速度，支持 PDF/报告/日志导出
- 四种主题与 setup 向导，API key 本地存储、无遥测

## 适用场景

- 在终端里快速提问、生成样板代码或优化指定文件
- 让 AI 结合项目上下文做代码分析、解释与调试
- 对比使用云端 API 与本地 Ollama 模型并跟踪用量成本

## 场景标签

`AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: AI Terminal Pal isn't your typical CLI toy... — it's a full-blown developer productivity engine built into your ter
> L20: - 🤖 **Multi-AI Support:** GPT-4o, Claude 3, Gemini 1.5, Mistral, Groq Llama3, Ollama, and more

## 星数曲线

```mermaid
xychart-beta
    title "vishnupriyanpr/Terminal-pal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3bb702af52b7` · [字段定义](../../DATASET.md)*
