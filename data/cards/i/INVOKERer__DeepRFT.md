# INVOKERer/DeepRFT

⭐ 274 · Python · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/INVOKERer/DeepRFT) · 组织维护 · 中文 README

**图像去模糊研究代码：深度残差傅里叶变换网络**

AAAI 2023 Oral 论文《Intriguing Findings of Frequency Selection for Image Deblurring》及其早期版本《Deep Residual Fourier Transformation for Single Image Deblurring》的 PyTorch 官方实现。模型基于 PyTorch 1.8.0 构建，在 Ubuntu 18.04、Python3.8、CUDA11.1 环境测试。提供预训练模型（Google Drive 与百度网盘）用于单图去模糊与散焦去模糊的推理测试，并附训练脚本。面向复现论文实验的深度学习研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度残差傅里叶变换用于单图去模糊
- 提供去模糊与散焦去模糊的预训练模型测试命令
- 包含训练脚本与 conda 环境安装说明

## 适用场景

- 复现 AAAI 2023 论文的去模糊实验结果
- 用预训练模型对自己的模糊图像做去模糊测试
- 在 GoPro 等数据集上训练去模糊模型

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: # Intriguing Findings of Frequency Selection for Image Deblurring (AAAI 2023 Oral)
> L10: # Deep Residual Fourier Transformation for Single Image Deblurring
> L20: The model is built in PyTorch 1.8.0 and tested on Ubuntu 18.04 environment (Python3.8, CUDA11.1).

## 星数曲线

```mermaid
xychart-beta
    title "INVOKERer/DeepRFT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 273 --> 275
    line [274, 274]
```

2026-10-18 274 → 2026-10-29 274（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fe1fb39cd8ad` · [字段定义](../../DATASET.md)*
