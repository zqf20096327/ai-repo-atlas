# DecapodLabs/decapod

⭐ 237 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/DecapodLabs/decapod) · [官网](https://decapodlabs.github.io/decapod/) · 组织维护

**治理 AI 编码 agent 工作的 Rust CLI 内核**

面向使用 Cursor、Claude Code、Codex 等编码 agent 的开发者：Decapod 作为仓库内治理层，把需求转化为带范围的计划，管理并行任务认领与隔离工作区，记录计划、决策与工作历史到 .decapod/ 目录，使不同 agent 可跨工具接续同一 PR。内置验证流水线默认本地运行，可配置远程 Buildkite preflight。每次调用即起即退，无后台服务；无法治理其工作流之外 agent 执行的命令。通过 cargo binstall 安装，MIT 许可。

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

- 计划/决策/工作历史存于仓库，跨 agent 与跨工具续接同一 PR
- 任务认领、重叠检查与隔离工作区支持 agent 并行
- 内置验证流水线将结果与当前变更及必需检查绑定
- 即起即退的 Rust CLI，无后台服务

## 适用场景

- 在 Cursor 或 Claude Code 中开发时让计划与需求保持绑定
- 多个编码 agent 并行处理不同任务并避免冲突
- 中途更换 agent 工具后继续未完成的 PR
- 在 PR 合并前确认所需验证已完成

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6:  Work in Cursor, Claude Code, Codex, Antigravity, Grok, or your preferred coding agent.
> L43: Decapod is a Rust CLI that agents use throughout development. It reads the

## 星数曲线

```mermaid
xychart-beta
    title "DecapodLabs/decapod 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 236 --> 238
    line [237, 237]
```

2026-10-18 237 → 2026-10-22 237（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ef23478d49ff` · [字段定义](../../DATASET.md)*
