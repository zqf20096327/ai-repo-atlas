# mapooon/PetFace

⭐ 115 · Python · 推送 2026-07-10 · [GitHub](https://github.com/mapooon/PetFace) · 组织维护

**动物身份识别大规模数据集与基准（25万+ID，13科）**

ECCV 2024 Oral 论文 PetFace 的官方 PyTorch 实现：提供覆盖 13 科动物、超过 25 万个体 ID 的大规模动物身份识别数据集（需通过 Google 表单申请，人工审核后发放链接，仅限非商业研究用途），以及配套的 ArcFace 训练、重识别与验证评测代码。支持按物种或跨物种统一训练，提供预训练权重（Google Drive）、top-k 准确率与 AUC 计算，及基于关键点的面部对齐脚本。推荐 Docker 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 科动物、25 万+ ID 的大规模识别数据集（Google 表单申请获取）
- ArcFace 训练 / 重识别 / 验证完整代码与预训练权重
- top-k 准确率与 AUC 评测脚本
- 基于 AnyFace 5 关键点的自家图像面部对齐工具

## 适用场景

- 我想训练或评测动物个体识别模型
- 做宠物或野生动物的身份重识别研究
- 将自己的动物图像对齐到 PetFace 数据口径做推理

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L6: > **PetFace: A Large-Scale Dataset and Benchmark for Animal Identification**,
> L10: ## TL;DR: We established a large-scale animal identification dataset with more than 250k IDs across 13 families
> L15: ### Our PetFace dataset, code in this repository, and pretrained models are **for non-commercial research purpose o

## 星数曲线

```mermaid
xychart-beta
    title "mapooon/PetFace 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 113 --> 116
    line [114, 115, 115]
```

2026-10-18 114 → 2026-10-23 115（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `63b73592f1d2` · [字段定义](../../DATASET.md)*
