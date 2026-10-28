# lucidrains/enformer-pytorch

⭐ 575 · Python · MIT · 推送 2026-06-26 · [GitHub](https://github.com/lucidrains/enformer-pytorch) · 个人维护

**Deepmind Enformer 基因表达预测模型的 PyTorch 实现与微调库**

将 Deepmind 基于 attention 的基因表达预测网络 Enformer 用 PyTorch 重新实现，支持从 DNA 序列预测基因表达，并提供 HeadAdapterWrapper、ContextAdapterWrapper、ContextAttentionAdapterWrapper 等微调包装器用于下游任务。已将官方 TensorFlow Sonnet 权重移植到 HuggingFace（约 1GB，模型 EleutherAI/enformer-official-rough），早期版本存在数值舍入误差，0.8.0 起通过预计算 gamma 位置修正。附带 GenomicIntervalDataset 从 .bed 文件按区间读取序列并支持数据增强。以 pip 包形式提供，面向基因组学深度学习研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Enformer（attention 网络预测基因表达）的 PyTorch 实现
- 提供从 HuggingFace 加载的移植预训练权重与 from_pretrained 接口
- 三种微调适配器：新 track 微调、上下文条件微调、上下文注意力聚合
- GenomicIntervalDataset 支持 .bed 区间序列读取与位移/反向互补增强

## 适用场景

- 我在做基因组学序列到基因表达的预测任务
- 我想在自有数据（细胞类型、转录因子等）上微调 Enformer
- 我需要从 Enformer 提取嵌入用于下游建模

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Implementation of Enformer, Deepmind's attention network for predicting gene expression, in Pytorch. This repository
> L53: Deepmind has released the weights for their tensorflow sonnet Enformer model! I have ported it over to Pytorch and 

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/enformer-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 574 --> 576
    line [575, 575]
```

2026-10-18 575 → 2026-10-28 575（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c173fbb13071` · [字段定义](../../DATASET.md)*
