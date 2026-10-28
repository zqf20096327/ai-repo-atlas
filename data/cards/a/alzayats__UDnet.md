# alzayats/UDnet

⭐ 72 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/alzayats/UDnet) · [官网](https://alzayats.github.io/UDnet/) · 组织维护

**水下图像增强模型：无需参考图去除蓝绿偏色与雾感**

PyTorch 实现的水下图像/视频增强模型，出自 Expert Systems with Applications 2025 论文。V1 完全无监督：训练中由经典对比度拉伸和可学习的多色彩空间拉伸模块（SGMCSS）自建参考，条件变分自编码器配合 PAdaIN 建模参考的不确定性，1.4M 参数可纯 CPU 运行。V2 改用 NAFNet 结构并在 UIEB/LSUI 配对数据上监督训练（需 CUDA）。支持图片与逐帧视频处理、Python API 调用、自训练与 PSNR/SSIM/UIQM/UCIQE 评测；可选 Real-ESRGAN 细节增强。MIT 许可，面向学术研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- V1 完全无监督，无需参考图，1.4M 参数可纯 CPU 运行
- 支持图片与视频（逐帧、保持原帧率）增强，含 Python API
- 提供自训练（V1/V2）与 PSNR/SSIM/UIQM/UCIQE 评测脚本
- 可选 Real-ESRGAN 细节增强与实验性 DiffBIR AI Max 分支

## 适用场景

- 去除水下照片和视频的蓝绿偏色与雾感
- 在无参考图的原始水下图像上做增强（V1）
- 在 UIEB/LSUI 配对数据上训练或微调自己的增强模型
- 用标准指标评测水下增强结果

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Underwater image enhancement trained without ground truth.**
> L5: Official code for *Adaptive deep learning framework for robust unsupervised underwater image enhancement* (Expert Sy
> L23: |**UDnet&nbsp;V1**|Released|`UDnet.pth`&nbsp;·&nbsp;5.6&nbsp;MB|457&nbsp;img/s&nbsp;GPU 11&nbsp;img/s&nbsp;CPU|Pape

## 星数曲线

```mermaid
xychart-beta
    title "alzayats/UDnet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 70 --> 73
    line [71, 72, 72]
```

2026-10-18 71 → 2026-10-28 72（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1cf47d6a5573` · [字段定义](../../DATASET.md)*
