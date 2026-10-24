# googleapis/mcp-toolbox-sdk-js

⭐ 77 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/googleapis/mcp-toolbox-sdk-js) · [官网](https://mcp-toolbox.dev/documentation/introduction/) · 组织维护

**在 JS Agent 应用中加载 MCP Toolbox 工具的 SDK**

Google 维护的 JavaScript/TypeScript SDK 集合，用于连接运行中的 MCP Toolbox 服务器，将其定义的工具以标准 JS 函数或对象形式加载进 Agent 应用。提供框架无关的 core 包与面向 ADK 应用的 adk 包两个 npm 包，均以 TypeScript 编写。使用前提是已有运行中的 MCP Toolbox 服务器，详细配置依赖主文档站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 MCP Toolbox 服务器定义的工具加载为标准 JS 函数/对象
- 框架无关的 core 包与面向 ADK 应用的 adk 包
- 以 npm 包形式发布，TypeScript 编写

## 适用场景

- 在自研 Agent 应用中调用 MCP Toolbox 定义的数据库工具
- 在 ADK 应用中接入 Toolbox 工具集

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: This repository contains JavaScript SDKs for MCP Toolbox. These SDKs allow you to load and use tools defined in you
> L24: |`@toolbox-sdk/core`|Framework-agnostic / Custom apps|`packages/toolbox-core/`|JS Core Guide|

## 星数曲线

```mermaid
xychart-beta
    title "googleapis/mcp-toolbox-sdk-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-24 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cc9f96175d3c` · [字段定义](../../DATASET.md)*
