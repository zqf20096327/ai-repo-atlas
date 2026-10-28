# xmindflow/cenet

⭐ 39 · Python · 推送 2026-10-22 · [GitHub](https://github.com/xmindflow/cenet) · 组织维护

**医学图像多域分割网络（MICCAI 2025）的 PyTorch 实现**

MICCAI 2025 论文 CENet 的官方 PyTorch 实现，面向医学图像分割研究者：通过跳跃连接中的双选择性增强块（DSEB）与解码器中的多尺度上下文特征注意力模块（CFAM），在心脏 MRI（ACDC）、腹部 CT（Synapse）、皮肤镜（HAM10000/PH2）等多域数据上训练与评估分割模型。提供 PyTorch Hub 预训练模型加载、Hugging Face/Mega.nz 权重下载、各数据集预处理说明与训练/评估脚本；声明模型仅供研究、不可临床使用。测试环境为 Python 3.10.16 与 CUDA 12.9。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DSEB 融入跳跃连接、CFAM 多尺度上下文注意力的分割网络实现
- PyTorch Hub 免克隆加载预训练模型并直接输出分割掩码
- 覆盖 ACDC/Synapse/HAM10000/PH2 四个数据集的训练与评估脚本
- 预训练权重托管于 Hugging Face 与 Mega.nz

## 适用场景

- 在心脏 MRI、腹部 CT 或皮肤镜数据上训练/评估分割模型
- 通过 PyTorch Hub 直接推理获得医学图像分割掩码
- 复现 MICCAI 2025 论文的多域分割实验结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: A unified PyTorch implementation of **CENet**, our Context Enhancement Network for robust, high-resolution segmenta
> L20: Medical image segmentation, particularly in multi-domain scenarios, requires precise preservation of anatomical str

## 星数曲线

```mermaid
xychart-beta
    title "xmindflow/cenet 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-26", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-23 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7e57b398ab2f` · [字段定义](../../DATASET.md)*
