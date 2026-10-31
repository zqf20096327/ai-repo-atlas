# whyashthakker/beam-cli

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/whyashthakker/beam-cli) · [官网](https://www.agentbeam.com) · 组织维护

**本地 AI agent 安全与监控层：安装钩子捕获活动并执行策略**

AgentBeam 是面向 AI coding agent 的本地安全层 CLI（beam）。beam setup 检测机器上已安装的 agent（Claude Code、Codex、Gemini CLI、Cursor、Copilot CLI 等），为其安装原生 pre-tool 钩子，清点 MCP 服务器，应用组织策略（审批/阻止/脱敏/记录敏感变量、密钥、越界文件、破坏性命令），并将遥测发送至 AgentBeam dashboard。另含 WipeBench 编码 agent 安全基准（112 场景）、可选 Jev/任意 LLM 动作审判、应用日志监控（beam monitor）与 CVE 检查。通过 npm 全局安装，策略依赖云端 dashboard。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 8+ 种 agent 安装原生 pre-tool 钩子并捕获 agent 与 MCP 活动
- 本地策略执行：审批/阻止/脱敏/记录密钥、.env、越界文件、破坏性命令
- WipeBench 安全基准：112 场景、12 类别、Docker 内评测
- 可选 beam judge：任意 OpenAI 兼容端点（含 Ollama/vLLM）或自建决策服务给出 allow/review/deny

## 适用场景

- 给团队的 coding agent 加统一的密钥与破坏性操作防护策略
- 集中清点与审计 agent 的 MCP 服务器使用情况
- 监控应用日志中的攻击迹象并做依赖 CVE 检查
- 评测 coding agent 任务完成与有害副作用（WipeBench）

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: AgentBeam is a local security layer for AI agents. `beam` is the AgentBeam CLI. It installs hooks for the agents det
> L64: Depending on organization policy, AgentBeam can ask for approval, block, redact, or log:
> L79: |Agent|Hook support|

## 星数曲线

```mermaid
xychart-beta
    title "whyashthakker/beam-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `09cbcc53898a` · [字段定义](../../DATASET.md)*
