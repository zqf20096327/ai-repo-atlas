# volnei/reviewly

⭐ 19 · TypeScript · GPL-3.0 · 推送 2026-09-03 · [GitHub](https://github.com/volnei/reviewly) · 个人维护

**给开发者的本地优先 GitHub PR 审查桌面应用，AI 在本机运行**

基于 Tauri 2（Rust + React）的原生桌面应用，覆盖 macOS/Windows/Linux，将 GitHub PR 审查整合进单一工作区：按待审/自己的 PR/可合并分组的收件箱、统一或分栏 diff 视图、行内评论批量提交为一次 GitHub review、Checks 重跑、Dependabot 告警、本地 clone 集成与 SQLite 离线缓存。AI 部分通过用户本机的 Claude/Codex/Gemini CLI 或 OpenAI 兼容端点（含 Ollama/LM Studio/OpenRouter）提供分层审查、引导式讲解与对话问答；GitHub token 存于系统钥匙串。以安装包形式分发，GPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 走本机 CLI（Claude/Codex/Gemini）或用户自配的 OpenAI 兼容端点，diff 不经中转服务器
- 分层审查模式：按依赖顺序将大 PR 切成多个语义层逐层阅读
- 行内评论批量提交、per-PR 草稿与 viewed-files 跟踪
- PR 本地 SQLite 缓存，列表离线可用

## 适用场景

- 在一个桌面窗口里处理分散在多个浏览器标签的 PR 审查工作
- 让本机 AI 带我通读大型变更并生成讲解/建议评论
- 在不把代码发给第三方服务器的前提下做 AI 辅助审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5:  A fast, local-first desktop app for reviewing GitHub pull requests — with AI that runs on your own machine.
> L14: Reviewly is a native desktop console (macOS, Windows, Linux) that turns PR review from a dozen browser tabs into on
> L18: > **Local-first by design.** Your GitHub token lives in the OS keychain. AI review runs through *your* local CLI (C

## 星数曲线

```mermaid
xychart-beta
    title "volnei/reviewly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4f07a5a56f38` · [字段定义](../../DATASET.md)*
