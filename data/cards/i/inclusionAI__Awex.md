# inclusionAI/Awex

⭐ 178 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/inclusionAI/Awex) · 组织维护

**RL 训练-推理权重同步框架：秒级更新推理端模型参数**

面向强化学习工作流的权重同步框架，在训练引擎（Megatron）与推理引擎（vLLM、SGLang）之间实现秒级参数更新，使 rollout 阶段持续使用最新模型。核心机制：统一权重转换层处理不同并行策略与张量布局差异，仅传输必要分片并支持推理端 GPU 显存原地更新，传输模式覆盖 NCCL、RDMA（Mooncake）与共享内存。以 Python 包经 pip 安装，要求 Python 3.10+ 与 PyTorch 2.0+，训练/推理后端框架需单独安装且版本一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 万亿参数模型可在 10 秒内完成同步（RDMA 下 1T 约 6 秒）
- 统一权重适配层自动处理不同并行策略与张量布局差异
- 支持 NCCL、RDMA（Mooncake）、共享内存多种传输模式
- 兼容 Megatron 训练端与 vLLM/SGLang 推理端，参数名归一化为统一 HF 风格命名

## 适用场景

- RLHF 等在线 RL 训练中让推理 rollout 用上最新策略权重
- 大规模集群上缩短训练到推理的参数同步延迟
- 跨不同训练/推理引擎做权重格式转换与校验

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L8: **Awex** is a high-performance RL training-inference **weight synchronization** framework,
> L9: designed to enable **second-level parameter updates** from training to inference in RL workflows.
> L30: - **WeightWriter**: Runs within each training process, responsible for metadata collection and reporting of weight 

## 星数曲线

```mermaid
xychart-beta
    title "inclusionAI/Awex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 176 --> 179
    line [177, 178, 178]
```

2026-10-18 177 → 2026-10-29 178（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `648e62ad8af5` · [字段定义](../../DATASET.md)*
