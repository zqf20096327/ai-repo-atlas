# seamus-brady/springdrift

⭐ 48 · Gleam · AGPL-3.0 · 推送 2026-04-27 · [GitHub](https://github.com/seamus-brady/springdrift) · [官网](https://springdrift.ai/) · 个人维护

**长生命周期 LLM agent 的持久运行时（参考架构）**

用 Gleam 基于 Erlang/OTP 构建的 LLM agent 持久运行时，定位为论文所称的 Artificial Retainer 参考架构：提供仅追加记忆与 git 版本化恢复、监督进程、案例推理（CBR）混合检索记忆层、可审计公理链的规范性安全门控，以及每周期注入的结构化自感知表示（sensorium）。内含 planner/coder/researcher 等多个子 agent 但共享同一身份与认知循环。状态为 Beta，需 Erlang/OTP 27+、Gleam 1.9+ 与 Git，至少一个 LLM provider API key（默认 Anthropic），通过 setup 脚本或 gleam 源码构建运行，提供 Web GUI 与 TUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 仅追加 JSONL 审计日志 + git 备份的记忆与恢复机制
- 案例推理（CBR）记忆层，可选 Ollama 语义嵌入检索
- 确定性规范性演算做安全门控，拒绝时引用具体公理
- 多子 agent 委派共享单一身份、记忆与认知循环

## 适用场景

- 让 agent 跨会话持续积累关于我的偏好与历史
- 需要事后审查每次决策与拒绝理由的可审计 agent
- agent 长期驻留运行并自主诊断故障、调度工作

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L27: A persistent runtime for long-lived LLM agents. Integrates an auditable execution substrate (append-only memory, su
> L29: Built in Gleam on the Erlang/OTP runtime.

## 星数曲线

```mermaid
xychart-beta
    title "seamus-brady/springdrift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-27 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c1b49a617dbe` · [字段定义](../../DATASET.md)*
