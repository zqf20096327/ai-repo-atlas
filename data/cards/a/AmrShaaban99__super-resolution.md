# AmrShaaban99/super-resolution

⭐ 36 · Jupyter Notebook · 推送 2026-04-06 · [GitHub](https://github.com/AmrShaaban99/super-resolution) · 组织维护

**七个深度学习超分辨率模型的实现与 Tkinter GUI**

毕业/课程性质的超分辨率项目：实现 SRCNN、FSRCNN、ESPCN、RDN、RFDN、Autoencoder（两种结构）与 ESRGAN 共七种基于 CNN 的超分模型，在 DIV2K 数据集（900 张图，80/20 划分）上以 x2/x4 尺度训练 50-120 epochs。提供 Tkinter 三页 GUI（选择模型与尺度、展示输入输出图像对比、About 页）。测试覆盖 Set5、Set14、医学数据集与自建数据集，报告 PSNR/SSIM 与处理耗时。关键限制：无独立 pip 安装途径，依赖锁定为 Python 3.8.8 + TensorFlow 2.3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七种 CNN 超分模型实现并提供预训练权重
- Tkinter GUI 支持选择模型与尺度并对比前后图像
- 在 Set5/Set14/医学/自建四类数据集上报告 PSNR/SSIM 与耗时

## 适用场景

- 用 GUI 对低分辨率图像做 x2/x4 超分
- 对比学习多种经典超分网络的实现
- 复现并查看各模型在基准数据集上的指标

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8: Image super-resolution (ISR) is the process of recovering high-resolution (HR) images from low-resolution (LR) image
> L19: The seven implemented models have been trained on DIV2K dataset, which contains **900 RGB images** with different s

## 星数曲线

```mermaid
xychart-beta
    title "AmrShaaban99/super-resolution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `30e80caf3b20` · [字段定义](../../DATASET.md)*
