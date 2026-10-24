# momhq/mom

⭐ 62 · Go · Apache-2.0 · 推送 2026-08-24 · [GitHub](https://github.com/momhq/mom) · [官网](https://askmom.sh) · 组织维护

**给 AI 编程 agent 的持久记忆层：跨会话保存项目上下文**

面向 AI 编码 agent 的持久记忆工具：后台监听支持的 harness（Pi、Claude Code、Codex）的会话记录，写入只追加 Ledger（$HOME/.mom/ledger/），并投影为每项目的 markdown vault（.mom/vault/），agent 用普通文件工具自行读取，无查询服务器。通过 harness 上下文文件与 mom skills（/mom-fold、/mom-status）集成，提供 mom lens 本地可视化。当前为 v0.53.0-alpha 公开 alpha；本地优先，采集受项目绑定隐私门控；v0.50 起不迁移旧 SQLite vault。以 Go 编写，提供 Homebrew 与源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 会话记录写入只追加 Ledger，投影为可读可 diff 的 markdown vault
- harness 无关：Pi、Claude Code、Codex 端到端验证
- vault 丢失可用 mom vault rebuild 从 Ledger 重建
- 本地优先与隐私门控：未绑定项目的目录不记录

## 适用场景

- 新会话开始时让 agent 自动读取项目历史与约定，无需重新解释
- 跨工具、跨项目保留架构决策与上下文
- 用 mom lens 查看已捕获会话的可视化视图

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: _Mom_ gives AI coding agents persistent memory across sessions, projects, and tools.
> L32: - **Harness-agnostic** — Pi, Claude Code, and Codex are integration targets, not storage silos.

## 星数曲线

```mermaid
xychart-beta
    title "momhq/mom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `59b259669a6f` · [字段定义](../../DATASET.md)*
