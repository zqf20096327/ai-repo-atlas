# malkreide/swiss-public-data-mcp

⭐ 18 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/malkreide/swiss-public-data-mcp) · 个人维护

**连接 AI 助手与瑞士公共开放数据的 42 个 MCP 服务器组合**

个人维护的 Model Context Protocol (MCP) 服务器组合：42 个生产就绪的活跃服务器覆盖 41 个数据源、13 个领域（交通、能源、环境、教育、法律等），每个服务器作为只读瘦客户端直接读取一个瑞士官方数据门户或 API（如 opendata.swiss、Open Data Zurich、GeoAdmin），不复制或再托管数据。配套 120 项检查的审计方法（12 类）、portfolio.json 机读清单、registry 与安装片段文档。限制：部分服务器需 API 凭证，15 个服务器启动行为未输出可探测信号。

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

- 42 个活跃 MCP 服务器，每个对应一个瑞士官方数据源，均为只读瘦客户端
- 配套 120 项检查、12 类别的审计方法与 mcp-continuous-auditor 持续 CI 审计
- 苏黎世市/州覆盖最深：交通、教育统计、州法律三个服务器直读官方门户
- 提供 portfolio.json 机读清单、MCP Registry 生成项与客户端安装片段文档

## 适用场景

- 让 Claude Desktop、VS Code + Continue、Cursor 等客户端直接查询瑞士官方数据
- 记者与研究者用自然语言交叉引用多个官方数据源
- 公共管理部门评估开放数据在 AI 助手中的可用性
- civic-tech 开发者复用现成的公共数据 API 客户端接口

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L16: > A curated portfolio of Model Context Protocol (MCP) servers connecting AI agents to Swiss public and open data. T
> L56: **The gap this closes.** An AI assistant cannot browse a portal, read a schema, and guess a query. It needs a small

## 星数曲线

```mermaid
xychart-beta
    title "malkreide/swiss-public-data-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2c401bd1c0cc` · [字段定义](../../DATASET.md)*
