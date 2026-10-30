# ondata/istat_mcp_server

⭐ 24 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/ondata/istat_mcp_server) · [官网](https://ondata.github.io/istat_mcp_server/) · 组织维护

**供 MCP 客户端查询意大利 ISTAT 统计数据的 MCP 服务器**

基于 Python 的 Model Context Protocol 服务器，通过 SDMX REST API 向 Claude Desktop 等 MCP 客户端提供意大利国家统计局（ISTAT）数据访问：8 个工具覆盖数据集发现、维度/代码表元数据查询与按维度过滤取数（TSV 格式）。内置双层缓存（内存 5 分钟 TTL + 磁盘持久化，元数据缓存 1 个月）、限流（每分钟最多 4 次 API 调用）与指数退避重试；支持 dataflow 黑名单过滤与领土代码解析。需 Python >=3.11，默认 stdio 传输，另附 HTTP 传输、Dockerfile 与 Helm chart，无版本化发布（main 分支即安装版）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 MCP 工具：数据集发现、约束/元数据查询、按维度过滤取数（TSV）
- 双层缓存（内存 + 磁盘持久化）与限流（4 次/分钟）+ 指数退避重试
- dataflow 黑名单与领土代码（大区/省/市镇）解析
- 支持 stdio 与 MCP streamable-HTTP 两种传输，附 Dockerfile 与 Helm chart

## 适用场景

- 在 Claude Desktop / Claude Code 等客户端中用自然语言查询意大利官方统计数据
- 发现并过滤 ISTAT 数据集、查看维度与代码表后取数
- 以 HTTP/Docker/Kubernetes 方式在网络环境部署该数据服务

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: MCP server for accessing Italian statistical data from the ISTAT SDMX API.
> L12: This Model Context Protocol (MCP) server provides Claude Desktop with access to Italian statistical data from ISTAT
> L94: This server works with any MCP-compatible client. The sections below cover the most common ones.

## 星数曲线

```mermaid
xychart-beta
    title "ondata/istat_mcp_server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b81da3f5af64` · [字段定义](../../DATASET.md)*
