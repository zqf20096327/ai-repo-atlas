# Inparsian/gray-meadows-shell

⭐ 21 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Inparsian/gray-meadows-shell) · [官网](https://gray-meadows.inpr.sn) · 个人维护

**Hyprland 桌面 shell：含 AI 助手的 gtk4 栏/侧栏/启动器**

个人维护的独立 Hyprland 桌面 shell，使用 gtk4 与 gtk4-layer-shell，以 Rust 和 C++ 从零重写（前身为 TypeScript+JSX 的 AGSv2 版本）。功能包括：工作区/音乐/托盘/系统状态栏，通知与音量 OSD，基于 cliphist 与 wl-clipboard 的剪贴板管理，带智能搜索与应用启动权重加成的 Overview，左右侧边栏（通知、音频、日历、天气、翻译、取色器、录屏），以及一个接入 OpenAI/Gemini 的集成 AI 助手。README 声明为 beta 软件，日常可用但可能有 bug；未在 README 中给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- gtk4-layer-shell 实现的栏、OSD 与双侧边栏桌面组件
- 应用启动器追踪最常启动应用并提升其搜索权重
- 集成 OpenAI/Gemini 的 AI 助手（左侧栏）
- 基于 cliphist/wl-clipboard 的剪贴板管理与 gpu-screen-recorder 录屏集成

## 适用场景

- 在 Hyprland 上使用自包含的桌面 shell 与状态栏
- 通过侧栏 AI 助手、翻译、取色器等工具完成日常桌面操作
- 需要带搜索权重学习功能的应用启动器

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: My personal stand-alone Hyprland desktop shell using gtk4 and gtk4-layer-shell, re-written from scratch in Rust and
> L56:  - Integrated AI assistant powered by OpenAI/Gemini

## 星数曲线

```mermaid
xychart-beta
    title "Inparsian/gray-meadows-shell 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b82659677ba3` · [字段定义](../../DATASET.md)*
