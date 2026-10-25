# google-deepmind/brave

⭐ 52 · Python · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/google-deepmind/brave) · 组织维护

**BraVe 自监督视频学习的 JAX 实现，含预训练检查点**

DeepMind 论文 Broaden Your Views for Self-Supervised Video Learning 的 JAX 实现：基于窄视角/宽视角（视频/音频/光流）对比的自监督视频表征学习，骨干网络为 TSMResnet。提供多个预训练检查点及在 HMDB51/UCF-101/K600 上的评测结果，支持用本包直接评测 HMDB51（Python 3.7+），也支持基于 jaxline 从头训练。限制：不提供光流训练选项，检查点并非由本包训练器产出，部分结果可能与论文不完全一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 V/AF、V/A、V/VVV 等多种配置的预训练检查点与评测数据
- 支持直接对 HMDB51（三个 split）进行评测，含数据集下载脚本
- 支持基于 jaxline 从头训练，数据格式遵循 DMVR
- GPU 运行需安装对应 CUDA 版本的 jaxlib

## 适用场景

- 复现论文在 HMDB51/UCF-101/K600 上的评测结果
- 使用预训练检查点提取视频/音频嵌入用于下游动作识别
- 基于 jaxline 在自有数据（DMVR 格式）上自监督训练视频模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This is a JAX implementation of
> L14: We provide a selection of pretrained checkpoints in the table below, which can

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/brave 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `527473b756b3` · [字段定义](../../DATASET.md)*
