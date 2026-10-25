# Lumi-supercomputer/LUMI-AI-Guide

⭐ 82 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/Lumi-supercomputer/LUMI-AI-Guide) · 组织维护

**将机器学习应用迁移到 LUMI 超算的教程指南**

由 LUMI 用户支持团队（LUST）与 LUMI AI Factory 维护的迁移教程：以 PyTorch Vision Transformer 在 ImageNet 上训练图像分类模型为贯穿示例，从一个可在本地运行的脚本逐步改写为在 LUMI 上运行的版本，覆盖训练迁移直至 LLM 推理章节（使用 vLLM 做内存占用可控的托管）。主题多与具体框架无关，需具备 ML 基础、LUMI 账号及 GPU 时数项目方可运行示例。仓库提供全部 Python 与 bash 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 PyTorch VIT + ImageNet 训练为贯穿示例，从本地脚本逐步改写为 LUMI 版本
- 第 10 章覆盖从训练到生产的 LLM 推理（vLLM 托管）
- 全部配套 Python/bash 脚本随仓库提供
- 多数主题不依赖特定机器学习框架

## 适用场景

- 把本地 ML 训练任务迁移到 LUMI 超算
- 学习在超算上进行多 GPU/多节点训练与 profiling
- 了解在 LUMI 上部署 LLM 推理服务（vLLM）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This guide is designed to assist users in migrating their machine learning applications from smaller-scale computing
> L7: All Python and bash scripts referenced in this guide are accessible in this GitHub repository. We start with a basic

## 星数曲线

```mermaid
xychart-beta
    title "Lumi-supercomputer/LUMI-AI-Guide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-25 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e31c8891fa33` · [字段定义](../../DATASET.md)*
