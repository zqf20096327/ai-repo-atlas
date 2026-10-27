# marco-looy/pega-dx-mcp

⭐ 22 · JavaScript · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/marco-looy/pega-dx-mcp) · 个人维护

**让 GenAI Agent 通过自然语言操作 Pega Infinity 应用的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Pega DX API 封装为 67 个工具、11 个类别（案件、任务、附件、数据视图、参与者、标签等），使 Claude Desktop、Claude Code、Cline 等 MCP 客户端能用自然语言创建案件、处理任务、查询数据。支持 OAuth 2.1 with PKCE 认证与按类别启用/禁用工具，Constellation DX API V2 完整支持、V1 部分支持。项目自声明为实验性，非官方 Pega 产品，不建议用于生产。通过 npm 安装，需 Node.js 22+ 与 Pega Infinity 23+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 67 个工具覆盖案件、任务、附件、数据视图等 11 个类别
- Constellation DX API V2 完整支持，V1 提供案件基础操作
- OAuth 2.1 with PKCE 认证，支持 session-only 模式
- 工具类别可按环境变量逐项启用/禁用

## 适用场景

- 在 Claude Desktop/Cline 中用对话创建和流转 Pega 案件
- 让 IDE 里的 AI 助手查询 Pega 任务与数据视图
- 用 MCP 客户端批量管理 Pega 案件附件与参与者

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: This package transforms Pega Infinity&trade; interactions into intuitive, conversational experiences through the Mo
> L93: The Pega DX MCP Server bridges GenAI applications with Pega Infinity using the Model Context Protocol:

## 星数曲线

```mermaid
xychart-beta
    title "marco-looy/pega-dx-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `43c2c0d1d5f0` · [字段定义](../../DATASET.md)*
