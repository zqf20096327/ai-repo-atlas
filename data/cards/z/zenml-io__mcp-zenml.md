# zenml-io/mcp-zenml

⭐ 49 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/zenml-io/mcp-zenml) · [官网](https://www.zenml.io) · 组织维护

**连接 MCP 客户端与 ZenML MLOps/LLMOps 管道的 MCP 服务器**

实现 Model Context Protocol 的服务器，供 Claude Desktop、Cursor、VS Code 等 MCP 客户端访问 ZenML API。默认 compact 档位提供 16 个工具，覆盖用户、Stack、管道、运行、快照、部署、模型注册表等资源的读取、常规变更与触发管道运行；legacy 档位保留 57 个旧工具名用于迁移。通过环境变量切换读写策略（read_only 可移除全部变更工具），日志读取有 50,000 条上限与截断标记。含两个实验性 MCP Apps（运行仪表盘与活动图表），需 Streamable HTTP 传输。版本 2.0.0 要求 MCP Python SDK 2.2.0 与 ZenML 0.96.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- compact 档位 16 个工具：7 个通用资源 CRUD 工具 + 9 个诊断/日志/触发专用工具
- ZENML_MCP_WRITE_POLICY=read_only 可移除全部变更工具，无效配置回退只读
- 触发管道运行支持 Snapshots（推荐）与已弃用的 template 方式
- 两个实验性 MCP Apps：管道运行仪表盘与 30 天活动图表

## 适用场景

- 在 IDE 或聊天客户端中查询 ZenML 管道运行状态、步骤日志与代码
- 通过对话触发新的管道运行并打开仪表盘
- 以只读模式向团队暴露 MLOps 资源信息

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L4: This project implements a [Model Context Protocol
> L6: the ZenML API.
> L26: ZenML is an open-source platform for building and managing ML and AI pipelines.

## 星数曲线

```mermaid
xychart-beta
    title "zenml-io/mcp-zenml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-31 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9f8e40e710e6` · [字段定义](../../DATASET.md)*
