# mehmetdemircs/RepoSpend

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/mehmetdemircs/RepoSpend) · [官网](https://repospend.com) · 个人维护

**本地优先的 AI 编程 token 用量与成本仪表盘**

面向开发者的本地仪表盘：读取 Codex、Claude Code、GitHub Copilot（及实验性 Cursor）在本地存储的用量文件（只读模式），归一化为会话并按 Git 仓库分组，展示仓库、会话、模型、工具维度的 token 形态（输入/缓存/输出/推理）与 API 等效成本估算，并提供命令摩擦（agent friction）信号。通过 npx repospend 或全局 npm 安装运行，默认在 localhost:2005 打开仪表盘；无登录、无遥测、不上传提示词或代码。成本为估算值而非账单，且要求 Node.js 22.12+，使用 better-sqlite3 需安装原生 SQLite 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取本地 Codex/Claude Code/GitHub Copilot 用量文件（只读），按 Git 仓库根分组
- 按仓库/会话/模型/工具展示 token 形态与 API 等效成本估算
- 区分阻塞性命令失败与无害退出的 agent friction 信号
- 本地优先：无登录、无遥测、不上传提示词或代码

## 适用场景

- 查看哪个仓库、会话或模型在消耗最多的 token 和估算成本
- 在不联网、不上传代码的前提下本地对比多个 AI 编程工具的用量
- 检查缓存复用与命令重试等 agent 摩擦信号以定位低效会话

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: RepoSpend is a local-first dashboard for tracking AI coding token usage and API-equivalent spend by repository, sess
> L11: RepoSpend turns local AI coding usage data into a repo-level cost dashboard, so
> L73: Use it to inspect Codex token usage, Claude Code token usage by repo, GitHub

## 星数曲线

```mermaid
xychart-beta
    title "mehmetdemircs/RepoSpend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bb273af35bd9` · [字段定义](../../DATASET.md)*
