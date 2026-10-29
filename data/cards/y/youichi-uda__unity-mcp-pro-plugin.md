# youichi-uda/unity-mcp-pro-plugin

⭐ 82 · C# · MIT · 推送 2026-07-21 · [GitHub](https://github.com/youichi-uda/unity-mcp-pro-plugin) · [官网](https://unity-mcp.abyo.net/) · 个人维护

**连接 AI 助手与 Unity 编辑器的 MCP 插件（280+ 工具）**

Unity 编辑器插件，通过 WebSocket 与 Node.js MCP 服务器通信，把场景管理、GameObject、脚本、预制体、物理、动画、地形、构建管线、输入模拟、截图、测试、ECS、Netcode、XR 等 50 个类别的 280+ 工具暴露给 Claude、Cursor、Windsurf、VS Code Copilot 等 MCP 兼容客户端。所有 AI 操作经 Unity Undo 系统可撤销；WebSocket 带心跳、指数退避重连与端口扫描（6605–6609），支持多编辑器实例。要求 Unity 2021.3+ 与 Node.js 18+，MCP 服务器需单独获取并构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 280+ 工具、50 个类别覆盖 Unity 开发全流程
- 所有 AI 操作走 Unity Undo 系统，可 Ctrl+Z 撤销
- WebSocket 心跳、自动重连与域名重载安全（Domain Reload Safe）
- 多编辑器实例支持（UNITY_MCP_PORT 指定端口）

## 适用场景

- 在 Claude/Cursor 等 AI 助手中直接操作 Unity 编辑器完成场景与脚本工作
- 让 AI 执行批量操作、截图、性能分析等编辑器任务
- 多个 Unity 编辑器同时连接不同 AI 助手实例

## 场景标签

 · 领域:游戏开发/AI 工具集成

## 证据(README 行号)

> L3: Unity editor plugin that connects AI assistants (Claude, Cursor, Windsurf, VS Code Copilot) to the Unity editor via 
> L91: AI Assistant  ←—stdio/MCP—→  Node.js MCP Server  ←—WebSocket—→  Unity Editor Plugin (this repo)

## 星数曲线

```mermaid
xychart-beta
    title "youichi-uda/unity-mcp-pro-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-29 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `93a0695b1685` · [字段定义](../../DATASET.md)*
