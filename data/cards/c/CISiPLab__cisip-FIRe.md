# CISiPLab/cisip-FIRe

⭐ 72 · Python · BSD-3-Clause · 推送 2026-02-27 · [GitHub](https://github.com/CISiPLab/cisip-FIRe) · [官网](https://fast-image-retrieval.readthedocs.io/en/latest/) · 组织维护

**面向图像检索研究的二值哈希方法统一框架**

由马来亚大学 CISiP Lab 发布的图像检索研究框架，将多种二值哈希方法（有监督/无监督/浅层共 20 余种，如 DPN、HashNet、OrthoHash）、多种骨干网络（AlexNet/VGG/ResNet）与多个公开数据集（ImageNet100、NUS-WIDE、COCO 等）统一在同一框架内，便于实现、复现与基准测试。采用模块化设计，研究者可组合组件实现自有方法；方法均提供 config 模板与 mAP 基准数字。BSD 3-Clause 许可，2021 年 9 月发布，安装与教程见其 readthedocs 文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一实现 20 余种二值哈希方法（监督/无监督/浅层三类）
- 支持 AlexNet/VGG/ResNet 骨干与 7 个公开数据集
- 各方法提供 config 模板与 64bit ImageNet AlexNet mAP 基准
- 模块化设计，可组合组件实现自有方法

## 适用场景

- 在统一框架下复现和对比二值哈希检索方法
- 实现自定义哈希方法并做基准测试
- 图像检索课程与研究实验

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L10: Fast Image Retrieval (FIRe) is an open source image retrieval project release by Center of Image and Signal Process
> L15:  Herein, we unified (i) various binary hashing methods, (ii) different backbone, and (iii) multiple datasets under 

## 星数曲线

```mermaid
xychart-beta
    title "CISiPLab/cisip-FIRe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-29 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `70a7deb265e4` · [字段定义](../../DATASET.md)*
