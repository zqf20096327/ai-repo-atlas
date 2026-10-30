# kud/mcp-jenkins

⭐ 19 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/kud/mcp-jenkins) · [官网](https://kud.io/projects/mcp-jenkins) · 个人维护

**让 AI 客户端通过 MCP 操作 Jenkins 的服务器（38 工具）**

TypeScript/Node.js 实现的 Jenkins MCP 服务器：向 Claude 等 MCP 客户端暴露 38 个工具，覆盖 Jenkins API 的任务管理、构建触发与停止、流水线阶段状态、控制台日志、测试结果、构件、队列、节点开关与系统操作。支持 API token 与 bearer token 两种认证，可经逗号分隔环境变量同时连接多个 Jenkins 实例；每请求默认 30 秒超时可用环境变量调整，也可按工具名设置允许/屏蔽清单。通过 npm 全局安装或 npx 免安装运行。

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

- 38 个工具覆盖任务/构建/流水线/队列/节点/插件等操作
- 支持 classic API token 与 bearer token 认证
- 多 Jenkins 实例同时连接（逗号分隔环境变量）
- npx 免安装直接运行，超时与工具可见范围可配置

## 适用场景

- 在 AI 客户端中触发构建并跟踪流水线阶段与日志
- 通过对话管理 Jenkins 任务、节点与队列
- 统一对接公司内多个 Jenkins 实例

## 场景标签

 · 领域:开发工具/CI-CD 集成

## 证据(README 行号)

> L6: **Jenkins MCP server with bearer token authentication support**
> L12: - **38 tools** — covers ~95% of the Jenkins API: jobs, builds, nodes, views, queue, plugins, and system operations

## 星数曲线

```mermaid
xychart-beta
    title "kud/mcp-jenkins 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e5daa3bc769d` · [字段定义](../../DATASET.md)*
