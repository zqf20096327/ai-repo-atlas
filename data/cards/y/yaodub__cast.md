# yaodub/cast

⭐ 41 · TypeScript · MIT · 推送 2026-08-23 · [GitHub](https://github.com/yaodub/cast) · [官网](https://getcast.dev) · 个人维护

**本机自托管多用户 Claude agent 编排框架**

在用户自己的机器上运行一组 AI agent 的开源框架（MIT，开发者 alpha）。每个 agent 是一个文件夹，用自然语言描述任务；agent 运行在容器内，网络仅限模型提供方与白名单域名，邮件/日历/网页等操作由容器外代码以固定动作执行，消息经身份校验，服务凭据不进入容器。支持多用户隔离会话、定时/事件触发的常驻任务，以及通过 Design 控制台或 Claude Code 技能两种构建方式。运行需容器运行时（macOS Apple Container、Linux/WSL2 Docker）、Node 20+ 和 Claude 凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 以容器隔离运行，网络限模型提供方与白名单域名
- 邮件/日历/网页动作在容器外以固定动作执行，凭据不入容器
- 多用户：每人与 agent 的会话、权限、历史相互隔离，首条消息需批准
- 支持定时/账户事件触发的常驻任务（watch），可列出并撤销

## 适用场景

- 让 agent 长期照看邮箱、仓库、家庭日程等常驻事务
- 在自有机器上安全地给 agent 接入真实账户
- 多人共享同一 agent 但保持各自私有会话与权限

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: Cast runs a small team of AI agents on your own machine. An agent is a folder, and you write its job in plain Engli
> L13: Each agent runs in a container whose network only reaches the model provider and any domains you whitelist. Its onl
> L33: `pnpm start` installs, builds, builds the agent container image (~2 min the first time), and boots the server. You'

## 星数曲线

```mermaid
xychart-beta
    title "yaodub/cast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bcd2fc6b603e` · [字段定义](../../DATASET.md)*
