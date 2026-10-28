# mhajder/ghostfolio-mcp

⭐ 22 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/mhajder/ghostfolio-mcp) · [官网](https://pypi.org/project/ghostfolio-mcp/) · 个人维护

**让 AI agent 查询与管理 Ghostfolio 投资组合的 MCP 服务器**

基于 Python 和 FastMCP 的 Model Context Protocol 服务器，连接自建或托管的 Ghostfolio 实例，向 AI agent 暴露 40 余个工具：账户与余额管理、持仓与绩效查询、股息与投资数据、交易创建/更新/删除与批量导入导出、基准对比、自选列表、汇率与市场数据、资产档案与符号检索。支持读写与只读模式，提供按标签禁用工具类别、滑动窗口限流、工具搜索（BM25/regex）、SSL/TLS 配置以及 Bearer token 或 OIDC/OAuth 认证。面向希望用 agent 自动化个人投资组合管理的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ 工具覆盖账户、交易、持仓、基准、汇率与市场数据
- READ_ONLY_MODE 只读模式与按标签禁用工具类别
- 限流、日志审计、SSL/TLS、Bearer/OIDC/OAuth 认证
- FastMCP 工具搜索（bm25/regex）缩减大工具集的提示体积

## 适用场景

- 让 AI agent 分析我的投资组合绩效与持仓
- 通过对话创建、导入或导出交易记录
- 以只读模式安全地用 agent 监控账户与股息

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L15: Ghostfolio MCP Server is a Python-based Model Context Protocol (MCP) server designed to provide advanced, programma
> L3: **Let AI agents analyze and manage your Ghostfolio investment portfolio**

## 星数曲线

```mermaid
xychart-beta
    title "mhajder/ghostfolio-mcp 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-19 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5496998a3b2d` · [字段定义](../../DATASET.md)*
