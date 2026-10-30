# ZenyaDAR/PlayGuard

⭐ 15 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ZenyaDAR/PlayGuard) · [官网](https://playguard.dev/) · 个人维护

**给 AI agent 用的 MCP 代理：优化 Playwright/Figma 工具响应**

位于 AI agent 与 Playwright MCP / Figma MCP 之间的代理层，对外暴露单一统一 MCP 服务器。功能包括：浏览器死会话自动恢复与重试、快照压缩与增量 diff、eval 缓存、截图策略（warn/redirect/block/allow）；Figma 响应经多模块管线剥离元数据、不可见图层、重复组件与 SVG 几何；另提供 Figma 节点与 DOM 元素的设计 diff 工具。兼容 Claude Code、Claude Desktop、Cursor、Codex 等 MCP 客户端，Playwright MCP 作为依赖打包，无需单独安装。

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

- 死浏览器会话自动重启、恢复 URL 并透明重试调用
- 快照压缩/delta diff/缓存，降低浏览器快照开销（宣称 70–90%）
- Figma 响应 8 个优化模块（元数据清理、组件去重、SVG 引用化、预算裁剪等）
- playguard_compare_design 对比 Figma 节点与 DOM 实现并报告差异

## 适用场景

- 让 Claude Code/Cursor 等 agent 的浏览器操作更省 token 且不断会话
- AI 实现 Figma 设计稿时缩减响应体积、核对还原度
- 统一接入并管控 Playwright 与 Figma 两套 MCP 工具

## 场景标签

 · 领域:AI agent 工具链/浏览器自动化

## 证据(README 行号)

> L3: An MCP proxy that sits between your AI agent and browser/design tools. It wraps Playwright MCP and optionally a Figm
> L10: Works with Claude Code, Claude Desktop, Cursor, Codex, or any MCP-compatible agent.

## 星数曲线

```mermaid
xychart-beta
    title "ZenyaDAR/PlayGuard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f15ac34753b1` · [字段定义](../../DATASET.md)*
