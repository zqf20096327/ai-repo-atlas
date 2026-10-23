# vuetifyjs/mcp

⭐ 115 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/vuetifyjs/mcp) · 组织维护

**向 AI 编程客户端提供 Vuetify 组件文档与 API 的 MCP 服务器**

Vuetify 官方维护的 Model Context Protocol 服务器，把 Vuetify 组件库的 API 类型、文档、安装指南、FAQ、发布说明及 v2→v3→v4 升级手册以工具形式提供给任意 MCP 兼容客户端或 IDE（VS Code、Claude、Cursor、Trae、Windsurf）。可使用官方托管的 HTTP 端点，或通过 npx 本地以 stdio/HTTP 传输运行并自托管；另支持 @vuetify/v0 无头组件与 71 个 composable 的文档查询。Claude Desktop 不支持 HTTP 传输，需 stdio 或 mcp-remote 桥接。

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

- 按版本返回组件/指令的 props、events、slots 等 API 信息
- v2→v3→v4 升级工具：playbook、组件映射、破坏性变更目录
- 托管 HTTP 端点与 npx 本地运行（stdio/HTTP 双传输）均可
- 交互式 CLI 自动检测并配置 5 种受支持 IDE

## 适用场景

- 在 AI 编程助手中生成符合规范的 Vuetify 组件代码
- 升级 Vuetify v2 到 v3 时让 agent 查询组件映射与破坏性变更
- 不离开 IDE 查询 Vuetify 安装指南与 FAQ

## 场景标签

 · 领域:前端开发/AI 工具集成

## 证据(README 行号)

> L8: Model Context Protocol (MCP) server providing Vuetify component information and documentation to any MCP-compatible 
> L323: This project uses the `@modelcontextprotocol/sdk` package to create a Model Context Protocol server that Claude an

## 星数曲线

```mermaid
xychart-beta
    title "vuetifyjs/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-23 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `89daca8c6051` · [字段定义](../../DATASET.md)*
