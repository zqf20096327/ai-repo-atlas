# arassadin/image-compression-benchmarking

⭐ 42 · Python · WTFPL · 推送 2026-08-13 · [GitHub](https://github.com/arassadin/image-compression-benchmarking) · 个人维护

**RNN 图像压缩方法与传统编解码器的质量基准对比工具**

受 Google 论文 Full Resolution Image Compression with Recurrent Neural Networks 及其 TensorFlow 实现启发的基准项目：下载 Google 预训练模型对图像执行神经网络压缩，生成传统编解码器与神经网络方法的压缩样本，再以 MS-SSIM 指标输出 CSV 格式的质量对比结果，可覆盖不同压缩级别与图像分辨率。要求 Ubuntu 环境、TensorFlow、Pillow 3.4+、NumPy 1.11+，通过 install_deps.sh 安装依赖，GPU 非必需但推荐。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | WTFPL |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Google 预训练模型（residual_gru.pb）的神经网络压缩编码
- 生成传统编解码器与神经网络压缩的对照测试样本
- MS-SSIM 指标质量基准，输出 CSV 结果

## 适用场景

- 对比神经网络压缩与传统编解码器在不同压缩级别下的质量
- 在不同分辨率图像上评估 RNN 压缩方法的效果
- 复现论文方法并快速试用预训练压缩模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This project inspired by Google's paper ***Full Resolution Image Compression with Recurrent Neural Networks*** (arxi
> L5: The code inside aims to compare (quantitatively and qualitatively) different aspects of compression done by this **m
> L51: Finally, run `python benchmark_quality_msssim.py` for quality benchmarking based on MS-SSIM metric. It will generat

## 星数曲线

```mermaid
xychart-beta
    title "arassadin/image-compression-benchmarking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4ab98b953036` · [字段定义](../../DATASET.md)*
