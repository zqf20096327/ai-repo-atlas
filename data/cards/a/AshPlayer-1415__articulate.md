# AshPlayer-1415/articulate

⭐ 3 · JavaScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/AshPlayer-1415/articulate) · [官网](https://ashplayer-1415.github.io/articulate/) · 个人维护

**为编码 agent 构建个人工作偏好档案并在工具间共享的本地 CLI/MCP 服务**

以本地 CLI 与 MCP 服务器形式运行，从 Codex、Claude Code、Cursor 的活动记录中提取用户协作偏好，生成经人工审核的工作档案与项目上下文；按客户端逐个授权分发，Claude Desktop 可消费已审核上下文。需特定补丁版本的 Node.js，无需 Docker、账号或 API key；偏好仅约束呈现与协作方式，不承诺事实准确性提升。npm 公测版本 0.0.1，可选云端服务尚未上线。

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

- 本地 CLI + MCP 服务器，无需 Docker、账号或 API key
- 从 Codex/Claude Code/Cursor 活动提取偏好并生成建议供审核
- 按客户端逐个授权分享，设置本地备份
- 支持 Work/Personal/项目专属多档案与带输入校验的快捷过程

## 适用场景

- 让不同编码 agent 遵循同一套经审核的个人协作偏好
- 为新项目快速携带既有工作上下文与流程约定
- 控制哪些 agent 能读取哪些上下文片段

## 场景标签

`Agent 记忆` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L30: It runs as a local CLI and MCP server. It can use available Codex, Claude Code
> L11: Articulate helps you build reviewed working profiles and carry useful preferences


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `be8207821985` · [字段定义](../../DATASET.md)*
