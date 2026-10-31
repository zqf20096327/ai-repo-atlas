# Wadan3/ai-github-repository-assistant

⭐ 15 · TypeScript · MIT · 推送 2026-08-23 · [GitHub](https://github.com/Wadan3/ai-github-repository-assistant) · 个人维护

**本地 AI 驱动的 GitHub 仓库分析与问答应用**

基于 Next.js 16 的开源 Web 应用：通过 GitHub OAuth 登录后浏览可访问仓库（含私有），提供仓库报告、架构分析、PR/Issue 摘要与风险检测、逐文件解释等 AI 功能，回答需引用经验证的文件路径。默认使用本地 Ollama 作为 AI 提供方（默认模型 qwen2.5:3b），无需付费 AI 服务；通过 AIProvider 抽象层隔离模型实现，Ollama 停止时应用仍可用于 GitHub 浏览。不执行仓库代码，不进行任何 GitHub 写操作。

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

- GitHub OAuth 登录与仓库/代码/PR/Issue 的证据接地 AI 分析
- 默认 Ollama 本地模型，仓库上下文留在本机，无需外部 AI 服务
- AIProvider 抽象使模型后端可与 GitHub/UI 代码解耦
- 明确的安全边界：不执行仓库代码、无 GitHub 写端点

## 适用场景

- 接手新仓库时快速了解架构、入口与风险点
- 让 AI 基于真实文件路径回答仓库相关问题
- 本地 Ollama 生成 PR/Issue 摘要与审查清单，不外发代码上下文

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: RepoLens AI is an open-source Next.js application that connects to GitHub, lets developers explore accessible reposi
> L18: - Repository chat that cites verified file paths and admits missing evidence
> L40:                                └─ AIProvider ─ Ollama

## 星数曲线

```mermaid
xychart-beta
    title "Wadan3/ai-github-repository-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a2ee50ca0d12` · [字段定义](../../DATASET.md)*
