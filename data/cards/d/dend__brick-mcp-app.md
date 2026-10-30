# dend/brick-mcp-app

⭐ 28 · TypeScript · MIT · 推送 2026-03-16 · [GitHub](https://github.com/dend/brick-mcp-app) · 个人维护

**MCP App：让 AI 通过自然语言在 3D 场景中搭积木**

基于 Three.js 的 MCP App，以 MCP 服务器形式运行（http://localhost:3001/mcp），可接入 Claude Desktop（custom connector）与 VS Code（原生 Streamable HTTP）。服务器是场景状态的唯一权威，AI 与交互 UI 均通过 MCP 工具读写场景，服务器校验碰撞、边界与支撑关系。提供 8 个 MCP 工具（放置/读取/删除/导出等）、7 种交互模式的 3D 编辑器、20 种积木类型（48x48 底板），新增积木类型仅需两个文件。作者声明底板设计仍属实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 服务器为场景状态单一事实源，AI 与 UI 均经 MCP 工具变更状态
- 8 个 MCP 工具：读取/放置/删除/清空/导出场景等
- 7 种交互模式的 3D 编辑器（放置/选择/移动/旋转/删除/上色）
- 新增积木类型只需 2 个文件，目录/校验/几何/自动接入

## 适用场景

- 在 Claude Desktop 或 VS Code 中用自然语言让 AI 搭建积木结构
- 在 3D 视口中手动设计积木构造并与 AI 操作互通
- 作为 MCP Apps SDK 的学习/参考实现

## 场景标签

 · 领域:MCP 应用/3D 设计工具

## 证据(README 行号)

> L3:  A Three.js MCP App for designing 3D brick constructions inside MCP-enabled hosts like Claude Desktop and Visual Stu
> L49: The server is the **single source of truth** for all scene state. Both the AI (LLM) and the interactive UI mutate s

## 星数曲线

```mermaid
xychart-beta
    title "dend/brick-mcp-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `872a56ff117f` · [字段定义](../../DATASET.md)*
