# dunialabs/kimbap

⭐ 16 · Go · 推送 2026-04-20 · [GitHub](https://github.com/dunialabs/kimbap) · [官网](https://kimbap.sh) · 组织维护

**把 REST API/CLI/macOS 应用封装成 agent 可安全调用的 CLI 运行时**

面向 AI agent 开发者的 CLI 运行时与安全层：用一个 YAML 清单将 REST API、本地 CLI、macOS 原生应用封装为可直接调用的命令（kimbap call），支持从 OpenAPI 3.x 规范生成服务定义。凭据在执行时由加密保管库注入，不进入 agent 进程；每个动作经过策略检查、审批与审计，输出过滤可裁剪 API 响应（宣称减少 83-94% token）。内置大量 SaaS、开发者 CLI 与 macOS 服务适配，兼容 Claude Code、OpenCode、Codex 等 agent。提供 curl 脚本与 Homebrew 安装，Go 编写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个 YAML 清单封装 REST API/CLI/macOS 应用三类适配器
- 凭据执行时注入加密保管库，不进入 agent 进程
- 每动作经过策略检查、审批与自动审计日志
- 可从 OpenAPI 3.x 规范生成服务定义
- 四种集成模式：call/run/proxy/serve 共享同一安全管线

## 适用场景

- 让 AI agent 安全调用 GitHub/Slack 等 SaaS API 而不暴露密钥
- 把内部 REST API 快速封装成 agent 可用的 CLI 工具
- 对 agent 执行的动作做策略审批与审计追踪
- 裁剪 API 响应降低 agent 的 token 消耗

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: > **Turn anything into a CLI your agent can use. Securely.**
> L57: ```bash
> L64: Works with Claude Code, OpenCode, Codex, OpenClaw, NanoClaw, and any agent that can run a CLI command.

## 星数曲线

```mermaid
xychart-beta
    title "dunialabs/kimbap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `de01859afd2f` · [字段定义](../../DATASET.md)*
