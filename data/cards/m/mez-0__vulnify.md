# mez-0/vulnify

⭐ 38 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/mez-0/vulnify) · 个人维护

**聚合五大 CVE 数据源并经 MCP 供 AI agent 查询的漏洞库**

CVE 摄取与富化流水线：从 CVEProject、NVD、CISA KEV、EPSS、OSV 及 Nuclei/Exploit-DB/Metasploit 语料构建单一规范化 SQLite 库（20 表，含 FTS5 全文索引），流水线带断点续跑与水位标记。附带 FastMCP stdio 服务器 `vulnify-mcp`，向 Claude Code/Claude Desktop/Cursor 等 agent 暴露 8 个查询工具（CVE 详情、多维过滤检索、exploit 证据等），另有约 70 个预置视图的 Streamlit 探索器。每次 release 附带预构建压缩数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五大 CVE 数据源合并为单一规范化 SQLite 库
- FastMCP 服务器向 AI agent 提供 8 个查询工具（含 FTS5 全文检索）
- 流水线断点续跑、按水位增量更新
- release 附预构建压缩数据库与 FTS5 索引

## 适用场景

- 让 Claude Code/Cursor 等 agent 直接查询 CVE 与 exploit 信息
- 安全研究人员用 Streamlit 仪表盘浏览漏洞态势
- 本地构建并维护一份富化后的 CVE 数据库

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L142: `vulnify.mcp` exposes the SQLite database to AI agents over the
> L144: server speaking stdio, so agents like Claude Code, Claude Desktop, and

## 星数曲线

```mermaid
xychart-beta
    title "mez-0/vulnify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4dd818d63dc7` · [字段定义](../../DATASET.md)*
