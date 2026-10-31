# devteapot/slop

⭐ 14 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/devteapot/slop) · [官网](https://slopai.dev) · 组织维护

**让 AI 直接观察与操作应用状态的协议与 SDK 集合**

SLOP 定义了一个应用与 AI 之间的状态感知协议：应用发布语义状态树，AI 可订阅子树、按可变深度查询，并通过节点上的上下文化 affordance 执行动作；状态变化以 JSON Patch 增量推送，附带注意力提示。提供 TypeScript、Python、Go、Rust 多语言 SDK、Chrome 扩展、桌面应用、CLI 与 MCP Apps bridge，并附带 MCP 对照基准测试。README 声明 v0.2.0 仍有限制：服务器端提供者不区分多用户会话、无自动重连、无背压、无局域网发现。

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

- 语义状态树 + JSON Patch 增量订阅推送
- 上下文化 affordance：动作附着于所影响的节点
- TypeScript/Python/Go/Rust 多语言 SDK 与框架适配器
- Chrome 扩展、桌面应用、CLI、MCP Apps bridge 与 OpenClaw 集成

## 适用场景

- 让 AI agent 感知应用当前状态后再执行操作
- 把现有 Web/桌面应用封装为 AI 可观察的 SLOP 提供者
- 对比 SLOP 与 MCP 在同一应用上的 agent 表现

## 场景标签

 · 领域:AI Agent 基础设施/协议

## 证据(README 行号)

> L3: SLOP is a protocol that lets AI observe and interact with application state directly — no screenshots, no scraping, 
> L5: Applications expose a **semantic state tree** that AI can subscribe to, query at variable depth, and act on through 
> L80: - MCP Interoperability — MCP Apps bridge, proxy, discovery alignment

## 星数曲线

```mermaid
xychart-beta
    title "devteapot/slop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `496583ce095e` · [字段定义](../../DATASET.md)*
