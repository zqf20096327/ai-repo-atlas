# eat-pray-ai/yutu

⭐ 736 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/eat-pray-ai/yutu) · [官网](https://yutu.ifor.dev) · 个人维护 · 中文 README

**自动化 YouTube 工作流的 CLI、MCP 服务器与 AI Agent**

面向 YouTube 创作者与开发者的自动化工具：通过 CLI 与 AI Agent 完成视频上传优化、评论/播放列表/频道品牌管理；同时可作为 MCP 服务器接入 Claude 等 AI Agent，并提供 youtube-automation 技能包为 Agent 注入 YouTube 领域知识与 SEO 实践。需自备 Google Cloud 账号并完成 YouTube Data API 与 OAuth 凭据配置。提供 npm、Docker、Homebrew、WinGet、go install 等多种分发渠道，覆盖 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一工具提供 CLI、MCP 服务器与 Agent（Miffy）三种形态
- MCP 一条命令接入 claude、opencode、codex 等 Agent
- 可调用 google/openai/anthropic 三类 LLM provider，支持自定义 base-url
- 提供 npx skills add 的 Agent 技能包（youtube-automation）

## 适用场景

- 从命令行批量管理我的视频、播放列表与评论
- 让 Claude 等 Agent 通过 MCP 直接操作我的 YouTube 频道
- 自动化视频上传并按 SEO 建议优化元数据
- 在 CI 中用 GitHub Actions 定时上传视频

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: `yutu` is a CLI, MCP server, and AI Agent to automate YouTube workflows — from uploading and optimizing videos to m
> L181: `yutu` provides a unified skill that extends AI Agents with YouTube domain knowledge, common workflows, and SEO be

## 星数曲线

```mermaid
xychart-beta
    title "eat-pray-ai/yutu 星数(近 20 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26"]
    y-axis "stars" 699 --> 739
    line [702, 703, 704, 705, 707, 709, 710, 712, 704, 716, 721, 722, 723, 726, 728, 730, 729, 730, 732, 736]
```

2026-10-23 702 → 2026-11-26 736（+34）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b64b7512275d` · [字段定义](../../DATASET.md)*
