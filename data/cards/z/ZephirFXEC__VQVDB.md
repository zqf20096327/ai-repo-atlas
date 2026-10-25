# ZephirFXEC/VQVDB

⭐ 107 · C++ · GPL-3.0 · 推送 2026-06-24 · [GitHub](https://github.com/ZephirFXEC/VQVDB) · 个人维护

**用 VQ-VAE 压缩 OpenVDB 体素的深度学习工具**

面向 OpenVDB 体数据（如烟雾体积）的深度学习压缩器：训练阶段用 PyTorch 编码器将 8×8×8 叶节点体素块压缩为 128 维隐向量，量化到 256 项码本（uint8 索引），宣称可达 32× 压缩且视觉层面近似无损。运行时以 C++/CUDA 实现解码：CUDA 核函数将隐码还原为稠密体素块并重建 openvdb::FloatGrid，支持分批懒加载以降低显存占用，同时支持 CPU 编解码，并声明可与 Houdini 集成。作者在 README 中自述未能编译 pyopenvdb、训练数据需先抽取为 .npy 文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VQ-VAE 编码 + 256 项码本量化，索引以 uint8 存储
- CUDA 核函数 GPU 解码，重建 openvdb::FloatGrid
- 支持分批懒加载流式解压，声明低显存占用
- 支持 CPU 编解码，声明支持集成 Houdini

## 适用场景

- 压缩存储 OpenVDB 浮点体素网格以减小体积
- 在 Houdini 流程中按需解压大型体积数据
- GPU 实时解码大体量体积场景

## 场景标签

 · 领域:计算机图形/体积数据压缩

## 证据(README 行号)

> L16: VQVDB is a deep learning–powered compressor for volumetric data stored in OpenVDB.
> L17: It uses Vector Quantized Variational Autoencoders (VQ-VAE) to learn a compact latent space and achieves up to 32× c

## 星数曲线

```mermaid
xychart-beta
    title "ZephirFXEC/VQVDB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-25 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5c836a272f54` · [字段定义](../../DATASET.md)*
