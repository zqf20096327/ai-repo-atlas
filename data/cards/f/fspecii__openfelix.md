# fspecii/openfelix

⭐ 33 · Swift · 推送 2026-03-06 · [GitHub](https://github.com/fspecii/openfelix) · [官网](https://openfelix.com) · 个人维护

**macOS 菜单栏语音优先 AI 助手，本地 MLX 或云端模型**

面向 macOS 用户的菜单栏 AI agent：Option+Space 全局热键唤起，支持语音或文字输入，可读写日历与提醒事项、搜索网页、生成运行代码、生成音乐、执行定时任务，并以语音回应。本地通过 MLX 在 Apple Silicon 上运行 Qwen 等模型（无需 API key），也可切换 Claude、GPT-4o 或任意 OpenAI 兼容云端模型。技能系统兼容 OpenClaw 的 SKILL.md 格式并自动继承其配置。DMG 下载或源码构建（需 Xcode 15+、Python 3.12+），自述为早期功能原型，部分功能仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Option+Space 语音/文字输入的菜单栏 agent，含屏幕视觉与定时任务
- 本地 MLX 运行 Qwen 0.8B–9B（1–6GB RAM），可切换 Claude/GPT-4o 云端模型
- 技能系统兼容 OpenClaw，自动继承其技能、API key 与通知配置
- 内置 YouTube 搜索、财务查询、音乐生成等技能，支持 SKILL.md 定时调度

## 适用场景

- 在 Mac 上用语音让 AI 代为查日历、发消息、跑定时任务
- 希望 AI 助手完全本地离线运行于 Apple Silicon
- 已有 OpenClaw 配置的用户零配置复用技能与 API key

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L28: OpenFelix is a free, open-source AI agent that lives in your Mac menu bar. Press **Option+Space** anywhere, speak o
> L30: It's not a chatbot. It's an agent with tools, voice I/O, and a skill system that extends it to anything. It runs **

## 星数曲线

```mermaid
xychart-beta
    title "fspecii/openfelix 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2d04fc7cdc82` · [字段定义](../../DATASET.md)*
