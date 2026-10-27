# Protocol-Lattice/harness-router

⭐ 23 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/Protocol-Lattice/harness-router) · [官网](https://harness-router.vercel.app) · 组织维护

**嵌入 agent harness 的工具选择决策层：为下一步调用挑选工具**

嵌入现有 agent harness 生命周期的决策组件：接收目标、当前观察与可用工具列表，返回工具选择、置信度或回退给宿主规划器。默认通过 OpenRouter 调用 Jev 模型做离散决策，缓存可复用选择，超过 24 个工具时启用先类别后工具的分层路由，并支持可选的 MCTS 模拟搜索（本地可无 API key 运行）。提供 CLI、stdio MCP server 与 Python API，并为 Codex、Claude Code、ohmypi、Antigravity、DeepSeek Harness 五种宿主提供钩子集成。状态标注为 alpha。

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

- goal+observation+tools 输入，返回工具选择/置信度/回退决策
- 通过 OpenRouter 使用 Jev 模型，支持决策缓存与分层路由（>24 工具）
- 可选 MCTS 搜索路径，支持无 API key 本地运行
- CLI / MCP server / Python API 三种使用方式，五种宿主 harness 钩子集成

## 适用场景

- 在大型工具注册表中为 agent 每一步挑选下一个工具
- 为 Codex / Claude Code 等编码 agent 添加 next-tool 决策预计算
- 通过 MCP 在自建 agent 中显式调用工具路由与 MCTS 搜索

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Harness Router takes a goal, the current observation, and a set of available tools,
> L11: processes its result. Router supplies the next-tool decision at the lifecycle

## 星数曲线

```mermaid
xychart-beta
    title "Protocol-Lattice/harness-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dfd311a76211` · [字段定义](../../DATASET.md)*
