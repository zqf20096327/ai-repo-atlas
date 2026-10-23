# PytorchConnectomics/pytorch_connectomics

⭐ 202 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/PytorchConnectomics/pytorch_connectomics) · [官网](https://pytorchconnectomics.github.io/pytorch_connectomics/) · 组织维护

**电镜连接组学图像的深度学习分割工具箱**

基于 PyTorch 的 2D/3D 电子显微镜（EM）连接组学分割工具箱，覆盖组织尺度血管/细胞核、细胞尺度神经元/突触、细胞器尺度线粒体/囊泡等结构的分割。流水线分为 train、infer、decode、evaluate、tune 五个可组合阶段，支持从单 GPU 到多节点集群运行，内置 Lucchi++、SNEMI3D、CREMI 等基准数据集与教程配置，并提供基于 coding agent（claude/codex CLI）的安装与工作流驱动方式。由 Boston College Donglai Wei 团队维护，MIT 许可。

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

- 五阶段可组合流水线：train/infer/decode/evaluate/tune，CLI 任意字段可覆盖
- 覆盖组织/细胞/细胞器三个尺度的多种结构分割
- 内置多个公开基准数据集教程配置与预训练 checkpoint
- 支持 claude/codex coding agent 驱动安装与工作流

## 适用场景

- 在 EM 大体积数据上训练和推理神经元/线粒体/突触分割模型
- 用内置基准复现或对比分割方法
- 在自有 EM 数据上通过教程配置训练分割模型

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: **Modern deep learning for 2D / 3D connectomics.** Train, run inference, decode, and evaluate segmentation pipelines
> L140: EM volume ─[train]─▶ checkpoint ─[infer]─▶ representation ─[decode]─▶ instances ─[evaluate]─▶ metrics

## 星数曲线

```mermaid
xychart-beta
    title "PytorchConnectomics/pytorch_connectomics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 201 --> 203
    line [202, 202]
```

2026-10-18 202 → 2026-10-23 202（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b9db127d3bae` · [字段定义](../../DATASET.md)*
