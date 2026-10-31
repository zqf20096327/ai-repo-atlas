# nachosystems/deep-thinker

⭐ 15 · TypeScript · MIT · 推送 2026-05-23 · [GitHub](https://github.com/nachosystems/deep-thinker) · [官网](https://www.npmjs.com/package/deep-thinker) · 组织维护

**为 MCP 客户端提供结构化深度推理服务的认知思考服务器**

基于 Model Context Protocol 的认知推理 MCP 服务器，以 DAG 思维图组织思考节点，支持分支、合并与交叉边。提供 10 种推理策略（含基于内容信号的 auto 自动选择）、17 个工具（think/evaluate/metacog/graph/prune/reset/conclude 等）、节点别名、会话持久化（~/.deep-thinker/sessions/）、置信度评分、自我批判、知识整合与思维剪枝。通过 npx 或 npm 全局安装，stdio 通信，可接入 Claude Desktop 及其他 MCP 客户端。多语言思考内容支持含中文。

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

- DAG 思维图支持分支、合并与交叉边
- 10 种推理策略含 auto 自动选择（关键词与图状态驱动）
- 元认知引擎检测停滞/置信度下降并建议策略切换
- 会话持久化与 17 个工具（思考/评估/剪枝/结论等）

## 适用场景

- 在 Claude Desktop 等 MCP 客户端中进行结构化多策略推理
- 复杂决策（架构选型、事故根因分析）时用思维图管理推理过程
- 跨会话保存并恢复分析过程

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: Advanced cognitive thinking MCP server with DAG-based thought graph, **10 reasoning strategies** (including auto-sel
> L100: The server communicates over stdio. Point your MCP client to the `deep-thinker` command or `node path/to/dist/inde

## 星数曲线

```mermaid
xychart-beta
    title "nachosystems/deep-thinker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `700dd95ebe5b` · [字段定义](../../DATASET.md)*
