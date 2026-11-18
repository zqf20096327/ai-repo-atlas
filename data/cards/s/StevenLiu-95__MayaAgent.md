# StevenLiu-95/MayaAgent

⭐ 21 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/StevenLiu-95/MayaAgent) · 个人维护 · 中文 README

**面向 Maya 游戏开发管线的自然语言 AI Agent 插件**

运行在 Autodesk Maya（2020–2026）内的 AI Agent 面板：用自然语言驱动建模、UV、绑骨蒙皮、动画、材质、灯光与 FBX/OBJ/USD/ABC 导出，内置 235 个工具（18 类），含 15 种模板骨架的自动绑骨与 11 个蒙皮权重工具。支持 15 家大模型（默认 DeepSeek，含 Ollama 本地与自定义 OpenAI 兼容接口），接入 Meshy/Tripo/腾讯混元3D 云端生 3D，并提供 MCP 桥供 Cursor/VS Code/Claude Desktop 调用同一套工具。整轮修改可一次 Ctrl+Z 回退；对话依赖 httpx，图表依赖 matplotlib。提供 Windows 图形安装器、install.bat 与拖入式三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 235 个内置工具 / 18 个类别，覆盖建模、UV、绑骨蒙皮、动画、导出等游戏管线
- 15 家大模型可选（含视觉模型与 Ollama 本地），默认 DeepSeek
- Meshy / Tripo / 腾讯混元3D 云端生 3D 并导入 Maya
- MCP 桥（127.0.0.1 + Bearer token）供 Cursor / VS Code / Claude Desktop 调用同一套工具

## 适用场景

- 用自然语言让 AI 在 Maya 里完成建模、UV 与自动绑骨
- 通过云端 AI 3D 生成模型并导入 Maya 做后处理
- 在 Cursor / VS Code 里经 MCP 远程驱动当前 Maya 会话

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **v1.6.0** — 面向 **Autodesk Maya 游戏开发管线** 的 AI Agent：用自然语言驱动建模、UV、绑骨蒙皮、动画、材质、灯光与导出。内置 **235 个工具 / 18 个类别**，支持 **15 家*
> L9: |**工具调用 Agent**|235 个内置工具（18 个类别）；LLM 规划 → 执行 → 流式回写；单轮可多步工具（默认最多 30 轮，设置里可调至 100）|
> L19: |**Agent / Ask / Plan 模式**|对话栏可切换：**Agent**（全工具）、**Ask**（只读调研）、**Plan**（先 `create_plan` 出步骤卡片，用户「批准执行」后再改场景）；工具按模式白

## 星数曲线

```mermaid
xychart-beta
    title "StevenLiu-95/MayaAgent 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-16", "2026-11-18"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-11-08 20 → 2026-11-18 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `34c02c710707` · [字段定义](../../DATASET.md)*
