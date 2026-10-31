# oll4com/spaceapp

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/oll4com/spaceapp) · [官网](https://spaceapp.dev) · 组织维护

**自托管工作区：并排运行多个 AI 编码 CLI 的统一驾驶舱**

面向使用 AI 编码助手的开发者的自托管工作区：在持久化 room 中并排运行 16 种 AI 编码 CLI（OpenCode、Codex、Claude Code、Gemini、Qwen、Kimi、Grok、DeepSeek 等），每个 CLI 用自己的账号并共享技能、MCP 服务器与记忆。核心机制包括 Nous 统一调度（读各 pane 进度报告、只把四类决策交给用户）、Vault 浏览器端加密登录、Space Gateway 模型账户网关、可选 PostgreSQL+pgvector 3D 向量记忆图，以及 6 个 copilot 与 3 个 studio 可选模块。一条 npx 命令完成安装（缺失时自动装 Docker），支持 Linux/macOS/Windows 11。限制：room 不是互不信任用户间的安全边界，copilot/studio 默认不启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 种 AI 编码 CLI 并排运行，共享技能、MCP 服务器与记忆
- Nous 统一调度：读 pane 进度报告，仅四类决策需用户确认
- Vault 浏览器端加密登录，Space Gateway 优先用订阅、最后用 API key
- 可选 pgvector 3D 向量记忆图与 6 copilot/3 studio 模块

## 适用场景

- 在同一项目或多个工作区并行使用多个 AI 编码助手
- 让 Nous 代做例行工作，只在发布/删除/对外决策时找我
- 用自己机器自托管，保留自己的模型账号与登录凭据

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L25:  Run OpenCode , OpenAI Codex , Claude Code , Google Gemini , Qwen , Kimi , Grok , and DeepSeek concurrently in pers
> L141: **SpaceApp** is a self-hosted workspace engineered for developers who use AI coding assistants. Instead of jugglin
> L148: - **One-Command Setup**: A single universal launcher command installs Docker prerequisites (if missing), configure

## 星数曲线

```mermaid
xychart-beta
    title "oll4com/spaceapp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 16
    line [12, 14, 15]
```

2026-10-18 12 → 2026-10-31 15（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a13543008255` · [字段定义](../../DATASET.md)*
