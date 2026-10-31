# karem505/claudecodex

⭐ 35 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/karem505/claudecodex) · [官网](https://aboelmakarem.pro) · 个人维护

**让 Claude Code 以 ChatGPT 订阅驱动的 GPT-5.6 为引擎的启动器**

面向已订阅 ChatGPT Plus/Pro 的开发者的薄启动器：启动真实 Claude Code CLI，将其指向本地 127.0.0.1:18765 的 Anthropic 兼容代理（claude-code-proxy），代理通过 Codex 订阅认证把请求转发到 GPT-5.6（Sol/Terra/Luna），从而无需 Anthropic 或 OpenAI API key。所有环境变量仅进程内生效，不改写原生 claude 配置；支持模型切换、372K 上下文设定与权限旁路开关。需先安装 Claude Code CLI 与代理并完成 OAuth 登录；README 声明将订阅路由至非官方客户端属 OpenAI 条款灰色地带，仅供个人本地使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Anthropic 兼容代理转发至 Codex 订阅后端的 GPT-5.6
- 环境变量仅进程内生效，不影响原生 claude 登录与设置
- 支持 Sol/Terra/Luna 三档模型切换与 max 推理档位
- 一行 curl 脚本安装，卸载仅需删除单文件

## 适用场景

- 用已有的 ChatGPT Plus/Pro 订阅运行 Claude Code，避免按 token 计费
- 在保留 Claude Code 工作流（文件编辑、MCP、skills）的同时使用 GPT-5.6 模型
- 按任务在 Sol/Terra/Luna 间快速切换模型档位

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L23: claudecodex launches the real Claude Code UI, points it at a local
> L24: Anthropic-compatible proxy on 127.0.0.1:18765, and the proxy forwards requests
> L30:    → local Anthropic-compatible proxy (127.0.0.1:18765)

## 星数曲线

```mermaid
xychart-beta
    title "karem505/claudecodex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-31 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00600a1864bb` · [字段定义](../../DATASET.md)*
