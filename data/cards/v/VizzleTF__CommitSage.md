# VizzleTF/CommitSage

⭐ 52 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/VizzleTF/CommitSage) · [官网](https://marketplace.visualstudio.com/items?itemName=VizzleTF.geminicommit) · 个人维护

**用 AI 从 Git 改动生成 commit 信息的 VS Code 扩展**

VS Code 扩展，读取暂存的 diff，经用户选择的 AI 提供商生成 commit 信息；支持 11 个提供商（Gemini、OpenRouter、Groq、Anthropic、OpenAI、DeepSeek、xAI、Codestral、Mistral、Ollama 及任意 OpenAI 兼容端点）。提供 11 种 commit 格式与 10 种输出语言，内置 commitlint 校验与自动修复、可选自动提交/推送、混合改动按文件分组拆分为多个提交（需确认后执行）。隐私方面：API key 存于 VS Code SecretStorage，.env/密钥文件内容不发送，diff 中已知密钥格式做掩码；本地 Ollama/自托管端点可留在自有网络。需 VS Code 1.93.0+ 与 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个 AI 提供商可选，含 Ollama 与任意 OpenAI 兼容自托管端点
- 11 种 commit 格式与 10 种输出语言，支持 commitlint 校验自动修复
- 混合改动按文件分组拆分为多个提交，执行前展示计划并需确认
- 敏感文件排除与已知密钥格式掩码，密钥存于 VS Code SecretStorage

## 适用场景

- 我不想手写 commit 信息，让 AI 按 conventional 格式生成
- 把一次混合改动自动拆成多个有逻辑的提交
- 在私有网络用 Ollama 生成 commit 信息，避免代码外发

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: Commit Sage is a VS Code extension that writes Git commit messages from your changes with an AI provider of your cho
> L37: - 11 providers: Gemini, OpenRouter, Groq, Anthropic, OpenAI, DeepSeek, xAI, Codestral, Mistral, Ollama and Custom (

## 星数曲线

```mermaid
xychart-beta
    title "VizzleTF/CommitSage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `549fd3aa4f34` · [字段定义](../../DATASET.md)*
