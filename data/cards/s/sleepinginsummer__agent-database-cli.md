# sleepinginsummer/agent-database-cli

⭐ 35 · Rust · MIT · 推送 2026-10-26 · [GitHub](https://github.com/sleepinginsummer/agent-database-cli) · [官网](https://www.npmjs.com/package/agent-database-cli) · 个人维护 · 中文 README

**面向 Agent 的多数据库本地 CLI：连接、查询、元信息与权限控制**

用 Rust 编写、经 npm 分发二进制的本地 CLI 工具，将 MySQL、PostgreSQL、Redis（含集群）、Oracle、MongoDB 的连接管理、SQL/命令执行、元信息读取封装为 Agent 可调用的命令。内置本地 daemon 复用连接，支持按连接配置只读模式（默认开启）与命令黑名单，密码等敏感信息本地加密存储；支持 SSH 隧道访问数据库，Oracle 默认走 SQLcl。附带本机 Web 编辑页面用于改配置并原子落盘，只监听 127.0.0.1、随机令牌鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MySQL/PostgreSQL/Redis(单机+集群)/Oracle/MongoDB 五类数据库
- 默认只读模式 + 命令黑名单双层权限控制
- 密码/密钥本地加密保存，配置文件不保留明文
- 本地 daemon 连接复用与 SSH 隧道（含 Redis 集群逐节点转发）

## 适用场景

- 让 Claude Code / Codex 等 Agent 安全查询我的数据库
- 生产库默认只读，按黑名单拦截高危命令
- 通过本机页面可视化编辑和校验数据库连接配置

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L20: `agent-database-cli` 是一个面向 Agent 的本地多数据库 CLI 工具，用 Rust 封装 MySQL、PostgreSQL、Redis、Oracle、MongoDB 的连接、查询、元信息读取、只读控制、命
> L3: 基于 CLI 的多数据库操作工具，将常见数据库连接、查询、元信息读取和连接复用能力封装为 Agent 可调用的本地命令。

## 星数曲线

```mermaid
xychart-beta
    title "sleepinginsummer/agent-database-cli 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-19 35 → 2026-10-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `01a255a8e015` · [字段定义](../../DATASET.md)*
