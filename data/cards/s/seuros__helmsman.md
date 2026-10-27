# seuros/helmsman

⭐ 24 · Rust · 推送 2026-10-25 · [GitHub](https://github.com/seuros/helmsman) · 个人维护

**为 AI 编程 agent 按模型与环境动态生成指令的 MCP 服务器**

用 MCP（及 CLI）替代静态 AGENTS.md 的指令服务器：基于 Jinja2 模板，按模型能力分层（monkey/engineer/agi 三档，预配置 Anthropic/OpenAI/Google 等映射）自动调节指令详略，并自动探测 OS、shell 与可用工具以适配环境。技能文件置于 .skills/ 自动发现，配置支持项目级与用户级 toml。环境探测为尽力而为；明确不做提示工程框架、无跨调用状态。以 Rust 编写，cargo install 安装，BSD-3-Clause 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型三档分层（monkey/engineer/agi）动态调整指令详略
- Jinja2 模板注入模型与环境上下文
- 自动探测 OS、shell、可用工具
- 提供 MCP 服务器模式与 CLI 两种使用方式

## 适用场景

- 让不同能力的模型收到不同详略的项目指令，节省 token 并减少失误
- 跨机器/系统环境下让 agent 指令自动适配本机工具链
- 通过 MCP 接入 Claude 类编程 agent 工作流

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L20: Helmsman serves **dynamic, context-aware instructions** via MCP (and CLI):
> L100: helmsman                              # MCP server mode

## 星数曲线

```mermaid
xychart-beta
    title "seuros/helmsman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b857b49fb3c0` · [字段定义](../../DATASET.md)*
