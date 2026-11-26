# blyth-ai/playable-kit

⭐ 5 · JavaScript · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/blyth-ai/playable-kit) · [官网](https://blyth.ai/arcade) · 组织维护

**让 AI agent 开发可玩手游与试玩广告的工具包**

Blyth Arcade 所依赖的工具包：包含 Play Kernel（HTML5 游戏内核，提供触控/键盘输入、固定步长循环、程序化音效、HUD、MRAID 消息等）、构建与验证脚本、两个参考游戏及 SKILL.md 工作流。用户在 Claude Code、Codex、Cursor 等 coding agent 中按 SKILL.md 指令生成游戏，经 build 打包为单个 5 MB 以内的 index.html，verify 在无头 Chromium 中由 bot 试玩并执行 17 项检查。构建的游戏可同时作为试玩广告发布，含广告模式与可调参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 定义 AI agent 生成游戏的工作流（plan→编码→build→verify）
- 17 项无头 Chromium 自动验证：bot 试玩、帧率、体积、无网络请求等
- 构建产物为单个 <5MB 自包含 index.html，可离线运行
- 同一文件可作为试玩广告，含三关广告模式与安装引导卡

## 适用场景

- 用 coding agent 从一句话描述生成可玩手游
- 为应用商店或广告网络制作试玩广告素材
- 营销人员不改代码调整游戏颜色、难度与文案参数

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: This is the kit Blyth Arcade runs on: the **Blyth Play Kernel**, build and verify tools, two
> L12: reference games and **`SKILL.md`**, the workflow an AI agent follows to turn one sentence into a finished game.
> L40: Open the folder in Claude Code, Codex, Cursor or any other coding agent and ask for a game:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a3a427dc2646` · [字段定义](../../DATASET.md)*
