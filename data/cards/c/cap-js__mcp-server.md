# cap-js/mcp-server

⭐ 117 · JavaScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/cap-js/mcp-server) · [官网](https://cap.cloud.sap/docs) · 组织维护

**面向 SAP CAP 开发的 MCP 服务器：让 AI 模型检索 CAP 文档与 CDS 模型**

SAP 官方团队 cap-js 维护的 Model Context Protocol 服务器，用于 CAP 应用的 AI 辅助开发（agentic coding）。提供两个工具：search_docs 用向量嵌入在本地对预处理 CAP 文档做语义检索，search_model 对编译后 CDS 模型的定义名做模糊搜索（含注解与 HTTP 端点）。通过 npx 启动，可接入 Claude Code、Cline、opencode、OpenAI Codex、GitHub Copilot 等 MCP 客户端，也提供 cds-mcp CLI 直接调用。支持嵌入模型选择、本地重排序（交叉编码器，默认关闭）、离线模式等环境变量配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- search_docs：本地向量嵌入语义检索 CAP 文档
- search_model：对编译后 CDS 模型定义名做模糊搜索
- 接入 Claude Code / VS Code(Cline/Copilot) / OpenAI Codex / opencode 等多种 MCP 客户端
- 提供 cds-mcp CLI 直接调用工具，支持本地交叉编码器重排序

## 适用场景

- 在 AI 编码助手中查询 CAP 项目的 CDS 服务与实体定义
- 开发 CAP 应用时让 AI 按 CAP 官方文档写代码
- 通过命令行快速检索 CAP 文档与模型定义

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server for the SAP Cloud Application Programming Model (CAP).
> L8: Use it for AI-assisted development of CAP applications (_agentic coding_).

## 星数曲线

```mermaid
xychart-beta
    title "cap-js/mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-27 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `84e6b87f5130` · [字段定义](../../DATASET.md)*
