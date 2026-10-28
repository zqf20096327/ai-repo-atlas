# logisky/logisheets-mcp

⭐ 41 · TypeScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/logisky/logisheets-mcp) · 个人维护

**给 AI agent 用的 MCP 电子表格服务器：Excel 公式引擎+命名块结构**

基于 Rust 编写的 LogiSheets 电子表格引擎构建的 MCP 服务器，本机运行、MIT 许可。提供 32 个工具：以命名 block（行有键、列有字段名）取代 A1 坐标寻址，字段公式整列声明一次，引擎持有计算值防止模型覆写；支持将 schema 与描述写入 .xlsx 供后续会话读取，图表存引用而非数值并随数据变动重算，另有 preview_changes、goal_seek、trace 等工具。公式为 Excel 兼容格式加 BLOCKREF/#FIELD 扩展。安装需 Node 20+，npm 全局安装，可接入 Claude Desktop、Cursor 等任意 stdio MCP host。

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

- 32 个 MCP 工具：block 建表、字段规则、透视表、图表、goal_seek 等
- 命名寻址（键+字段）替代 A1 坐标，插入行列不破坏引用
- schema 与 prose 描述写入 .xlsx，跨会话可恢复模型含义
- 图表存储引用而非数值，源数据变动后自动重算

## 适用场景

- 让 agent 构建财务模型并交付带活公式的 .xlsx 文件
- 接手他人发来的电子表格，转换成结构化 block 继续操作
- 对模型做多情景 what-if 分析与反解输入（goal_seek）

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: An MCP server over
> L11: LogiSheets, a spreadsheet engine written
> L12: in Rust. MIT, runs on your machine, opens no sockets.

## 星数曲线

```mermaid
xychart-beta
    title "logisky/logisheets-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5d2a9d0da40d` · [字段定义](../../DATASET.md)*
