# google-deepmind/c3_neural_compression

⭐ 105 · Python · Apache-2.0 · 推送 2026-06-11 · [GitHub](https://github.com/google-deepmind/c3_neural_compression) · 组织维护

**DeepMind C3 神经压缩论文官方代码：单图/视频过拟合压缩**

复现论文《C3: High-performance and low-complexity neural compression from a single image or video》的训练与评估代码。C3 对每张图像或每段视频单独过拟合一个小模型实现压缩，在 CLIC2020 图像与 UVG 视频基准上匹配参考编解码器的率失真性能且解码 MACs/pixel 较低；基于 COOL-CHIC 与 PyTorch。在单块 NVIDIA P100/V100 GPU、Python 3.10 上测试，通过 JAXline 运行图像/视频实验配置，Kodak/CLIC2020 数据自动下载，UVG 需手动准备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对每个图像/视频单独过拟合小模型的神经压缩方法
- 提供 Kodak/CLIC2020/UVG 三种基准的实验配置
- 输出 psnr、per-frame-mse 与 bpp 指标日志
- baselines 目录含各压缩基线的率失真与 MACs/pixel 数据

## 适用场景

- 复现 C3 论文的图像/视频压缩实验结果
- 对比神经压缩方法与 VTM 等基线的率失真性能
- 在神经压缩研究中基于 COOL-CHIC 改进方法做实验

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L14: introduce C3, a neural compression method with strong rate-distortion (RD)
> L26: This code can be used to train and evaluate the C3 model in the paper, that can

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/c3_neural_compression 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-29 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d8a81feb6429` · [字段定义](../../DATASET.md)*
