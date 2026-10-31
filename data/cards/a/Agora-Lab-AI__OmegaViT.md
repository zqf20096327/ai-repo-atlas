# Agora-Lab-AI/OmegaViT

⭐ 15 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Agora-Lab-AI/OmegaViT) · [官网](https://agoralab.xyz) · 组织维护

**融合 MQA、SSM 与 MoE 的视觉 Transformer 架构库**

面向研究者的视觉 Transformer 架构实现：在 Transformer 层中组合多查询注意力（MQA）、旋转位置编码、每三层一层的状态空间模型（SSM）与混合专家（MoE），通过自适应 patch embedding 支持任意分辨率输入图像。以 Python 包形式提供（pip install omegavit），包含 create_advanced_vit 与 train_step 等接口，内置 loguru 日志与张量形状跟踪。基准测试结果在 README 中标注为尚未发布，引用条目中的 arXiv 编号为占位符。

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

- 多查询注意力与旋转位置编码的组合实现
- 每三层插入一层状态空间模型（SSM）进行序列建模
- 混合专家（MoE）条件计算（默认 8 个专家网络）
- 自适应 patch embedding 支持任意分辨率输入图像

## 适用场景

- 研究者实验融合 MQA/SSM/MoE 的视觉 Transformer 架构
- 作为可配置的 ViT 模型组件用于视觉任务训练
- 基于可调参数（层数/专家数/patch 大小等）做架构消融

## 场景标签

 · 领域:计算机视觉/深度学习架构

## 证据(README 行号)

> L10: OmegaViT (ΩViT) is a cutting-edge vision transformer architecture that combines multi-query attention, rotary embed
> L17: - **State Space Models (SSM)**: Integrates efficient sequence modeling every third layer
> L18: - **Mixture of Experts (MoE)**: Implements conditional computation for enhanced model capacity

## 星数曲线

```mermaid
xychart-beta
    title "Agora-Lab-AI/OmegaViT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fa891c0b1b58` · [字段定义](../../DATASET.md)*
