# guillaumeboniface/super_resolution

⭐ 25 · Jupyter Notebook · 推送 2026-04-09 · [GitHub](https://github.com/guillaumeboniface/super_resolution) · 个人维护

**SR3 论文图像超分辨率复现：16x16→128x128 扩散模型**

复现论文《Image Super-Resolution via Iterative Refinement》（SR3）的部分结果，仅使用 CelebA-HQ 数据集的 16x16→128x128 任务。基于扩散模型与 UNet 架构（含低分辨率注意力层与残差连接），残差块取自 bigGAN，条件实例归一化取自 SDE 论文，参数量约 480M（论文为 550M）。训练依赖 TensorFlow，数据转为 tfrecord；支持 Google AI Platform（含 TPU）或本地训练，命令行执行推理，TensorBoard 监控。论文细节缺失处作者做了自行推测实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 复现 SR3 论文的 UNet 扩散架构（480M 参数）
- 四种噪声调度实现（quadratic/linear/constant/warmup）
- 支持 Google AI Platform 训练与本地训练，命令行推理

## 适用场景

- 复现 SR3 超分辨率扩散模型在 CelebA-HQ 上的结果
- 基于扩散模型的图像超分辨率研究实验
- 在 Google Cloud 或本地环境训练扩散超分模型

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Reproducing the Image Super-Resolution via Iterative Refinement paper
> L8: - The default hyperparameters are based on the paper description: 256 batch size, 1M steps training, adam optimizer,

## 星数曲线

```mermaid
xychart-beta
    title "guillaumeboniface/super_resolution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c66105078b2c` · [字段定义](../../DATASET.md)*
