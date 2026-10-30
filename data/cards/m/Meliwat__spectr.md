# Meliwat/spectr

⭐ 30 · HTML · MIT · 推送 2026-05-21 · [GitHub](https://github.com/Meliwat/spectr) · [官网](https://www.spectr.to) · 个人维护

**把 iOS 应用录屏转成可直接交给 Claude Code 的 spec.md**

面向使用 Claude Code 的开发者：输入一段 iOS 应用录屏（.mp4/.mov），通过场景切换检测与感知哈希抽取有效帧，交给视觉模型分析，生成 80–150 KB 结构化 spec.md，含 App 概览、导航架构、屏幕规格、组件库、设计系统（精确 hex/字重/间距）及可粘贴的 Claude Code 提示词，默认面向 Expo SDK 54 / React Native / iPhone 15。提供 MCP server、CLI、Claude Code skill 三种安装方式；需 Node 18+、Python 3.10+ 与 ffmpeg，不直接索取 API key，使用本机已有 Claude 凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 录屏→帧抽取（场景检测+感知去重）→视觉模型→七段式 spec.md 流水线
- 输出含精确设计 token 与可粘贴的 Claude Code 构建提示词
- MCP server / npx CLI / Claude Code skill 三种形态共享同一视觉流水线
- 复用本机 Claude 凭证，MCP 模式无需 API key

## 适用场景

- 拿竞品或参考应用的录屏快速产出可复刻的规格文档
- 为 Claude Code 提供含设计系统细节的上下文来构建应用
- 从现有 iOS 应用提取 hex、字重、间距等设计 token

## 场景标签

 · 领域:开发工具/AI 辅助规格生成

## 证据(README 行号)

> L39: claude mcp add spectr -- uvx spectr-mcp
> L63: Drops a `SKILL.md` into `~/.claude/skills/spectr/`. Mention "spec it" or "use Spectr" in any Claude Code conversati
> L70: - **Authenticated `claude` CLI** *or* `ANTHROPIC_API_KEY` in env

## 星数曲线

```mermaid
xychart-beta
    title "Meliwat/spectr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fc2d4ca06764` · [字段定义](../../DATASET.md)*
