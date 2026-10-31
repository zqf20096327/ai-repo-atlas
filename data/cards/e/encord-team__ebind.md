# encord-team/ebind

⭐ 14 · Python · NOASSERTION · 推送 2025-11-13 · [GitHub](https://github.com/encord-team/ebind) · [官网](https://encord.com) · 组织维护

**五模态统一嵌入模型：文本/音频/图像/视频/3D 点云共空间**

Encord 团队开源的多模态嵌入模型 EBind，支持图像、视频、音频、文本与 3D 点云五种输入，全部投影到共享嵌入空间以支持跨模态相似度计算。以 Python 库形式提供，可从 GitHub 源码安装或作为外部依赖引入，模型与 E-MM1-100M 数据集发布在 Hugging Face。3D 点云主干带可选 PointNet2 自定义 CUDA 算子，编译后可加速推理，同时保留纯 torch 回退实现以支持无 GPU 硬件。许可为 CC BY-NC-SA 4.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种模态投影到统一嵌入空间，支持跨模态相似度计算
- 模型与 E-MM1-100M 数据集发布于 Hugging Face
- PointNet2 CUDA 算子可选编译，无 GPU 时有 torch 回退实现
- 提供 Colab 演示 notebook

## 适用场景

- 我在做多模态检索，需要用同一空间嵌入图片和文本
- 为含 3D 点云的数据做跨模态相似度匹配
- 在研究或项目中复用多模态嵌入计算跨模态相似度矩阵

## 场景标签

`多模态` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L27: EBind is a multi-modal embedding model that supports image, video, audio, text, and 3D point cloud inputs. All moda
> L90: **Note:** The image/video similarity is significantly higher because they share the same vision encoder.

## 星数曲线

```mermaid
xychart-beta
    title "encord-team/ebind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `3b207f24d9e5` · [字段定义](../../DATASET.md)*
