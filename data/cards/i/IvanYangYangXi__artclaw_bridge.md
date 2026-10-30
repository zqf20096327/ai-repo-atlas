# IvanYangYangXi/artclaw_bridge

⭐ 36 · Python · MIT · 推送 2026-05-01 · [GitHub](https://github.com/IvanYangYangXi/artclaw_bridge) · 个人维护 · 中文 README

**让 DCC 创作软件通过 MCP 接入 AI Agent 的桥接框架**

面向 Unreal Engine、Maya、3ds Max、Blender、Houdini、Substance Painter/Designer、ComfyUI 等 DCC 软件的统一桥接层：每个 DCC 通过单一 MCP 工具暴露 Python 执行能力，使 OpenClaw、Claude Code、Cursor 等 Agent 平台可直接在编辑器内操作对象、材质与工作流。附带编辑器内 AI 聊天面板、四层优先级的热重载技能系统（官方技能 47 个）、三级记忆管理与本地 RAG 知识库。Houdini 支持及 UE5.3+/Maya2022+ 以外版本未经验证，给游戏开发、影视动画团队使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 款 DCC 软件各暴露单一 MCP 工具，AI 以执行 Python 完成全部操作
- 配置驱动的多 Agent 平台抽象层，支持编辑器内一键热切换
- 分层技能热重载系统：四层优先级、AI 自然语言生成技能、团队共享
- 编辑器内 AI 聊天面板：流式输出、工具调用可视化、附件分析

## 适用场景

- 在 UE/Maya/Blender 等编辑器内用自然语言让 AI 执行建模、材质与工作流操作
- 团队构建并共享跨 DCC 的技能库与工具
- 让 ComfyUI 通过 Agent 自动搭建与修复生成工作流

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Bridge DCC tools (UE, Maya, 3ds Max, Blender, Houdini, Substance Painter/Designer, ComfyUI) to AI Agents via MCP P
> L7: ArtClaw Bridge provides a unified AI bridging layer for Digital Content Creation (DCC) software. Through the MCP (Mo
> L51: ArtClaw Bridge is a **unified bridging layer** that:
> L53: - ✅ Provides a standardized protocol (MCP) for AI-to-software communication

## 星数曲线

```mermaid
xychart-beta
    title "IvanYangYangXi/artclaw_bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b9e4c5339eb5` · [字段定义](../../DATASET.md)*
