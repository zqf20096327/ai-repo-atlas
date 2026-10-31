# Hanpx20/SafeSwitch

⭐ 16 · Jupyter Notebook · 推送 2026-05-31 · [GitHub](https://github.com/Hanpx20/SafeSwitch) · 组织维护

**论文官方代码：用内部激活信号动态调控 LLM 不安全输出**

论文 "Internal Activation as the Polar Star for Steering Unsafe LLM Behavior" 的官方代码仓库。方法包含两部分：训练 safety prober 从模型内部状态在生成前预测不安全行为；当标记潜在不安全生成时激活 refusal head（LM head 上的模块）使响应偏向拒绝，仅在必要时施加安全干预。仓库提供训练 prober 与 refusal head 的脚本、评测基准（SORRY-Bench 增强版、TrustLLM 等）、可交互的推理 pipeline，以及预训练模型（HuggingFace）。需要 Python≥3.10，训练与分析需手动设置超参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- safety prober 从内部激活在生成前预测不安全行为
- refusal head 模块按需将响应偏向拒绝
- 提供训练、评测与交互式推理脚本及预训练 prober/head
- 含 SORRY-Bench 增强版与 TrustLLM 等评测数据

## 适用场景

- 复现论文中 LLM 安全性实验
- 在自己的模型上训练 safety prober 与 refusal head
- 以交互方式体验 SafeSwitch 调控的生成效果

## 场景标签

`模型评测` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L8: SafeSwitch proposes a novel solution to balance safety and utility. Unlike traditional methods that bias LLMs unifor
> L10: We train a safety prober to extract information from internal states and predict unsafe behaviors pre-generation. W

## 星数曲线

```mermaid
xychart-beta
    title "Hanpx20/SafeSwitch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `16dd2941fac4` · [字段定义](../../DATASET.md)*
