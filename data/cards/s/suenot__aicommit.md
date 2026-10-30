# suenot/aicommit

⭐ 25 · Rust · Unlicense · 推送 2026-03-30 · [GitHub](https://github.com/suenot/aicommit) · [官网](https://aicommit-theta.vercel.app/) · 个人维护

**用 LLM 生成 git 提交信息的命令行工具**

基于 Node.js/Rust 的 CLI 工具 aicommit，读取 git 变更并通过 LLM 生成提交信息，支持自动暂存（--add）、自动推送（--push/--push-all）、交互与 watch 模式。支持多种 LLM 提供方：OpenRouter、Simple Free 免费模型模式（含三级 jail/blacklist 故障转移与按参数规模的模型排序）、Ollama 本地推理、任意 OpenAI 兼容端点（LM Studio 等）。另提供版本号同步（Cargo.toml/package.json/GitHub tag）与 VS Code 扩展。配置存于 ~/.aicommit.json，支持失败重试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成提交信息，支持 OpenRouter/Ollama/OpenAI 兼容端点
- Simple Free 模式自动选取 OpenRouter 免费模型，带 jail/blacklist 故障转移
- 自动暂存与推送（--add/--push/--push-all 到全部远程）
- 版本号递增与 Cargo.toml/package.json/GitHub tag 同步

## 适用场景

- 我不想手写 commit message，让 AI 根据变更生成
- 用本地 Ollama 模型离线生成提交信息
- 同时推送到 github/gitlab 多个远程仓库并自动管理版本号

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L12: A CLI tool that generates concise and descriptive git commit messages using LLMs (Large Language Models).
> L17: - ✅ Uses LLMs to generate meaningful commit messages from your changes
> L21:  - Ollama (local)

## 星数曲线

```mermaid
xychart-beta
    title "suenot/aicommit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `194d805e3ecf` · [字段定义](../../DATASET.md)*
