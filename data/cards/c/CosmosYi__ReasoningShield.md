# CosmosYi/ReasoningShield

⭐ 27 · HTML · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/CosmosYi/ReasoningShield) · [官网](https://cosmosyi.github.io/ReasoningShield/) · 组织维护

**检测大型推理模型思维链安全风险的 1B/3B 模型与 9.2K 数据集**

面向 LRM 安全审核的研究项目：提供 10 类风险、3 级安全级别的分类体系，9.2K 配对数据集（7K 训练 + 2.2K 人工标注测试），以及基于结构化风险分析与对比学习两阶段训练的 1B/3B 审核模型，输入 query 与思维链，输出逐步风险分析与安全判定。论文评估中 3B 模型在开源 LRM 子集平均 F1 为 91.8%。提供 Transformers 与 vLLM 两条推理评测路径，vLLM 路径需 Linux/CUDA 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 风险类别 × 3 安全级别的 CoT 审核分类体系
- 1B/3B 两档模型，1B 版本 GPU 显存占用约 2.3GB
- 输出逐步风险分析列（_analysis）与安全判定列（_judgment）
- 7K 训练 + 2.2K 人工标注测试（Fleiss κ=0.75）

## 适用场景

- 审核推理模型的中间思维链是否含不安全内容
- 训练/评测 CoT 安全审核模型
- 构建 LRM 输出安全评估基准

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9:  A 9.2K dataset and lightweight 1B/3B models for detecting safety risks in reasoning traces.
> L35: Large Reasoning Models (LRMs) may include unsafe content in intermediate reasoning steps even when their final answ

## 星数曲线

```mermaid
xychart-beta
    title "CosmosYi/ReasoningShield 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `57543e113ab8` · [字段定义](../../DATASET.md)*
