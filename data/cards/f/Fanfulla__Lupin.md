# Fanfulla/Lupin

⭐ 35 · TypeScript · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/Fanfulla/Lupin) · [官网](https://www.npmjs.com/package/lupin-code) · 个人维护

**让 Claude Code 接入任意 LLM 提供商的本地代理路由器**

本地优先的代理与 CLI：把 Claude Code 的 API 流量指向 Lupin，从而在保留 MCP 服务器、技能、hooks、插件与项目指令的前提下切换模型。支持四种路由通道（passthrough/responses/codeassist/translate），凭据路径覆盖 API key、OAuth 订阅登录（含 ChatGPT、Kimi、Google Code Assist、GitHub Copilot）与 Ollama/LM Studio 等本地运行时；提供 failover、会话内切模型、Rust TUI 引导设置，以及基于真实 headless 会话与磁盘产物的逐模型兼容性评分命令 lupin doctor。代理仅绑定 127.0.0.1，提示词与响应不持久化。需 Node.js ≥20 与 PATH 中的 claude，TUI 需 Rust 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- lupin doctor：真实 headless Claude Code 会话评分，依据磁盘产物而非模型自述
- 四种路由通道，passthrough 优先避免格式翻译
- 会话进行中切换模型/配置，会话不中断
- 凭据存于 OS 钥匙串，代理仅绑定 127.0.0.1，提示词不持久化

## 适用场景

- 在 Claude Code 里改用 Kimi、ChatGPT、Gemini 等订阅或 API key 模型
- 配额用尽时在会话内切换到另一提供商继续任务
- 在接入前先测某模型能否满足 Claude Code harness 的任务要求
- 让 Ollama/LM Studio 本地模型跑在 Claude Code 界面里

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21:  Claude Code, on any model.
> L30: Your whole setup lives in Claude Code, not in the model: MCP servers, skills, `CLAUDE.md`, hooks, memories, plugins
> L67: That command starts Claude Code with its API traffic pointed at Lupin. Your

## 星数曲线

```mermaid
xychart-beta
    title "Fanfulla/Lupin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `003e790a4608` · [字段定义](../../DATASET.md)*
