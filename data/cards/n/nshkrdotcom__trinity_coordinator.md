# nshkrdotcom/trinity_coordinator

⭐ 77 · Elixir · MIT · 推送 2026-09-30 · [GitHub](https://github.com/nshkrdotcom/trinity_coordinator) · [官网](https://github.com/nshkrdotcom/trinity_coordinator) · 个人维护

**Elixir 实现的本地小模型 LLM 路由协调器**

以 Elixir/Nx 实现 TRINITY 式路由：经 Sakana AI 奇异值微调适配的 Qwen3-0.6B 小模型读取对话记录，提取隐藏状态向量，由路由头映射为 agent 与角色 logits，再经可配置的 provider 边界把任务派发给 LLM 提供方，并带 Thinker/Worker/Verifier 编排与验收终止逻辑。提供 Mix 任务从 HuggingFace 拉取 SHA-256 校验的 624MB 模型包，含五套本地评测面（不做外部 LLM 调用），CUDA 上评测 37/37 通过，也支持 CPU 与 Apple Silicon 后端。项目声明处于活跃开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 适配版 Qwen3-0.6B 隐藏状态向量 → agent/角色 logits 的路由机制
- Thinker/Worker/Verifier 编排与 verifier ACCEPT 终止、JSONL trace 持久化
- mix trinity.artifact.fetch 按 SHA-256 pin 拉取 HuggingFace 模型包
- 五套本地评测/诊断面，无外部 LLM 调用，CUDA 评测 37/37 通过

## 适用场景

- 在 Elixir 应用中用本地小模型决定 LLM 调用派发给哪个 agent/角色
- 离线验证路由正确性与 Python 管线的一致性
- 研究 SVF 微调产物的导出与复现流程

## 场景标签

`多智能体` `模型网关` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L15: `trinity_coordinator` is an Elixir/Nx implementation of a TRINITY-style
> L19: agent and role logits, and a configurable provider boundary dispatches
> L20: the selected work to a live LLM provider.

## 星数曲线

```mermaid
xychart-beta
    title "nshkrdotcom/trinity_coordinator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-30 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `35d139f3e425` · [字段定义](../../DATASET.md)*
