# nazdridoy/ngpt

⭐ 48 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/nazdridoy/ngpt) · [官网](https://nazdridoy.github.io/ngpt/) · 个人维护

**终端里的多 LLM 客户端：对话、生成代码与 git 提交信息**

Python 编写的命令行工具，接入 OpenAI、Ollama、Groq、Claude、Gemini 及任意 OpenAI 兼容端点，支持单参数切换 provider 与流式输出。功能包括交互式聊天（含会话保存/加载）、代码生成、OS 感知的 shell 命令生成与执行、文本改写、从 git diff 生成规范化提交信息、Web 搜索增强、stdin 管道处理（{} 占位符）与可复用自定义 AI 角色。通过 pip 安装，需 Python 3.8+，采用 JSON 配置文件支持多配置切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一参数在 OpenAI/Ollama/Groq/Claude/Gemini 等 provider 间切换
- 从 git diff 生成规范化提交信息
- OS 感知的 shell 命令生成并可选择执行
- stdin 管道 {} 占位符与 Web 搜索增强

## 适用场景

- 在终端直接与多家 LLM 对话并流式查看输出
- 让 AI 根据代码改动生成规范化 git 提交信息
- 用自然语言生成并执行当前系统对应的 shell 命令
- 管道传入文件或命令输出做摘要、改写与解释

## 场景标签

`聊天机器人` `代码生成` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L16: 🤖 **nGPT** - A lightning-fast CLI tool that brings any OpenAI-compatible LLM (OpenAI, Ollama, Groq, Claude, Gemini)
> L24: - 🔄 **API Flexibility**: Works with OpenAI, Ollama, Groq, Claude, Gemini, and any OpenAI-compatible endpoint
> L36: - 📑 **Git Commit Messages**: AI-powered generation of conventional, detailed commit messages from git diffs

## 星数曲线

```mermaid
xychart-beta
    title "nazdridoy/ngpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c46084b1632d` · [字段定义](../../DATASET.md)*
