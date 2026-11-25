# autonomous-loop-studio/Autonomous

⭐ 3 · JavaScript · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/autonomous-loop-studio/Autonomous) · [官网](https://autonomous-loop-studio.github.io/Autonomous/) · 个人维护

**自托管 AI agent 控制台：让任意模型在本地跑真实工具**

用纯 PHP 实现的自托管多 agent 控制台，一个源码文件夹部署在已有主机上，不依赖 Docker、Node 或构建步骤。核心循环：探测每个模型的工具调用方言（JSON、Claude XML、原生 tool-call 标签），失败时按方言序列重试，并按 provider+model 记住有效方言。提供文件读写沙盒、allowlist 命令、DevTools 驱动浏览器、git、MCP 调用；带步数/时限上限、上下文压缩、训练 drill 与 3D 运行地图。安全默认关闭 exec、浏览器与 MCP server，无 token 时拒绝服务。

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

- 工具方言探测与按模型记忆的有效方言重试机制
- 支持 6-17 步训练 drill，逐项执行并重试至通过
- 步数上限、时限、ask_agent 无环链与重复调用抑制
- 写操作逐次确认，exec/浏览器/MCP 默认关闭

## 适用场景

- 用笔记本上的 7B/8B 本地模型跑 agent 团队
- 在自有服务器上自托管多 agent 工作台而不引入 Docker/Node
- 按 provider 实际限速编排多 key 轮换与节流

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A self-hosted agent console in plain PHP.** No Docker. No Node. No build step. No account.
> L15: Autonomous Loop Studio — a self-hosted AI agent console in plain PHP
> L47: - 🤖 **Any model, any provider.** It detects each provider's API shape *and* its tool dialect —

## 星数曲线

```mermaid
xychart-beta
    title "autonomous-loop-studio/Autonomous 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `8f5095a97bb7` · [字段定义](../../DATASET.md)*
