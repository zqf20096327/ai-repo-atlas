# TIGER-AI-Lab/SWE-QA-Pro

⭐ 15 · Python · MIT · 推送 2026-06-26 · [GitHub](https://github.com/TIGER-AI-Lab/SWE-QA-Pro) · 组织维护

**仓库级代码理解 QA 基准与 agentic 训练配方**

ACL 2026 Findings 论文项目，包含两部分：SWE-QA-Pro Benchmark 从长尾真实仓库的真实 issue 种子构建仓库级问答基准，题目经聚类保证主题多样、人工核验、难度校准管道过滤可直答的题目，使 agent 探索成为必要；训练部分提供两阶段配方（SFT 后接 RLAIF/GRPO），在 Qwen3-8B 上生成合成工具调用轨迹并训练。评测代码支持 Direct 与 Agent 两种模式，后端含 GPT-4o、Claude、Gemini、DeepSeek 及本地 vLLM 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从真实 issue 种子构建、人工核验、难度校准过滤的仓库级 QA 基准
- 两阶段训练配方（SFT → RLAIF/GRPO），基于 ms-swift 与 verl-tool
- 评测支持 Direct 与 Agent 模式，后端含 OpenAI/Claude/Gemini/DeepSeek 及本地 vLLM
- 训练 8B 模型在基准上报告超过 GPT-4o +2.3 分

## 适用场景

- 评测代码 agent 在长尾仓库上的探索与问答能力
- 用提供的轨迹数据与配方训练小模型的 agentic 推理
- 对比直答与工具调用 agent 的性能差距

## 场景标签

`模型评测` `强化学习` `微调` · 领域:评测与运维

## 证据(README 行号)

> L13: **SWE-QA-Pro** is a benchmark and training framework for **agentic repository-level code understanding**, enabling 
> L20: 1. **SWE-QA-Pro Benchmark:**
> L44: - **Training**: the two-stage recipe (SFT then RL) lives under `train/`. Stage 1 fine-tunes Qwen3-8B on agentic tra

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/SWE-QA-Pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c2d66e3015bb` · [字段定义](../../DATASET.md)*
