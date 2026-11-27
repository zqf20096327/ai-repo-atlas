# di-sukharev/opencommit

⭐ 7,554 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/di-sukharev/opencommit) · [官网](https://www.npmjs.com/package/opencommit) · 个人维护

**用 LLM 为 git 暂存变更自动生成提交信息的 CLI 工具**

OpenCommit 是一个 npm 全局安装的 CLI 工具（命令 oco），读取 git 暂存区的变更并调用 LLM 生成提交信息，替代 git commit -m 的手写流程。支持多家 LLM 提供方与本地模型（Ollama、llama.cpp、MLX），提供 GitMoji、Conventional Commit 与 @commitlint 两种提示模块、生成语言配置、代理配置、模型列表管理与跳过确认等选项，配置可按仓库（.env）或全局（~/.opencommit）设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- oco 一条命令为暂存变更生成提交信息并提交
- 支持 openai/anthropic/azure/ollama/llamacpp/mlx/gemini/groq/mistral/deepseek/minimax/openrouter/flowise 等提供方
- 可接入 OpenAI 兼容网关与自定义端点 URL
- 支持 GitMoji 全规格、@commitlint 提示模块与多语言生成

## 适用场景

- 日常提交代码时自动生成符合规范的 commit message
- 在本地用 Ollama/llama.cpp 离线生成提交信息
- 团队统一 Conventional Commit/GitMoji 提交风格

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5:  Auto-generate meaningful commits in a second
> L36: You can call OpenCommit with `oco` command to generate a commit message for your staged changes:
> L145: OCO_AI_PROVIDER=<openai (default), anthropic, azure, ollama, llamacpp, mlx, gemini, flowise, groq, mistral, deepse

## 星数曲线

```mermaid
xychart-beta
    title "di-sukharev/opencommit 星数(近 19 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 7540 --> 7556
    line [7542, 7543, 7544, 7542, 7543, 7541, 7542, 7543, 7545, 7546, 7548, 7549, 7552, 7554, 7553, 7552, 7554, 7555, 7554]
```

2026-10-25 7,542 → 2026-11-27 7,554（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `377ed2b9a0b3` · [字段定义](../../DATASET.md)*
