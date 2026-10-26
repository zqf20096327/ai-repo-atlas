# nipponjo/deepfillv2-pytorch

⭐ 220 · Python · 推送 2026-06-14 · [GitHub](https://github.com/nipponjo/deepfillv2-pytorch) · 个人维护

**DeepFill v2 图像修复的 PyTorch 复现实现**

论文 Free-Form Image Inpainting with Gated Convolution (DeepFill v2) 的 PyTorch 复现代码库，基于原作者 TensorFlow 实现转换。提供 Places2 与 CelebA-HQ 数据集的官方权重转换版和微调版预训练模型，支持命令行测试（test.py）、配置文件训练（train.py + TensorBoard 日志）以及基于 FastAPI + React 的演示 Web 应用。需求为 python3、pytorch、torchvision 等库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Places2/CelebA-HQ 官方权重转换版与微调版
- test.py 命令行推理与 test.ipynb notebook 示例
- train.py 配置文件训练并支持 TensorBoard 日志
- FastAPI + React 演示 Web 应用

## 适用场景

- 对带掩码的图像做自由形状缺失区域修复
- 在 Places2 或 CelebA-HQ 上训练/微调修复模型
- 通过 Web 界面体验图像修复效果

## 场景标签

`图像视频处理` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: A PyTorch reimplementation of the paper **Free-Form Image Inpainting with Gated Convolution** (DeepFillv2) (https://
> L18: python test.py --image examples/inpaint/case1.png --mask examples/inpaint/case1_mask.png --out examples/inpaint/cas

## 星数曲线

```mermaid
xychart-beta
    title "nipponjo/deepfillv2-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 219 --> 221
    line [220, 220]
```

2026-10-18 220 → 2026-10-26 220（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `87a6eac9995f` · [字段定义](../../DATASET.md)*
