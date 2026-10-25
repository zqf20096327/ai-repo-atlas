# odylith/odylith

⭐ 36 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/odylith/odylith) · [官网](https://odylith.ai) · 个人维护

**给编码 agent 加治理层的本地工具：约束 Codex/Claude Code 的行动**

安装在本地项目文件夹中、通过 Codex 或 Claude Code 使用的编码代理治理工具。包含 Context Engine（在 agent 推理前将仓库收窄到最小有据切片）、Execution Engine（将上下文转为约束 agent 可做/不可做动作的契约）、Tribunal 诊断引擎（对受阻/有歧义的姿态构建证据卷宗、十个固定角色评审并裁定），以及跨会话的持久记忆。空仓库时提供 greenfield 模式生成只读治理提案。附本地 index.html shell，提供 Radar/Compass/Atlas/Registry/Casebook 等界面。GA 平台为 Apple Silicon macOS 与 Linux（x86_64/ARM64），不支持 Intel macOS 与 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Context/Execution 双引擎：推理前收窄上下文、动作前校验许可性
- Tribunal 结构化诊断：证据卷宗+十角色评审+裁定与有界修正包
- greenfield 模式：空仓库生成只读、分阶段的治理提案
- 本地 index.html shell 含 Radar/Compass/Atlas/Registry/Casebook 界面

## 适用场景

- 让 Codex/Claude Code 会话基于仓库真实边界与历史失败教训工作
- 对受阻或有歧义的开发状态做证据化诊断而非让模型继续猜
- 在空仓库中先生成分阶段治理提案再动工

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Install Odylith into a project folder on your laptop. Use it through Codex or Claude Code.
> L25: Odylith reasons about your repo through delivery intelligence, grounds every
> L121: what is the next admissible move?"** It sits between the Context Engine and

## 星数曲线

```mermaid
xychart-beta
    title "odylith/odylith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e2857bd5e8f0` · [字段定义](../../DATASET.md)*
