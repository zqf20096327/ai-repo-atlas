# keurcien/auxilia

⭐ 23 · HTML · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/keurcien/auxilia) · 个人维护

**面向团队的自托管 Web 端 MCP AI 助手运行平台**

开源自托管的 Web 平台，供团队集中运行基于 MCP 的 AI 助手：管理员一次性注册远程 MCP 服务器与助手，全工作区共享，成员无需技术背景即可创建助手，支持浏览器或 Slack 对话、人工审批敏感操作、定时触发与后台运行。技术栈为 FastAPI 后端加 Next.js 前端，基于 LangGraph 构建，附带 PostgreSQL 与 Redis 的 Docker Compose 部署。可选 Anthropic、OpenAI、Google、DeepSeek 等多家 LLM 提供商并随时切换；仅支持远程（Streamable HTTP）MCP 服务器。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作区级统一注册远程 MCP 服务器与助手，按助手配置工具审批规则
- 人工在环审批、定时触发与 Redis 支撑的后台运行
- 代码沙箱（OpenSandbox/Cloud Run/Daytona）与 SKILL.md 格式技能库
- 支持多家 LLM 提供商切换，Langfuse 追踪与成本归因

## 适用场景

- 团队共享一套 MCP 助手，避免每人各自配置提示词与凭据
- 业务人员无代码搭建并在 Slack 中使用 AI 助手
- 敏感工具调用前经人工审批后执行
- 定时任务与后台长时间运行助手并回看结果

## 场景标签

`AI 助手` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: **auxilia is a web platform for running AI agents as a team.** An admin sets up MCP servers and agents once, and th
> L64: |🤖 **Agents**|System prompt, avatar, and bound MCP servers per agent. Coordinator agents dispatch work to **subagen
> L144:  Built with ❤️ using LangGraph and the Model Context Protocol.

## 星数曲线

```mermaid
xychart-beta
    title "keurcien/auxilia 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a753efe2c0a9` · [字段定义](../../DATASET.md)*
