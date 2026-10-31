# gauravvij/GithubRepoAgent

⭐ 14 · Python · 推送 2026-06-08 · [GitHub](https://github.com/gauravvij/GithubRepoAgent) · [官网](https://heyneo.com) · 个人维护

**用 LLM 分析任意 GitHub 仓库并回答代码库问题的终端风 agent**

Python/Flask Web 应用：粘贴公开 GitHub URL 后自动克隆仓库、递归扫描代码文件，通过并行 map-reduce 分块摘要与分层归并生成结构化架构报告（目录结构、模块交互、依赖关系、数据流等），随后可在多轮对话界面追问代码库问题。LLM 层支持多提供商：OpenRouter（默认）、MiniMax 或任意 OpenAI 兼容端点，经 .env 配置；前端为终端风格深色 UI，SSE 流式输出进度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 克隆并递归扫描任意公开 GitHub 仓库，生成结构化架构报告
- 并行 map-reduce 分块分析，token 感知的分层归并（单次调用上限 100k tokens）
- 多轮对话式追问代码库问题，保留完整报告上下文
- 多 LLM 提供商支持：OpenRouter / MiniMax / 任意 OpenAI 兼容端点

## 适用场景

- 快速了解一个陌生开源仓库的架构与模块关系
- 针对他人代码库提问，寻找功能缺口与改进点
- 代码审查前的整体结构梳理

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: A terminal-styled AI agent that analyzes any GitHub repository and answers questions about its codebase. Point it at
> L26: - **LLM**: Multi-provider support — OpenRouter (default), MiniMax, or any OpenAI-compatible endpoint

## 星数曲线

```mermaid
xychart-beta
    title "gauravvij/GithubRepoAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4e5a0516d78e` · [字段定义](../../DATASET.md)*
