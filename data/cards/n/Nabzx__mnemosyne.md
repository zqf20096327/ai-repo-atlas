# Nabzx/mnemosyne

⭐ 17 · Rust · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Nabzx/mnemosyne) · [官网](https://nabzx.github.io/mnemosyne/) · 个人维护

**AI agent 记忆的版本控制系统：commit/branch/merge/blame**

面向 AI agent 开发者的记忆版本控制工具：将 agent 运行中积累的事实与决策记录为不可变、内容寻址的快照，提供 commit、branch、merge、blame、bisect、任意历史点重建等 Git 式命令。Rust 核心，附带 mnem CLI 与 Python SDK（pip 包 mnem-agents），本地运行、确定性、无网络、无模型调用。冲突以对象形式呈现并用 --resolve/--strategy 解决。明确声明：版本化记忆不提升回答质量，提供的是历史、审计与安全合并。缺 push/pull/clone（属后续规划）。提供 examples/ 覆盖 SDK、Claude、LangGraph、MCP 接入面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- blame/bisect 可将任一信念溯源到引入它的提交与观察
- 任意历史提交处精确重建记忆
- merge 以对象形式呈现冲突并支持 --resolve/--strategy 解决
- Rust 核心 + mnem CLI + Python SDK，本地确定性、无网络无模型调用

## 适用场景

- 排查 agent 记忆中错误事实的引入时间与来源
- 在隔离分支上探索假设性记忆再合并
- 对 agent 记忆做审计与可追溯管理

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: An AI agent builds up memory as it works: facts it learns, decisions it makes. Frameworks store that as state it ov
> L81: More worked examples, one per surface (SDK, Claude, LangGraph, MCP), live in
> L121: Issues, bug reports, and ideas are genuinely welcome, that's the best way to shape what gets built next. Developed

## 星数曲线

```mermaid
xychart-beta
    title "Nabzx/mnemosyne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dacc70125877` · [字段定义](../../DATASET.md)*
