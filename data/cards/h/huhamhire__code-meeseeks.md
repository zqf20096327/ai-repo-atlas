# huhamhire/code-meeseeks

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/huhamhire/code-meeseeks) · [官网](https://huhamhire.github.io/code-meeseeks/) · 个人维护 · 中文 README

**面向个人评审者的本地 AI 代码评审桌面客户端**

基于 Electron 的 pr-agent 桌面 GUI：拉取 GitHub/Bitbucket/GitLab 上待评审的 PR/MR，本地运行 pr-agent 生成 AI 评审意见，由评审者逐条确认/编辑后再发布回远端。数据（仓库镜像、PR 元数据、评论草稿）均存本地，支持自托管实例与 HTTP 代理。提供多 LLM 供应商配置、个性化规则目录、Agentic 编排与 AutoPilot 预评审；另带本地 HTTP API 与跨平台 CLI（meebox）。Windows/macOS 提供安装包，pr-agent 内嵌于安装器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拉取待评审 PR，本地运行 pr-agent 生成评审意见，人工确认后发布
- 统一访问 GitHub / Bitbucket / GitLab（含自托管实例），数据全部留在本地
- 多 LLM 供应商支持（OpenAI/Anthropic/DeepSeek/通义千问/火山方舟/Ollama 等 openai-compatible 端点）
- 本地 HTTP API 与跨平台 CLI `meebox`，可被外部 agent 工具集成

## 适用场景

- 工程师/Tech Lead 在桌面端半自动完成 AI 辅助代码评审
- 企业内网中连接自托管 Bitbucket/GitLab 并走 HTTP 代理
- 为本地 agent 工具（claude/codex）暴露 PR 评审能力

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: **A desktop GUI for PR-Agent · A local, semi-automated AI code-review client for the individual reviewer**
> L22: Code Meeseeks (internal codename `meebox`) is a **desktop graphical interface (GUI)** for the command-line tool pr-

## 星数曲线

```mermaid
xychart-beta
    title "huhamhire/code-meeseeks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3de1db84263d` · [字段定义](../../DATASET.md)*
