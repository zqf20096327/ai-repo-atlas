# eat-pray-ai/yutu

⭐ 738 · Go · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/eat-pray-ai/yutu) · [官网](https://yutu.ifor.dev) · 个人维护 · 中文 README

**自动化 YouTube 工作流的 CLI、MCP 服务器与 AI Agent**

以 Go 编写的多形态工具：既是命令行工具，也可作为 MCP 服务器供 AI Agent 调用，还内置 Agent 模式（Miffy）自动执行 YouTube 操作，覆盖视频上传与优化、评论、播放列表、频道品牌管理等。Agent 通过 --provider 支持 google/openai/anthropic 三类 LLM 后端，默认 Gemini 兼容接口。需要 Google Cloud 账号完成 OAuth 授权后运行。

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

- CLI、MCP 服务器、Agent 三种形态共用一套 YouTube 操作
- yutu mcp setup 一条命令为多个 AI Agent 配置 MCP
- 提供 youtube-automation 技能包扩展 AI Agent 的 YouTube 领域知识
- 支持 brew/npm/winget/docker/go install 多渠道安装及签名验证

## 适用场景

- 用命令行批量管理 YouTube 视频、评论和播放列表
- 让 Claude 等 AI Agent 通过 MCP 调用 YouTube API
- 配置 Agent 自动化执行视频上传与 SEO 优化

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: `yutu` is a CLI, MCP server, and AI Agent to automate YouTube workflows — from uploading and optimizing videos to m
> L145: `yutu` provides an Agent mode (Miffy) to automate YouTube workflows. The Agent can retrieve, create, update, and d
> L181: `yutu` provides a unified skill that extends AI Agents with YouTube domain knowledge, common workflows, and SEO be

## 星数曲线

```mermaid
xychart-beta
    title "eat-pray-ai/yutu 星数(近 20 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 700 --> 741
    line [703, 704, 705, 707, 709, 710, 712, 704, 716, 721, 722, 723, 726, 728, 730, 729, 730, 732, 736, 738]
```

2026-10-24 703 → 2026-11-27 738（+35）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `79e8966edcd4` · [字段定义](../../DATASET.md)*
