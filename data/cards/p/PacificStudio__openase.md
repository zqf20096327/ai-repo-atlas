# PacificStudio/openase

⭐ 269 · Go · Apache-2.0 · 推送 2026-08-09 · [GitHub](https://github.com/PacificStudio/openase) · [官网](https://pacificstudio.ai) · 组织维护 · 中文 README

**工单驱动的自动化软件工程平台，AI agent 自动领取并执行工单**

单个 Go 二进制内置 API 服务、工作流编排器与嵌入式 Web UI，采用工单驱动模型：每个工单绑定工作流，AI agent（Claude Code/Codex/Gemini CLI）按状态触发自动领取并在注册的机器上执行，活动流记录每一步。提供异步 Ticket Agent 与同步 Project AI 两种人机交互模式，技能以可复用指令文档扩展 agent 能力，支持多组织、OIDC 登录与 RBAC。默认以宽松权限启动 CLI agent，README 声明不面向公网部署，面向本地开发、内网与可信环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Go 二进制交付 API 服务、编排器与嵌入式 Web UI（运行时无 Node.js）
- 适配 Claude Code / Codex / Gemini CLI 三种 agent CLI，SSE 实时输出
- Markdown Harness 文档约束 agent 行为，技能运行时注入 .codex/.claude/.gemini 技能目录
- 多组织管理、机器管理（本地/直连/反向连接）与 Cron 定时工单

## 适用场景

- 把需求拆成工单，让 AI agent 在自己机器上自动完成开发任务
- 用混合接力模式让多个专职 agent 分工完成设计、前后端与测试
- 通过看板和实时活动流跟踪 agent 执行进度

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L38: OpenASE is a **single Go binary** that ships an API server, workflow orchestrator, and embedded web UI together. It
> L198: |**Multi-agent**|Adapter-based support for Claude Code, Codex, and Gemini CLI|

## 星数曲线

```mermaid
xychart-beta
    title "PacificStudio/openase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-28 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `42698f102226` · [字段定义](../../DATASET.md)*
