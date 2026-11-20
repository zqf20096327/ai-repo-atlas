# raphaelmansuy/opengenie

⭐ 9 · Python · Apache-2.0 · 推送 2026-11-14 · [GitHub](https://github.com/raphaelmansuy/opengenie) · [官网](https://raphaelmansuy.github.io/opengenie/) · 个人维护

**自托管 Databricks 编码代理应用：可见工作区、自选模型**

一个开源 Databricks App（FastAPI + React 19），在用户自己的 Databricks 工作区中运行编码代理：每个会话启动一个 opencode 代理进程（ACP over stdio），通过 MCP 工具服务器读取/操作 Unity Catalog、SQL 仓库、notebook、Jobs、Lakebase 与 SQL 编辑器，core 档提供 32 个工具。模型作为可配置项，目录内置来自 4 个供应商的 13 个模型并可在运行时发现工作区 serving endpoints。写入受文件夹/Schema/作业名前缀围栏约束，完成声明会与实际工具调用核对。需 Databricks 工作区、Python 3.12、Node.js 20 部署或本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个会话独立的 MCP 工具服务器，以登录用户身份调用 Databricks，Unity Catalog 权限决定代理可见范围
- 模型目录含 4 个供应商 13 个模型，个人 API key 经 Databricks secret 信封加密
- 写入围栏：限定单一文件夹、Schema 与作业名前缀，越界写入被服务器拒绝或需审批
- 证据机制：代理的完成声明与其实际工具调用匹配，未发生的引用会被报告

## 适用场景

- 在 Databricks 数据工程任务中使用可自选模型的自托管编码代理
- 需要写入范围受服务器强制约束的团队协作
- 按任务切换模型或使用已有付费的模型配置

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: what the work costs. OpenGenie is an open-source Databricks App that gives a coding agent the same kind
> L50: Each conversation gets its own MCP tool server. In a deployment it calls
> L81:     A -->|"ACP over stdio"| O["opencode agent<br/>one per conversation"]

## 星数曲线

```mermaid
xychart-beta
    title "raphaelmansuy/opengenie 星数(近 3 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-20"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-11-11 8 → 2026-11-20 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `77a0df43bbc4` · [字段定义](../../DATASET.md)*
