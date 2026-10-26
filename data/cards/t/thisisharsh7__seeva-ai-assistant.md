# thisisharsh7/seeva-ai-assistant

⭐ 30 · TypeScript · MIT · 推送 2026-05-09 · [GitHub](https://github.com/thisisharsh7/seeva-ai-assistant) · [官网](https://thisisharsh7.github.io/seeva-ai-assistant/) · 个人维护

**快捷键呼出的桌面 AI 问答悬浮层，支持多模型与屏幕识别**

基于 Tauri/React/Rust 的跨平台 AI overlay 应用：按 Ctrl+Shift+Space 在任意应用（含全屏、游戏、编辑器）上方唤出问答窗口，可接入 Claude、GPT 或 OpenRouter 并随时切换。支持屏幕截图作为提问上下文（macOS 需授权屏幕录制）、检测当前所在应用并附入上下文，会话数据以 SQLite 全部本地存储。提供 macOS/Windows/Linux 安装包，也可从源码构建。作者自述 v0.2.0 处于早期阶段，功能尚未完整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 快捷键全局呼出，可覆盖全屏应用与游戏
- 支持 Claude/GPT/OpenRouter 多提供商切换（BYOK）
- Watch Screen 屏幕截图提问与应用上下文检测
- 会话与数据全部本地 SQLite 存储，无云端/遥测

## 适用场景

- 写代码时快捷键快速问 AI，减少浏览器标签切换
- 把屏幕内容截图直接交给 AI 分析，不用文字描述
- 在多个 AI 提供商之间切换使用自己的 API key

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: AI overlay that works like Spotlight. Press a key, ask AI, get back to work.
> L34: Use Claude, GPT, or OpenRouter. Switch between them anytime.

## 星数曲线

```mermaid
xychart-beta
    title "thisisharsh7/seeva-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `25bd67a14b19` · [字段定义](../../DATASET.md)*
