# taco-group/PISCO

⭐ 63 · Python · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/taco-group/PISCO) · [官网](https://xiangbogaobarry.github.io/PISCO/) · 组织维护

**视频实例插入与编辑模型（PISCO）：稀疏控制精准插入/重排实例**

NeurIPS 2026 论文 PISCO 的官方实现：在视频中插入、移动、缩放指定实例（如人物、物体），以稀疏关键帧控制（实例抠图与深度条件）驱动。基于 Wan2.1/2.2 VACE 权重训练，提供 1.3B 与 14B 两个模型与推理脚本；训练分三阶段（输入投影预热、adapter 微调、DiT 联合微调），并发布 20,590 样本训练集（36.6 GB）与微调流程。安装通过 conda 环境 + torch 进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实例插入/创意编辑/重定位/缩放/仿真等多种视频编辑任务
- 稀疏关键帧控制（实例抠图+深度条件，随机采样关键帧）
- 1.3B 与 14B 双模型，14B 采用高低噪声双去噪专家混合
- 训练集（20,590 样本）与三阶段训练代码、自定义数据微调流程开放

## 适用场景

- 我想在已有视频中插入或移动某个人物/物体实例
- 基于自己的插入数据微调模型
- 复现论文的三阶段训练流程

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: This repo hosts the official implementation of PISCO: Precise Video Instance Insertion with Sparse Control
> L79: python inference/pretrained/infer_1.3B.py

## 星数曲线

```mermaid
xychart-beta
    title "taco-group/PISCO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-29 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ddcbb3874025` · [字段定义](../../DATASET.md)*
