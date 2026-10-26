# verygoodplugins/mcp-automem

⭐ 66 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/verygoodplugins/mcp-automem) · [官网](https://automem.ai/) · 组织维护

**为 Claude/Cursor 等 AI 工具接入持久图+向量记忆的 MCP 客户端**

连接各类 MCP 兼容 AI 平台与 AutoMem 记忆服务的客户端：通过引导式安装器配置端点与各平台接入，提供 store/recall/update/delete 等记忆工具，支持 11 种关系类型、混合检索与多跳推理（expand_entities 图扩展）。平台侧集成包括 Cursor 项目规则与会话钩子、Claude Code 插件、Copilot 钩子等。需另行运行 AutoMem 后端（本地 make dev、Railway 或 Docker 部署）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- store/recall/associate 等记忆工具，支持批量（≤500 条）与混合排序检索
- 11 种可授权记忆关系类型与多跳推理图扩展
- npx 引导式安装器覆盖 Claude Desktop、Cursor、Claude Code、Codex 等平台
- 可选 HTTP sidecar 支持远程 MCP（ChatGPT connectors、Claude.ai web 等）

## 适用场景

- 让 Claude/Cursor 在会话间记住我的决策、偏好与代码风格
- 多个 AI 工具共享同一份跨设备持久记忆
- 自托管 AutoMem 后端管理个人/项目记忆库

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L187: - MCP client that connects AI platforms to AutoMem
> L193: - Backend memory service with graph + vector storage

## 星数曲线

```mermaid
xychart-beta
    title "verygoodplugins/mcp-automem 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-26 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b64bc36100f0` · [字段定义](../../DATASET.md)*
