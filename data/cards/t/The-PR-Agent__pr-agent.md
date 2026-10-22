# The-PR-Agent/pr-agent

⭐ 13,555 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/The-PR-Agent/pr-agent) · [官网](https://www.pr-agent.ai)

**面向开发团队的 AI 代码审查 agent，自动审查 PR**

PR-Agent 是开源的 AI 代码审查 agent，已在 GitHub 上由 Qodo 捐赠给开源社区，现为社区维护项目，与 Qodo 商业产品相区分。核心工具包括 /describe、/review、/improve、/ask，以 PR 评论或 CLI 方式触发，每个工具使用单次 LLM 调用（约 30 秒）。支持 GitHub、GitLab、BitBucket、Azure DevOps、Gitea 平台，通过 PR Compression 策略处理大小 PR，基于 JSON 的提示词可经配置文件自定义。部署途径含 GitHub Action、CLI、Docker、自托管 webhook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 23,393 位贡献者
- 涨星:近 1 天 **+17**(自 20261016 起算)
- 平台:— · 协议:OPENAI-API / OLLAMA

## 能力要点

- /review、/improve、/describe、/ask 等工具以 PR 评论或 CLI 方式运行
- PR Compression 策略处理任意规模的 PR
- JSON 提示词经配置文件自定义审查类别与行为
- 支持 GitHub/GitLab/BitBucket/Azure DevOps/Gitea 与多种部署方式

## 适用场景

- 为仓库配置 GitHub Action 自动审查每个 PR
- 本地对指定 PR 运行 review/improve 命令
- 在自托管环境中控制代码数据的流向
- 通过评论命令向 AI 询问 PR 相关问题

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9:  This repository contains the open-source PR Agent Project.
> L12: PR-Agent is an open-source, AI-powered code review agent and a community-maintained legacy project of Qodo. It is d
> L72: - **AI Models**: OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any other model reachable thro

## 星数曲线

```mermaid
xychart-beta
    title "The-PR-Agent/pr-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 13416 --> 13539
    line [13426, 13457, 13529]
```

2026-10-18 13,426 → 2026-10-22 13,529（+103）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `24b508d8cd47` · [字段定义](../../DATASET.md)*
