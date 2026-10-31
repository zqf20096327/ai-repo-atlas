# bing-xu-graphics/light_transformer

⭐ 16 · Python · 推送 2026-10-16 · [GitHub](https://github.com/bing-xu-graphics/light_transformer) · [官网](https://bingxu.tech/projects/2026_lighttransformer/page.html) · 组织维护

**预测全局光照的 3D 光传输嵌入模型（SIGGRAPH 2026 论文代码）**

SIGGRAPH 2026 论文 "A Generalizable Light Transport 3D Embedding for Global Illumination" 的代码发布仓库：提供基础模型、训练与推理代码、预训练权重（Git LFS 跟踪）、紧凑测试集与场景准备流程文档。模型读取场景点云与查询特征，输出预测的辐照度；推理按 chunk 处理查询点，输出分辨率与场景点数无关。原始训练环境为 Linux + NVIDIA GPU + Python 3.10/PyTorch 2.5.1/CUDA 12.4，CUDA 扩展在安装时本地编译。仓库未附带项目级许可证（处于发布审核阶段）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 场景点编码 + 局部解码的全局光照预测模型（含预训练权重）
- chunked 推理，输出分辨率独立于场景点数量
- 提供训练管线 train.py 与可恢复的 checkpoint（含优化器状态）
- 附 Blender/PBRT 场景生成工作流与 6 个示例场景

## 适用场景

- 用预训练模型对 3D 场景预测全局光照/辐照度
- 在新数据集上继续训练或复现论文设置
- 按工作流生成新的程序化室内场景数据集

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L15: This repository contains the base model, training and inference code, pretrained weights, a compact test set, and d
> L27: - `infer.py`: chunked inference with local decoding
> L36: The original training environment used Python 3.10, PyTorch 2.5.1, and CUDA 12.4 on Linux with an NVIDIA GPU.

## 星数曲线

```mermaid
xychart-beta
    title "bing-xu-graphics/light_transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `84e76d6ec37f` · [字段定义](../../DATASET.md)*
