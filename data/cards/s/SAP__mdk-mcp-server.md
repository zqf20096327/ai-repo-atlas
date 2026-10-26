# SAP/mdk-mcp-server

⭐ 38 · JavaScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/SAP/mdk-mcp-server) · 组织维护

**面向 SAP MDK 开发的 MCP 服务器：让 AI 代理成为 MDK 开发专家**

由 SAP 开源的 Model Context Protocol 服务器，向 AI 代理提供 MDK 最佳实践知识、项目上下文、项目模板与 MDK CLI 工具访问能力，支持生成新项目、页面/动作/i18n 构件、规则示例检索，以及构建、部署、校验、迁移、生成二维码等项目管理操作。面向使用 Cline、Claude Code、Cursor、OpenCode 等 MCP 客户端的 MDK 开发者。通过 npm 安装或源码构建，需 Node.js 24.11.1；与 SAP Mobile Services 集成依赖 Cloud Foundry CLI 与 .service.metadata 文件。macOS 仅支持 Apple Silicon（Intel Mac 需 Rosetta 2 或旧版本）。

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

- mdk-create/mdk-gen/mdk-manage 三类工具覆盖项目创建、构件生成与管理操作
- 页面生成支持 15 种控件类型、布局生成支持 6 种布局类型
- 构建/部署/校验/迁移/二维码等 MDK 项目管理操作集成于单一工具
- 提供 Cline、Claude Code、Cursor、OpenCode、Claude Desktop 配置说明

## 适用场景

- 通过 AI 代理初始化并生成 MDK 项目与页面/动作构件
- 让 AI 代理完成 MDK 项目的构建、部署与校验
- 检索 MDK 规则示例与文档中的控件属性信息
- 将旧 MDK 项目迁移到最新 schema

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: This open-source server provides AI agents with comprehensive MDK knowledge and tools. By combining best practice gu
> L204: This release of the MDK MCP server includes the following tools, which can be accessed by your AI agent:
> L210: |`mdk-manage`|Comprehensive MDK project management tool that handles build, deploy, validate, migrate, show QR cod

## 星数曲线

```mermaid
xychart-beta
    title "SAP/mdk-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-26 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `66ed5e4b0971` · [字段定义](../../DATASET.md)*
