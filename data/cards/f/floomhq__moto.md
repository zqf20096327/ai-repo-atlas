# floomhq/moto

⭐ 32 · Shell · MIT · 推送 2026-06-10 · [GitHub](https://github.com/floomhq/moto) · [官网](https://github.com/floomhq/moto#readme) · 组织维护

**面向 Claude Code/Codex 的终端 AI agent 运行环境与安全框架**

Floom 从 500+ 真实会话中提取的终端 AI agent 操作环境：以 Claude Code 为控制平面、Codex 与 opencode 作为 worker，提供 17 个安全钩子（拦截破坏性命令、密钥泄漏）、60+ skills 斜杠命令、MEMORY.md 跨会话记忆、Docker 沙箱、远程 Linux 运行时（moto up + SSHFS + systemd + tmux）、Chrome CDP 浏览器自动化、WhatsApp/Gmail 集成与 token 成本追踪。面向创始人、Claude Code/Codex 用户与团队。通过 install.sh 安装，明确声明不替代 Claude Code，而是其外围环境。必需依赖为 Claude Code CLI 与 jq。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个安全钩子在每次工具调用时拦截破坏性命令与密钥泄漏
- 60+ skills 斜杠命令（/cost、/qa、/ship、/debug 等）
- Mac 控制平面 + 远程 Linux Docker 运行时的分体架构
- 按模型、按会话的 token 成本追踪与 Groq/Gemini/NVIDIA 廉价模型分流

## 适用场景

- 把重复工作流程固化为带钩子和技能的 agent 运行环境
- 多 agent 并行开发时防止破坏性命令和密钥泄漏
- 在远程服务器上运行长时间 agent 会话与容器沙箱

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8: `moto` is Floom's terminal IDE for AI agents: Claude as the control plane, Codex for backend/infra/debugging, openco
> L26: Most AI coding setups are a prompt file plus a pile of tools. `moto` is the full operating environment: context, ho
> L106: No. It's the operating environment around Claude Code (and Codex, and opencode). You still use Anthropic's CLI; mo

## 星数曲线

```mermaid
xychart-beta
    title "floomhq/moto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c15ff65adbdf` · [字段定义](../../DATASET.md)*
