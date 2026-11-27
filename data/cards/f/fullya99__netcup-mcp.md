# fullya99/netcup-mcp

⭐ 10 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/fullya99/netcup-mcp) · 个人维护

**把 netcup VPS 运维 API 以 MCP 工具暴露给 AI 助手的服务器**

一个 Model Context Protocol 服务器，将 netcup SCP REST API 封装为类型化工具，供 Claude Desktop、Claude Code 及任意 MCP 兼容客户端调用，覆盖服务器状态、快照、rDNS、防火墙、任务与指标等运维操作；另提供三个通用工具（list/describe/call_endpoint）访问任意端点，新端点经 spec 更新后无需改代码即可用。鉴权复用 netcup-api CLI 的离线 refresh token，不做交互式登录；MIT 许可，声明与 netcup GmbH 无关联。

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

- 一组面向日常运维的类型化工具（服务器/快照/rDNS/防火墙/任务/指标）
- 通用三工具 list_endpoints/describe_endpoint/call_endpoint 可达任意 API 端点
- 复用 CLI 的离线 refresh token，不做交互式登录
- 提供 NETCUP_MCP_ALL_TOOLS=1 将每个端点展开为独立工具

## 适用场景

- 用自然语言让 AI 助手管理 netcup VPS 的开关机与快照
- 查询服务器清单、指标与异步任务状态
- 生产环境操作前配合客户端审批提示确认破坏性工具调用

## 场景标签

 · 领域:基础设施运维/DevOps

## 证据(README 行号)

> L14: A Model Context Protocol server that exposes the
> L15: netcup Server Control Panel (SCP) REST API to AI assistants —
> L16: Claude Desktop, Claude Code, and any MCP-compatible client.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `b9782baa0b24` · [字段定义](../../DATASET.md)*
