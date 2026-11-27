# linkzy/symbio

⭐ 3 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/linkzy/symbio) · [官网](https://symbio.linkzy.dev) · 个人维护

**在浏览器里协调多 AI agent 团队协作同一项目的本地 Web 应用**

Symbio 是本地运行的 Node.js 服务器加 React UI：用户与一个 lead agent（core）对话，core 规划任务并委托给若干 helper agent，各 helper 在独立的 git worktree 副本中并行工作，通过消息机制互相沟通，需要决策时向用户提问。agent 运行在可选的 runtime（OpenCode 或 GitHub Copilot CLI）上，每个任务有 Done-when 检查与 reviewer 复核，工具调用受安全规则约束。局限：单人使用、无账号共享、非沙箱隔离，仅在 Windows 11 上经过开发与使用测试。

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

- core 规划任务并创建 helper，各 helper 在独立 git worktree 并行工作
- 每个 runtime（OpenCode / GitHub Copilot CLI）通过统一 AgentRuntime 接口接入
- 工具调用安全规则检查、凭据加密存储、崩溃恢复与 watchdog
- 实时看板、任务成本统计、手机远程访问布局

## 适用场景

- 在浏览器里指挥一支 agent 团队完成代码、文档、研究类项目
- 让多个 agent 并行处理任务而不互相覆盖编辑
- 对 agent 的花费、部署、删除等操作设置需要人工批准的权限

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L17: cleanup, a set of documents. Symbio provides the machinery (messaging, isolation, coordination,
> L147: Symbio is a Node.js server with a React UI, bound to your computer only. Each agent is a session of
> L154: - **One interface, two runtimes.** The team logic only knows `AgentRuntime`. The Copilot adapter


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `eecf918b8656` · [字段定义](../../DATASET.md)*
