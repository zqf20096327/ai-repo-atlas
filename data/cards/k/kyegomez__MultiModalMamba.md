# kyegomez/MultiModalMamba

⭐ 474 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/MultiModalMamba) · [官网](https://discord.gg/GYbXvDGevY) · 个人维护

**融合 ViT 与 Mamba 的多模态模型实现（文本+图像）**

基于 PyTorch 的多模态模型实现：将 Vision Transformer 与 Mamba 结构结合，同时处理文本与图像数据，构建于 Zeta 框架之上。提供 MultiModalMambaBlock 与可训练的 MultiModalMamba 两级接口，支持 depth、heads、patch_size、fusion_method 等架构参数定制，可选返回 embeddings 用于迁移学习或特征提取。以 pip 包 mmm-zeta 分发，MIT 许可。README 未给出预训练权重或基准结果。

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

- Vision Transformer 与 Mamba 融合，同时处理文本与图像
- 深度可定制架构（depth/d_state/patch_size/fusion_method 等）
- return_embeddings 选项支持特征提取与迁移学习

## 适用场景

- 搭建文本+图像联合输入的模型原型
- 在自定义数据集上训练多模态架构
- 提取中间 embeddings 用于下游任务

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4: Multi Modal Mamba (MultiModalMamba) is an all-new AI model that integrates Vision Transformer (ViT) and Mamba, creat
> L23: - Flexibility in Data Types: The MultiModalMamba model can handle both text and image data simultaneously. This all

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/MultiModalMamba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 473 --> 476
    line [475, 474]
```

2026-10-18 475 → 2026-10-29 474（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a862531e0490` · [字段定义](../../DATASET.md)*
