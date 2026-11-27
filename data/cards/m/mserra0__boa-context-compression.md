# mserra0/boa-context-compression

⭐ 3 · Python · MIT · 推送 2026-11-15 · [GitHub](https://github.com/mserra0/boa-context-compression) · [官网](https://mserra0.github.io/boa-context-compression/) · 个人维护

**研究者工具包：用 Mamba SSM 单遍压缩长上下文供冻结 LLM 使用**

Boa 是基于 Mamba 状态空间模型的即插即用上下文压缩器，将任意长度文本在单次 O(L) 线性遍历中编码为连续表示或 KV cache，以条件化冻结目标 LLM 而无需微调或修改其权重。仓库提供论文对应的训练、评估与延迟基准代码，含 quickstart 配置、多阶段训练脚本、MRQA 评估套件及与 ICAE/SAC/Activation Beacon 等基线的对比分支。面向复现论文实验的研究者，要求 Linux、NVIDIA GPU 与 CUDA 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mamba SSM 单遍 O(L) 线性时间上下文编码，输出 soft token 或 KV cache
- 条件化冻结 LLM，无需微调或修改目标模型权重
- 提供训练、评估（MRQA F1/EM）与延迟基准全套代码
- 分支内置 Activation Beacon、SAC、ICAE 等基线实现

## 适用场景

- 复现论文中的 8x 压缩与延迟/显存基准实验
- 为长上下文 LLM 应用接入压缩后的 KV cache
- 开展上下文压缩方法的消融与模型规模实验

## 场景标签

 · 领域:NLP/LLM 效率优化

## 证据(README 行号)

> L3: Boa is a plug-and-play online context compressor built on a Mamba state-space model (SSM). It encodes arbitrary-leng
> L40: Paper experiments (8x compression, Mamba2 1.3B compressor, fine-tuned Qwen3-1.7B as frozen LLM, see docs/training/t
> L87: - MRQA Evaluation Suite: official span-overlap F1/EM package and batch scripts

## 星数曲线

```mermaid
xychart-beta
    title "mserra0/boa-context-compression 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `5073b311c491` · [字段定义](../../DATASET.md)*
