# Azzurroooo/rind

⭐ 18 · JavaScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Azzurroooo/rind) · [官网](https://rindai.dev) · 个人维护 · 中文 README

**多 agent 协作 CLI：把文件夹变成各有工作区的 teammate**

以『文件夹即 agent』为核心的多 agent 协作运行时：每个 agent 绑定一个工作区（文件为上下文、RIND.md 存常驻指令、技能可复用），lead 委派、专家实现/测试/评审后交付。按需加载执行上下文，空闲时释放执行容器与模型客户端，会话历史存于磁盘文件，无需数据库服务。提供 CLI、Desktop、Web、移动客户端与 Telegram/Discord/Slack/飞书网关，支持 OpenAI 账号登录及 OpenAI/Anthropic/Google/DeepSeek 等 API-key 接入，可用 rind run 接入脚本与 CI。需 Node.js 18+，源码构建另需 Python 3.12+。

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

- 文件夹即 agent：每 agent 独立工作区，RIND.md 常驻指令与可复用技能
- 按需加载、空闲释放执行容器，会话历史落盘无需数据库
- CLI/Desktop/Web/移动客户端共享同一运行时，支持自托管
- rind run 非交互模式输出到 stdout，可接入脚本与 CI

## 适用场景

- 给一个目标，让 lead 委派多个 agent 并行开发、测试与评审
- 在 Telegram/Discord/Slack/飞书里继续与 agent 对话
- 用 rind run 在 CI 中自动审查 diff 并产出报告

## 场景标签

`多智能体` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L25: **Add workspaces to your team. Let each agent work in its own folder.**
> L71: Rind supports OpenAI account sign-in alongside API-key connections to OpenAI, Anthropic, Google, DeepSeek and other

## 星数曲线

```mermaid
xychart-beta
    title "Azzurroooo/rind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `23189b3449fd` · [字段定义](../../DATASET.md)*
