# AndurilCode/mcp-apps-kit

⭐ 16 · TypeScript · MIT · 推送 2026-04-14 · [GitHub](https://github.com/AndurilCode/mcp-apps-kit) · [官网](https://kanban.mcpappskit.com/mcp) · 个人维护

**单一代码库构建 MCP Apps 与 ChatGPT 交互应用的 TypeScript 框架**

面向开发者的 TypeScript 框架，通过文件约定（tools/、ui/widgets/、workflows/ 目录）自动发现并生成工具、React 小部件与工作流，免除手工维护 manifest。单一代码库可同时部署到 MCP Apps 与 ChatGPT（OpenAI Apps SDK），支持工具调用、结构化输出、OAuth 2.1、中间件、事件处理与多版本 API。提供 CLI 脚手架、codegen 监听与 Vite HMR，部署支持 Express、stdio 与 Serverless。要求 Node.js >=18（开发 >=20）、React 18/19、Zod ^4、Vite 5-7。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件约定自动发现 tools/widgets/workflows，codegen 生成 manifest
- 单一代码库双平台部署到 MCP Apps 与 ChatGPT
- 7 个 npm 包：core/codegen/ui/ui-react/testing 等
- 支持中间件、事件处理、工作流引擎与 Serverless 部署

## 适用场景

- 开发同时接入 MCP Apps 和 ChatGPT 的交互式 AI 应用
- 以文件目录约定快速搭建带 React 小部件的 MCP 工具服务
- 将 MCP 应用部署到 Express、stdio 或 Serverless 环境

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L4:  Build interactive AI apps for MCP Apps and ChatGPT. The Modern TypeScript Way.
> L35: |**Dual Platform**|Single codebase deploys to MCP Apps & ChatGPT|

## 星数曲线

```mermaid
xychart-beta
    title "AndurilCode/mcp-apps-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f996a2e5920a` · [字段定义](../../DATASET.md)*
