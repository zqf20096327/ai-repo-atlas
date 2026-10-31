# sideshowroberto/vfx-agent-toolkit

⭐ 15 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/sideshowroberto/vfx-agent-toolkit) · 个人维护

**面向 Claude Code 的 VFX 制作技能与 MCP 连接器工具集**

为 Claude Code 提供的插件市场与 MCP 连接器集合，覆盖 Nuke、Houdini、Unreal Engine、Blender、ComfyUI、Maya、Magnific、Seedance 等 VFX 应用。插件部分是按需加载的技能与专用 agent（70+ 技能），连接器部分通过 MCP 协议将 Claude Code 接入正在运行的制作软件，使其能建节点、驱动程序化生成、控制渲染等。安装以 PowerShell 脚本为主（Windows 优先），技能本身为纯 markdown 可跨平台。需 Claude Code、Node.js 18+、Python 3.12+、uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ 技能的 Claude Code 插件体系，覆盖 8 个 VFX 应用的制作流程
- MCP 连接器将 Claude Code 接入运行中的 Nuke/Houdini/Unreal/Blender/Maya/ComfyUI 等应用
- vfx-core 基础插件注册 brave-search/context7/desktop-commander 三个共享 MCP 服务
- 连接器注册的 MCP 服务均为第三方独立项目，工具箱本体 MIT 许可

## 适用场景

- 让 Claude Code 在 Nuke 中按 CSV 批量搭建镜头合成工程
- 通过对话驱动 Houdini 程序化生成、UE PCG 图与 Blender 渲染
- 为 ComfyUI 搭建工作流分析与无头生成指导
- 开发 ComfyUI 自定义节点时获取 V3 API 结构与发布指引

## 场景标签

`图像生成` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: - **Plugins** (`plugins\`) teach Claude Code how to do VFX work. Each plugin is
> L21: - **Connectors** (`connectors\`) wire Claude Code to your running applications
> L105: Connectors register MCP servers that bridge Claude Code to your applications.

## 星数曲线

```mermaid
xychart-beta
    title "sideshowroberto/vfx-agent-toolkit 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29", "2026-10-31"]
    y-axis "stars" 11 --> 16
    line [12, 13, 15, 15]
```

2026-10-18 12 → 2026-10-31 15（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3674cb5ee7d9` · [字段定义](../../DATASET.md)*
