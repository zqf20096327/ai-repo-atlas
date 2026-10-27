# doeixd/opencode-ralph-rlm

⭐ 32 · TypeScript · 推送 2026-06-30 · [GitHub](https://github.com/doeixd/opencode-ralph-rlm) · [官网](https://deepwiki.com/doeixd/opencode-ralph-rlm) · 个人维护

**OpenCode 插件：可托管的编码循环，supervisor 外环+全新 worker 内环**

OpenCode 的插件/集成，面向长时间无人值守的编码任务：用户向 ralph-rlm/supervisor 模型描述目标，后台由本地 provider 进程编排循环——先通过 interview 技能生成 PLAN.md 并与用户约定 verify.command（测试命令作为唯一完成判据），每次尝试启动全新 OpenCode worker session，验证失败则把教训写入协议文件（PREVIOUS_STATE、AGENT_CONTEXT_FOR_NEXT_RALPH 等）传递给下一次尝试。记忆存于磁盘文件而非聊天历史；参考材料不进上下文窗口，worker 通过 rlm_grep/rlm_slice 按需检索（RLM 思路）。支持并行 swarm、多版本命名计划。安装经 npm/npx 或 agent skill，Bun 非必需。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- verify.command 测试命令作为循环的唯一完成判据
- 每次尝试启动全新 worker，记忆存于可读可编辑的协议文件（PLAN.md 等）
- RLM 机制：大参考材料不进上下文，worker 用 rlm_grep/rlm_slice 按需切片
- 支持命名多版本计划切换与并行 swarm

## 适用场景

- 睡前交接一个编码目标，回来时验证测试已通过
- 让 agent 在多轮尝试间通过文件记忆自我纠正并积累经验
- 以 PLAN.md/RLM_INSTRUCTIONS.md 作为可控的长期引导面

## 场景标签

`编码 Agent` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: An OpenCode integration for **long-running, hands-off coding work**. Describe a goal, walk away, and come back to fi
> L14: You talk to **one** model in the OpenCode TUI — `ralph-rlm/supervisor`. Behind it, a small local helper runs the lo
> L158: - **Workers:** fresh OpenCode session per attempt; engine spawns via SDK.

## 星数曲线

```mermaid
xychart-beta
    title "doeixd/opencode-ralph-rlm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f4426fec5339` · [字段定义](../../DATASET.md)*
