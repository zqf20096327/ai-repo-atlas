# toxy4ny/nikki-ai-cli-assistent

⭐ 32 · Shell · MIT · 推送 2025-12-13 · [GitHub](https://github.com/toxy4ny/nikki-ai-cli-assistent) · 个人维护

**红队/DevOps 用本地离线 AI 终端助手（fish shell）**

基于 aichat 与 Ollama 构建的 fish shell 终端 AI 助手，面向红队与渗透测试人员：生成 PowerShell/C/Rust/Bash 攻击代码、分析 GitHub 仓库中的漏洞与利用、调试脚本并支持多轮会话。机制上通过 RAG 检索本地克隆的红队知识库（PayloadsAllTheThings、Atomic Red Team、SharpCollection 等），使用本地模型 rnj-1-instruct 与 nomic-embed-text 嵌入，处理全程本地无云端依赖；知识库未命中的内容会回复未找到而非生成。限制：依赖 Athena OS 或 Arch 系发行版、aichat、Ollama、fish 等环境，提供 PKGBUILD 与 install.sh 两种安装方式。

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

- 本地离线运行，无云端依赖与提示词外泄
- RAG 检索红队知识库（PayloadsAllTheThings/Atomic Red Team/SharpCollection 等）
- 知识库未命中时回复未找到，可用 .sources rag 核验来源
- 多轮会话（--session）与 fish shell 集成

## 适用场景

- 在终端中生成与调试红队攻击代码
- 基于最新红队仓库检索攻击技术并核验出处
- 在 Athena OS/Arch 环境下搭建离线 AI 助手

## 场景标签

`AI 助手` `RAG` `网络安全` · 领域:对话与助手

## 证据(README 行号)

> L3: > **Nikki** is your local, offline, uncensored AI teammate in the CLI — purpose-built for:
> L10: Powered by **aichat**, **Ollama**, **RAG**, and curated red team repositories like `PayloadsAllTheThings`, `Atomic 
> L14: - ✅ **Fully offline** — works without internet after setup

## 星数曲线

```mermaid
xychart-beta
    title "toxy4ny/nikki-ai-cli-assistent 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-24", "2026-10-25"]
    y-axis "stars" 31 --> 34
    line [32, 33, 32]
```

2026-10-19 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7fe3b8727454` · [字段定义](../../DATASET.md)*
