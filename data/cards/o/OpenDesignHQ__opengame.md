# OpenDesignHQ/opengame

⭐ — · [GitHub]() · 组织维护 · 中文 README

**把本地编码 Agent 变成全栈 AI 游戏工作室的工具链**

OpenGame 将 DeepSeek、Claude Code、Codex 等 22 个本地编码 Agent 接入游戏开发流水线：用户粘贴一段提示词后，通过 Skills CLI 安装 openmotion-game 技能（含 18 本游戏工程手册），并在本地从源码运行 Game Studio，Agent 借此调用 12 个 openmotion_game_* MCP 工具。内置 25 个可玩 HTML5/Three.js 游戏模板，支持一键 Remix 与换皮，提供逻辑校验、无头试玩、封面与预告生成，并可发布 Web 链接及导出 9:16 Playable Ads，对接微信小游戏/TikTok/抖音发布路径。需 Node.js 22.18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 22 个本地编码 Agent（BYOA/BYOK）
- 25 个内置可玩 HTML5/Three.js 游戏模板，含完整源码
- 12 个 openmotion_game_* MCP 工具供 Agent 调用
- Playable Ads 导出与微信小游戏/TikTok/抖音发布路径

## 适用场景

- 用本地编码 Agent 从一个想法生成可玩的 3D 或小游戏
- 基于内置模板一键 Remix 或换皮成自己的游戏
- 制作可导出 9:16 Playable Ads 的买量小游戏

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L24: OpenGame is **the first open-source Super Game Agent** — turning **DeepSeek (DSH)**, **Claude Code**, **Codex**, or
> L46: npx skills add OpenDesignHQ/opengame --skill openmotion-game
> L63: **Works with 22 local agents (BYOA)** · Choose your agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `eb10751520d0` · [字段定义](../../DATASET.md)*
