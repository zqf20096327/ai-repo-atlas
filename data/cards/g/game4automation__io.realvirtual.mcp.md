# game4automation/io.realvirtual.mcp

⭐ 19 · C# · MIT · 推送 2026-07-22 · [GitHub](https://github.com/game4automation/io.realvirtual.mcp) · [官网](https://realvirtual.io) · 组织维护

**让 AI agent 通过 MCP 协议实时控制 Unity 编辑器的服务器包**

Unity 编辑器内运行的 MCP 服务器包，使 Claude、Cursor 等 MCP 兼容客户端能实时操作 Unity 场景、GameObject、组件、仿真与数字孪生。提供 60+ 内置工具（场景/组件/物理/截图/编辑器等），自定义工具通过 C# 的 [McpTool] 特性以反射自动发现，无需改 Python。架构为 Unity 内 WebSocket 服务器 + 外部 Python 桥接进程，自带嵌入式 Python 3.12。配合 realvirtual 框架可追加驱动、传感器、PLC 信号与机器人 IK 工具用于虚拟调试。要求 Unity 6000.0+ 与系统安装 git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C# [McpTool] 特性定义工具，反射自动发现，无需改 Python 或重启服务器
- 60+ 内置工具覆盖场景、GameObject、组件、变换、物理、截图、编辑器操作
- 配合 realvirtual 框架提供驱动/传感器/PLC 信号/机器人 IK 等工业数字孪生工具
- 编辑器冻结时的 OS 级救援工具：unity_kill / unity_restart / 状态检测

## 适用场景

- 让 Claude/Cursor 等 AI 客户端直接操作我的 Unity 项目场景与组件
- 为工业数字孪生和虚拟调试项目添加 AI agent 可调用的控制工具
- AI agent 控制工厂仿真：移动机器人、控制传送带、读写 PLC 信号

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: This open-source Unity package implements a Model Context Protocol (MCP) server that lets AI agents like Claude, Cur
> L126: This package runs a **WebSocket server** inside the Unity Editor. When an AI agent sends a tool call, the Python M

## 星数曲线

```mermaid
xychart-beta
    title "game4automation/io.realvirtual.mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a7262d10c451` · [字段定义](../../DATASET.md)*
