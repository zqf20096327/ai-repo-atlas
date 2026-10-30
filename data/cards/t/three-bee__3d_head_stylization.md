# three-bee/3d_head_stylization

⭐ 16 · Python · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/three-bee/3d_head_stylization) · [官网](https://three-bee.github.io/head_stylization/) · 组织维护

**保持身份的 3D 头部风格化：从真实人脸生成艺术化 3D 头像**

ICCV 2025 论文官方代码：基于 PanoHead 3D GAN，从 360 度视角对 3D 头部做风格化，利用负对数似然蒸馏（LD）、多视角网格分数与镜像梯度、分数排名加权来保持原始对象身份。用户需先完成 PanoHead 与 3DDFA_V2 的数据处理流程获得 W+ latents，下载 PanoHead、RealisticVision v5.1、ControlNet、DepthAnythingV2 等多个检查点后运行推理或训练脚本。面向计算机视觉研究者，需 CUDA 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PanoHead 的 360 度视角 3D 头部风格化
- 负对数似然蒸馏（LD）增强身份保持
- 提供多个真实身份的 W+ latents 示例
- 提供推理脚本 infer_LD.py 与训练脚本 train_LD.py

## 适用场景

- 把真实人脸照片风格化为艺术化 3D 头像
- 复现论文的 3D 头部风格化实验
- 研究扩散模型与 GAN 之间的蒸馏方法

## 场景标签

`图像生成` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L1: # Identity Preserving 3D Head Stylization with Multiview Score Distillation [ICCV 2025]
> L9: 3D head stylization transforms realistic facial features into artistic representations, enhancing user engagement ac

## 星数曲线

```mermaid
xychart-beta
    title "three-bee/3d_head_stylization 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a0bd77f4ad02` · [字段定义](../../DATASET.md)*
