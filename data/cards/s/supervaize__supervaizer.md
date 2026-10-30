# supervaize/supervaizer

⭐ 15 · Python · MPL-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/supervaize/supervaizer) · [官网](https://runwaize.com) · 组织维护

**把 AI agent 接入 Supervaize Studio 的 Python 控制器 SDK（A2A/A2UI）**

Python 控制器 SDK，实现 A2A 协议的发现、Agent Card、JSON-RPC 控制调用与 SSE 事件，将用户自建 AI agent 的资源、UI Surface、Action 与 Artifact 声明暴露给 Supervaize Studio，由 Studio 渲染为通用运维界面。SDK 本身不含 agent 业务逻辑。提供 CLI（supervaizer start/scaffold/deploy）、内置 Hello World 示例、本地模式与 Docker/云部署（Cloud Run、App Runner、DigitalOcean）。声明处于 Beta 阶段，协议版本固定于注册契约中。Mozilla Public License 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 实现 A2A 协议：发现、Agent Card、JSON-RPC 调用、SSE 事件
- v2 操作契约：Jobs/Cases/Steps/Resources/Surfaces/Actions/Artifacts 与 job.sync 收敛
- 内置 Hello World 示例 agent 与 supervaizer scaffold 脚手架
- deploy CLI 支持构建镜像并部署到 Cloud Run/App Runner/DigitalOcean

## 适用场景

- 把自己的 AI agent 通过 A2A 协议暴露给 Supervaize Studio 统一运营
- 为 agent 声明 UI Surface 与 Action，生成可操作界面
- 本地模式快速验证 v2 控制器行为后部署上云

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: Supervaizer is the Python controller SDK for exposing AI agents to Supervaize Studio through the Supervaizer v2 oper
> L10: - A2A for discovery, Agent Cards, JSON-RPC controller calls, and SSE events

## 星数曲线

```mermaid
xychart-beta
    title "supervaize/supervaizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7174f4587dc1` · [字段定义](../../DATASET.md)*
