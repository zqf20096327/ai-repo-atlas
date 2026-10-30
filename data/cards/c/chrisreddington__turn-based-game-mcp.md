# chrisreddington/turn-based-game-mcp

⭐ 31 · TypeScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/chrisreddington/turn-based-game-mcp) · 个人维护

**回合制游戏 Web 应用兼 MCP Server，供开发者学习 MCP 的演示示例**

基于 Next.js 15 与 TypeScript 的回合制游戏平台，含井字棋与石头剪刀布两款游戏，前端与 API 之外提供一个 MCP Server，通过 6 个 MCP 工具（创建游戏、AI 走子、等待玩家、局面分析等）充当 AI 对手。作者声明这是面向对构建 Model Context Protocol 感兴趣的开发者的演示与学习工具，非生产级应用。井字棋 AI 分三档难度（random/strategic/minimax），石头剪刀布含随机、自适应与模式化策略。需 Node.js 18+，从源码构建运行，MIT 许可。

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

- 提供 6 个 MCP 工具（create/play/wait_for_player_move/analyze_game 等）
- 井字棋三档 AI 难度（Easy 随机 / Medium 策略 / Hard minimax）
- Next.js 15 前端 + API + MCP Server 的 monorepo 结构，共享游戏逻辑
- VS Code MCP 配置（.vscode/mcp.json），Server 以 stdio 运行

## 适用场景

- 学习如何构建和集成 Model Context Protocol 服务器
- 体验 MCP 客户端连接 AI 对手进行回合制游戏
- 参照其 monorepo 结构扩展自己的游戏与 MCP 工具

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This app is intended as a demo to showcase an example of MCP visually. It is not intended to be a production-ready a
> L5: It is a modern turn-based games platform featuring a Next.js 15 frontend (and API), as well as an MCP (Model Context
> L10: - **MCP Server**: AI opponent powered by Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "chrisreddington/turn-based-game-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a3bef079c9f7` · [字段定义](../../DATASET.md)*
