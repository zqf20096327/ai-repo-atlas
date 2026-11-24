# KIvanow/sessionly

⭐ 95 · TypeScript · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/KIvanow/sessionly) · [官网](https://sessionly.dev) · 组织维护

**为 AI 编码 agent 会话记录本地台账：追踪行为、成本与存活行**

本地优先的 Rust CLI 台账，为 Claude Code、Codex、Cursor 与 Grok 的会话建立统一记录：通过 hooks 捕获事件，读取 agent 自身的 transcript 汇总 token、模型与成本，归一化为本地 SQLite 账本（~/.sessionly）。核心指标是'survival'——统计 agent 写入的行有多少后续仍留在文件和 PR 中。上传与服务器为可选项，默认不上传提示词/命令/文件文本，源码不出本机。提供 GitHub Action 统计 PR 中 agent 写入占比，及可选团队服务器仪表板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 agent 会话归一为同一记录结构
- 统计 agent 行的存活率（文件留存与 PR review 后留存）
- 本地 SQLite 台账可删除后由 sync --force 重建
- 可选服务器与 GitHub Action 输出团队级统计

## 适用场景

- 查看自己各 AI 编码工具的会话明细与花费
- 统计 agent 写入的代码在 review 后的保留比例
- 团队部署服务器汇总成员的 agent 使用数据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L22: Sessionly keeps a ledger of your Claude Code, Codex, Cursor and Grok sessions, on your own
> L55: - **Lab-neutral.** Sessionly is not any agent maker's tool. It reads every agent's sessions the
> L104: 1. **Capture.** A hook appends each agent event to a local file in 2–4 ms. It only observes: it


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `db89a38aafea` · [字段定义](../../DATASET.md)*
