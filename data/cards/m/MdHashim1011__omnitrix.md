# MdHashim1011/omnitrix

⭐ 8 · TypeScript · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/MdHashim1011/omnitrix) · 个人维护

**MCP 服务器：把 Claude Code 的任务分派给你已有的其他 AI 账号执行**

运行在 Claude Code 会话内的 MCP 服务器：Claude 负责拆分任务与审核结果，omnitrix 将各任务路由到 Codex、Gemini、DeepSeek、Kimi、GLM、本地模型或任意 OpenAI/Anthropic 兼容 API。读取各账号剩余配额与限流头信息，围绕配额做路由；代码任务在独立 git worktree 执行并自动跑测试；提供 report 与 overhead 命令统计各账号完成/失败/被拒任务数与 token 用量。需 Node.js 20+，npm 安装或作为 Claude Code 插件安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将任务路由到 ChatGPT 计划（经 Codex）、API key 与本地模型的账号池
- 读取剩余配额与限流头，围绕配额重置做路由规划
- 代码任务在独立 git worktree 修改并自动运行指定测试命令
- report/overhead 命令按模型与任务类型统计用量与 Claude 开销

## 适用场景

- Claude 额度紧张时把代码任务转给 ChatGPT/Gemini 等已有账号
- 私密工作路由到本地 Ollama 模型执行
- 让多个模型独立审查同一段代码并交叉核验发现

## 场景标签

`多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: MdHashim1011/omnitrix MCP server
> L13: omnitrix is built for the frontier-model subscriptions and API keys you already pay for, and it runs inside your ex


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `94b7b8efd2a2` · [字段定义](../../DATASET.md)*
