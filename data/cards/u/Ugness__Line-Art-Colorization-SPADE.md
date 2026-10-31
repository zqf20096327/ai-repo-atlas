# Ugness/Line-Art-Colorization-SPADE

⭐ 15 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/Ugness/Line-Art-Colorization-SPADE) · 个人维护

**基于 SPADE 的线稿自动上色模型（PyTorch）**

以 NVlabs/SPADE 代码为基础构建的线稿自动上色生成模型，面向深度学习研究与开发者。提供预训练网络下载、Safebooru 数据集抓取与预处理（sketchKeras 提取线稿、sketch_simplification 简化线稿）、train.py 训练与 test.py 推理脚本，并附带 Flask demo 服务器部署方式。运行要求 CUDA 10.1，数据预处理依赖多个第三方模型文件（mod.h5、model_gan.pth）需单独下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SPADE（spadeladder 生成器）架构的线稿上色模型
- 提供预训练网络、数据集处理与训练/测试完整流程
- Safebooru 数据集的 tag 解析与图片下载工具
- Flask demo 服务器一键部署（flask_test.py）

## 适用场景

- 给动漫线稿自动生成彩色图像
- 在自己的 Safebooru 风格数据上训练上色模型
- 搭建线稿上色的 web 演示服务

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L4: - We used code from https://github.com/NVlabs/SPADE
> L84:   python train.py --name test --dataset_mode safebooru --dataroot data/safebooru/train_upper_body_768 --tf_log --ba
> L87: - For testing, use test.py. It will inference and save images in results/[EXP_NAME]

## 星数曲线

```mermaid
xychart-beta
    title "Ugness/Line-Art-Colorization-SPADE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `302120677b63` · [字段定义](../../DATASET.md)*
