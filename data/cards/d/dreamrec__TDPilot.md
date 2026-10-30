# dreamrec/TDPilot

⭐ 16 · Python · MIT · 推送 2026-07-23 · [GitHub](https://github.com/dreamrec/TDPilot) · [官网](https://github.com/dreamrec/TDPilot/releases/latest) · 个人维护

**让 AI agent 对话式操控 TouchDesigner 的本地 MCP 服务器（114 工具）**

面向 TouchDesigner 视觉编程的本地优先 MCP 服务器：为 Claude Code、Claude Desktop、Cursor、Codex 等 MCP 客户端提供 114 个工具，覆盖节点创建与连线、参数读写、截图验证、错误诊断、场景快照与回滚。内置基于 Derivative 官方文档审校的 659 卡操作器图谱，把抽象视觉概念路由到具体 TD 操作器链；变更采用事务式执行、预检与参数语义门控，并附可复用的技术记忆与知识存储。安装经 Claude Code 插件命令、shell 脚本或 npx，另需将 .tox 组件拖入 TD 工程；需 TouchDesigner 2025.33070+，无注册与托管服务。

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

- 114 个 MCP 工具：节点构建、参数读写、诊断截图、快照回滚
- 659 卡审校操作器图谱（源自 Derivative 官方文档）
- 事务式执行：预检、参数语义门控、快照与已验证回滚
- 技术记忆与自由格式知识存储，可导入导出

## 适用场景

- 用自然语言让 AI 在 TouchDesigner 里搭建与调试视觉网络
- 现场演出前让 agent 检查渲染链、修复黑屏并截图确认
- 把验证过的节点接法存为可复用技术并分享

## 场景标签

 · 领域:创意编程/视觉计算工具

## 证据(README 行号)

> L22: TDPilot gives Claude (or Cursor, Codex, any MCP client) live control of a
> L110: - A practical control layer between AI agents and TouchDesigner — built for iterative patch development, not one-s

## 星数曲线

```mermaid
xychart-beta
    title "dreamrec/TDPilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f8d4f47d94ba` · [字段定义](../../DATASET.md)*
