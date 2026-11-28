# Horonomos-laps/Yana-AI

⭐ 14 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/Horonomos-laps/Yana-AI) · [官网](https://yana.vutam.link/) · 组织维护 · 中文 README

**给 AI agent 加治理控制层的本地运行时：限制其可执行的操作**

位于 AI 模型与机器操作之间的本地控制平面：每个模型动作先经权威检查（Authority→Capability），通过能力清单、人工审批门、哈希链审计日志与核心文件 SHA-256 锁来限制 agent 能访问和执行的内容。提供 Rust 运行时 yana-rt（42 个子命令）与 Python CLI，为 Claude Code、Codex、Cursor、Antigravity 提供适配器；独立看门程序 Giám Thị 按计划任务检测漂移并锁定后续工具调用。安装需 Python 3.11+ 或 Rust、Git 与一个受支持宿主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次工具调用前置独立决策步骤，不依赖模型自身行为
- 哈希链审计日志，事后编辑可被检测
- 66 个 Pre/Post/Stop 钩子与破坏性命令拦截（rm -rf、force-push 等）
- 支持云端与本地多 provider，含故障转移与凭据池轮换

## 适用场景

- 让 coding agent 执行任务时拦截危险命令并留审计痕迹
- 强制要求发布/部署/删除类操作经人工确认
- 检测仓库中治理配置被未授权修改（漂移告警）

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5:  A local control plane between any AI model and real power over your machine.
> L111: |**Runtime `yana-rt`**|One turn loop and one authority contract for every client and every provider.|Live|
> L140: - **Providers:** anthropic, openai, gemini, groq, deepseek, openrouter, xai, novita, nvidia, minimax, glm, hugging

## 星数曲线

```mermaid
xychart-beta
    title "Horonomos-laps/Yana-AI 星数(近 3 点)"
    x-axis ["2026-11-11", "2026-11-26", "2026-11-28"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-11-11 13 → 2026-11-28 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `bd321de71e9c` · [字段定义](../../DATASET.md)*
