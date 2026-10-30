# dashenbibi/tutorial-generator

⭐ 15 · MIT · 推送 2026-06-04 · [GitHub](https://github.com/dashenbibi/tutorial-generator) · 个人维护 · 中文 README

**AI Skill：从任意 URL 自动生成带截图与 TTS 解说的图文/视频教程**

面向 Claude Code、Hermes、Gemini CLI、Codex、OpenHands、Playwright MCP 等 AI agent 的技能（SKILL.md）：输入 URL 后，agent 按六阶段工作流探索站点、自动检测并处理登录（密码/验证码/OAuth）、逐步截图记录操作，输出 Markdown/HTML/PDF/视频教程，视频可配 SRT 字幕与 TTS 配音（edge-tts/gtts，缺失时优雅降级）。采用抽象能力标识符（NAVIGATE/CAPTURE 等）实现工具无关，输出语言可指定，删除类操作停在确认框、支付页仅截图。通过 git clone 或下载 SKILL.md 安装。

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

- 抽象能力标识符设计，兼容多种支持浏览器自动化的 AI agent
- 自动登录检测，支持密码/验证码/OAuth 流程
- 多格式输出：Markdown/HTML/PDF/视频（SRT 字幕烧录 + TTS 配音）
- 每个模块保证至少 3 张截图；删除操作停在确认框、支付页仅截图

## 适用场景

- 为任意网站快速生成带截图的操作教程
- 制作带 TTS 解说的视频版产品使用指南
- 让不同 AI agent 复用同一技能生成多语言教程

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: An AI skill that automatically generates illustrated tutorials for any website. Input a URL, and the agent will expl
> L9: - **Tool-agnostic** — uses abstract capability identifiers, works with any AI agent that supports browser automation

## 星数曲线

```mermaid
xychart-beta
    title "dashenbibi/tutorial-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `38b08533ad96` · [字段定义](../../DATASET.md)*
