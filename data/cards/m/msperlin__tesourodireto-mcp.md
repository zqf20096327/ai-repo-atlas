# msperlin/tesourodireto-mcp

⭐ 4 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/msperlin/tesourodireto-mcp) · 个人维护

**为 LLM agent 提供巴西国债与 ANBIMA 收益率曲线数据的 MCP 服务器**

以 MCP 服务器形式运行的 Python 工具：读取 Tesouro Transparente 官方 CKAN 开放数据门户的 CSV，向 agent 提供巴西国债历史价格与收益率、各期限快照、统计摘要及 ANBIMA 实际/名义/隐含通胀收益率曲线。每日一次下载并本地缓存，门户不可用时回退到旧缓存；输出采用带注释头的 CSV 而非大量 JSON 记录，长序列可按月/年聚合。提供 5 个工具、债券目录资源与 analyze_bond 提示，支持 stdio 与 HTTP 传输，需 Python 3.10+，数据自 2005 年起。

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

- 5 个 MCP 工具：债券目录、历史数据、当前利率、统计摘要、收益率曲线
- 每日一次下载并本地缓存，门户宕机时回退旧缓存
- 带短注释头的 CSV 输出以减少 token 占用，长序列支持月/年聚合
- 支持 stdio、streamable-http、sse 三种传输方式

## 适用场景

- 通过 agent 查询某只国债的当前收益率与到期日
- 让 agent 分析某债券 2024 年收益率走势
- 将巴西国债收益率与 ANBIMA 实际回报曲线做对比分析

## 场景标签

`金融量化` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: An MCP server for **Brazilian government bonds (Tesouro Direto)** — historical
> L8: curve — built for LLM agents.

## 星数曲线

```mermaid
xychart-beta
    title "msperlin/tesourodireto-mcp 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-14", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-13 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e1220c03e8a7` · [字段定义](../../DATASET.md)*
