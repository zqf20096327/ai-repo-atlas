# shisa-ai/shisad

⭐ 30 · Python · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/shisa-ai/shisad) · [官网](https://shisa.ai/) · 组织维护

**安全优先的 AI agent 守护进程：模型提议动作，运行时裁决执行**

长期运行的后台守护进程，将 LLM 连接到工具、文件、网络与消息通道（Matrix/Discord/Telegram/Slack）。核心机制是模型只提议动作，ShisaD 的策略执行点（PEP）在执行前校验工具与参数、检查权限与资源访问、标记不可信内容并按需要求确认；COMMAND/TASK 会话隔离、摘要防火墙、五路行为监控、破坏性命令拦截与完整审计日志构成运行时强制体系。支持 Shisha/OpenAI/OpenRouter/Google/本地 vLLM 多路由。当前 v0.8.3，处于重度开发阶段，面向开发者，推荐运行于专用实例或容器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 动作执行前经 PEP 校验：权限、网络目的地、凭据、密钥扫描与污染内容规则
- COMMAND/TASK 会话隔离与摘要防火墙，隔离不可信内容的委托工作
- 五路独立监控跨动作检测可疑行为，含确认门与 lockdown 机制
- 多消息通道接入与多模型路由（含本地 vLLM），可混合本地与远程模型

## 适用场景

- 通过 Matrix/Discord/Telegram/Slack 长期运行一个受策略约束的个人 agent
- 在处理不可信内容（网页、邮件、工具输出）时防止提示注入接管 agent
- 以带审计与确认流程的方式让 agent 操作文件、Git 与浏览器自动化任务

## 场景标签

 · 领域:AI agent 基础设施/安全

## 证据(README 行号)

> L5: ShisaD is a long-running daemon that connects an LLM to tools, files, networks,
> L37: - **Actions are checked before execution** — planner actions pass through the
> L84: - **Flexible model routing** — configure Shisa, OpenAI, OpenRouter, Google, and

## 星数曲线

```mermaid
xychart-beta
    title "shisa-ai/shisad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4ed8aa7bfd27` · [字段定义](../../DATASET.md)*
