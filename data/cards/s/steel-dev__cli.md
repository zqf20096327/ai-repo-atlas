# steel-dev/cli

⭐ 33 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/steel-dev/cli) · 组织维护

**给 AI agent 用的云端/自托管浏览器基础设施 CLI**

单二进制命令行工具，为 Claude、Cursor、Browser Use 等 AI agent 提供浏览器基础设施：markdown 优先的抓取、24 小时长会话、具名 profile、隐身模式、住宅代理、自动验证码处理与凭据注入。可用 steel.dev 托管服务，也可通过 `steel dev` 或 Docker 自托管。内置 vendored 的 agent-browser 运行时，从上游迁移仅需改命令前缀。通过 curl 安装脚本或 cargo install 安装，支持 bash/zsh/fish 等补全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- markdown 优先输出与 `steel describe` 机器可读命令内省
- 24 小时长会话、可复用具名 profile 与持久认证上下文
- 内置 agent-browser 运行时，迁移仅需改命令前缀
- 云端或 Docker 自托管，MIT 开源

## 适用场景

- 为 AI agent 提供生产级抓取与浏览器会话
- 深度研究、异步任务等长时运行 agent 场景
- 需要代理、隐身与验证码处理的真实网页操作

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: The Steel CLI gives any AI agent (Claude, Cursor, Browser Use, or your own) a production-grade cloud browser: markdo
> L24: - **Framework-agnostic.** First-class support for Claude Computer Use, OpenAI Computer Use, Gemini Computer Use, Br
> L25: - **Cloud or self-hosted.** Fully open source. Use managed infrastructure at steel.dev, or run the Steel Browser st

## 星数曲线

```mermaid
xychart-beta
    title "steel-dev/cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bc725e168889` · [字段定义](../../DATASET.md)*
