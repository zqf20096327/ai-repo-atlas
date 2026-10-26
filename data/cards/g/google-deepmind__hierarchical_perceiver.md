# google-deepmind/hierarchical_perceiver

⭐ 37 · Python · Apache-2.0 · 推送 2026-07-24 · [GitHub](https://github.com/google-deepmind/hierarchical_perceiver) · 组织维护

**DeepMind HiP 层级感知器的官方 JAX 实现与代码发布**

论文《HiP: Hierarchical Perceiver》的官方代码仓库，提供 HiP 架构的 JAX 实现及 PerceiverIO 的改进实现。HiP 通过在全局注意力感知器中引入局部性并使用自监督方法学习低维位置嵌入，扩展其对原始高分辨率图像/视频等大规模输入的处理。安装需 Python 虚拟环境与 requirements 文件（GPU 版依赖 CUDA 与 nvidia-cuda-toolkit，亦有 CPU 版），附 Dockerfile 与单元测试；核心实现位于 perceiver.py。预训练检查点与 Colab 尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HiP 架构的官方 JAX 实现
- 附 PerceiverIO 的改进实现
- 提供 GPU/CPU 两套依赖文件与 Dockerfile
- 单元测试演示在多模态示例数据上运行 HiP

## 适用场景

- 复现 HiP 论文中的层级感知器架构
- 基于 perceiver.py 改造多模态感知模型研究
- 在标准化 Docker 环境中运行示例测试

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L9: This repository includes the official Jax implementation of the HiP
> L13: General perception systems such as Perceivers can process arbitrary modalities in any combination and are able to h

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/hierarchical_perceiver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `53c26e4e3d33` · [字段定义](../../DATASET.md)*
