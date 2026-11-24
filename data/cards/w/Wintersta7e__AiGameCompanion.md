# Wintersta7e/AiGameCompanion

⭐ 10 · Rust · MIT · 推送 2026-11-22 · [GitHub](https://github.com/Wintersta7e/AiGameCompanion) · 个人维护

**游戏内悬浮 AI 问答窗：边玩边向 Gemini/Claude/OpenAI 提问**

以 Tauri 2 + Svelte 5 构建的 Windows 桌面工具，包含游戏库启动器与一个置顶透明对话面板 Sage。用户可在游戏中通过快捷键唤出面板提问，直接获得 AI 生成的回答、屏幕截图解读与屏幕文字翻译。面板由 Windows 合成叠加于游戏之上，不注入 DLL、不挂钩图形 API。Gemini 走直连 API（免费 key），Claude 与 OpenAI 则调用用户已安装的 claude/codex CLI 子进程。限制：仅支持无边框/全屏窗口化游戏，不支持内核级反作弊竞技类游戏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 透明置顶悬浮窗，无注入、无图形 API 挂钩，Ctrl+Shift+G 唤出
- 多提供商：Gemini 直连 API，Claude/OpenAI 通过用户自有 CLI 子进程
- Windows.Graphics.Capture 截屏供三个提供商读取，发送前预览
- 翻译（Ctrl+Shift+T）与快捷提问（Ctrl+Shift+A）热键，聊天本地保存并提供续聊回顾

## 适用场景

- 游戏卡关时在游戏内直接向 AI 要提示或完整答案
- 游玩外文游戏时截屏翻译屏幕文字
- 截取当前游戏画面让 AI 解读局面

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L25: moment. Responses come from **Sage**, an in-game advisor drawn in a panel over
> L95: Sage can talk through **Gemini**, **Claude**, or **OpenAI** -- pick one from the
> L138: |App|[Tauri 2][tauri] + [Svelte 5][svelte] + Tailwind 4|One process, two windows: library + transparent overlay|

## 星数曲线

```mermaid
xychart-beta
    title "Wintersta7e/AiGameCompanion 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-29 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `3b6110c60a35` · [字段定义](../../DATASET.md)*
