# conorluddy/xclaude-plugin

⭐ 186 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/conorluddy/xclaude-plugin) · 个人维护

**Claude Code 的模块化 iOS 开发 MCP 插件（已停止维护）**

面向 Claude Code 的插件，提供 8 个按工作流划分的 MCP 服务器（xc-build/xc-launch/xc-interact 等），共享 24 个覆盖 Xcode、Simulator 与 IDB 的工具，按需启用以控制上下文 token 占用；工具将 Xcode 输出封装为结构化 JSON 以减少 token 消耗，另含 8 个按需加载的过程性技能与模拟器配置文件机制。作者声明 MCP 演进后该设计不再必要，已停止维护，建议改用其 xc-mcp 或 ios-simulator-skill 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个工作流专用 MCP 服务器，共享 24 个 Xcode/Simulator/IDB 工具
- 按需启用单个 MCP（约 400-3500 tokens）控制上下文占用
- Xcode 输出封装为结构化 JSON，替代原始 50+ 行日志
- 项目级/用户级模拟器默认配置与使用追踪

## 适用场景

- 在 Claude Code 中通过自然语言构建、测试和运行 iOS 应用
- 控制 MCP 工具在上下文窗口中的 token 占用
- 用 IDB 做基于无障碍树的模拟器 UI 自动化

## 场景标签

`编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: Note: This was built back when MCPs used to take up a bunch of context even when unused. The idea was that you could
> L15: Build, test, and automate iOS apps through natural conversation with Claude. 8 workflow-specific MCP servers with 2
> L25: - **8 workflow-specific MCP servers** (600-3500 tokens each)

## 星数曲线

```mermaid
xychart-beta
    title "conorluddy/xclaude-plugin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 183 --> 187
    line [184, 186, 186]
```

2026-10-18 184 → 2026-10-25 186（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d32af563cbd2` · [字段定义](../../DATASET.md)*
