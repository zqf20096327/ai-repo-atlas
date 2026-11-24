# tommy0103/obelisk

⭐ 970 · JavaScript · AGPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/tommy0103/obelisk) · [官网](https://obelisk.antinomie.org) · 个人维护 · 中文 README

**把编码 Agent 历史会话索引成 SQLite，供 Agent 查询、人浏览**

Obelisk 将本地多个编码 Agent（Claude Code、Codex、GitHub Copilot、DeepSeek Harness、Devin 等 12 个 Provider）的历史会话、消息、工具调用、子 Agent 等索引进统一的 SQLite 数据库，并监听各 Provider 目录保持增量更新。面向两类用户：Agent 通过 CLI 与技能文件用 JS 查询自身历史（search()/sql() 等查询面，FTS5 全文检索）；人通过 Electron 桌面应用浏览会话、管理 memory 文件、查看用量统计与周报卡片。需 Node.js 22.13+；桌面应用运行期间 CLI 只读。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引 12 个编码 Agent Provider 的会话到统一 SQLite 架构
- Agent 写 JS 查询检索自身历史：overview()/sessions()/search()/sql() 等
- memory 层：Agent 提议经用户批准的 markdown 记忆文件，后续会话可召回
- Electron 桌面应用提供会话浏览、热力图、token 图表与周报卡片

## 适用场景

- 让编码 Agent 检索自己过去的会话与改动原因
- 浏览和搜索所有 Agent 会话、工具调用与 token 用量
- 把一周的 Agent 工作生成可分享的 recap 卡片

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: Obelisk indexes your local coding-agent history into one SQLite database and
> L14: - **Agents** — the `obelisk` CLI plus an agent skill that teaches coding agents

## 星数曲线

```mermaid
xychart-beta
    title "tommy0103/obelisk 星数(近 25 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 660 --> 998
    line [688, 690, 692, 695, 696, 698, 700, 707, 750, 849, 695, 906, 916, 919, 921, 922, 928, 947, 950, 954, 955, 957, 967, 970, 970]
```

2026-10-22 688 → 2026-11-24 970（+282）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `ab5023631bf1` · [字段定义](../../DATASET.md)*
