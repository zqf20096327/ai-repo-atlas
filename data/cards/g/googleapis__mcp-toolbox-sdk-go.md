# googleapis/mcp-toolbox-sdk-go

⭐ 59 · Go · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/googleapis/mcp-toolbox-sdk-go) · [官网](https://mcp-toolbox.dev/documentation/introduction/) · 组织维护

**Go SDK：让 Go 应用加载并调用 MCP Toolbox 管理的工具**

googleapis 维护的 MCP Toolbox 官方 Go SDK 集合，作为 MCP Toolbox 服务的客户端：从运行中的 Toolbox 实例拉取工具定义、映射为 Go 结构体、调用底层 API/数据库工具，并处理认证与参数绑定。v0.6.0 起改为多模块结构，提供 core（框架无关）、tbadk（ADK Go 集成）、tbgenkit（Genkit Go 集成）三个包，需更新 import 与 go.mod。使用前须自行部署 MCP Toolbox 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个模块：core/tbadk/tbgenkit 分别面向通用应用、ADK 与 Genkit 集成
- 从 Toolbox 实例拉取工具定义并转为 Go 结构体调用
- 处理认证与参数绑定

## 适用场景

- 在 Go 开发的 Agent 应用中调用 MCP Toolbox 管理的数据库/API 工具
- 为 ADK Go 或 Genkit 应用接入 Toolbox 工具集

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L33: This repository contains the Go SDKs for MCP Toolbox. These SDKs allow you to load and use tools defined in your MC
> L41: The MCP Toolbox service provides a centralized way to manage and expose tools

## 星数曲线

```mermaid
xychart-beta
    title "googleapis/mcp-toolbox-sdk-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-26 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `198a9ecf8348` · [字段定义](../../DATASET.md)*
