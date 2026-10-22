# HorizonWind2004/reconstruction-alignment

⭐ 419 · Python · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/HorizonWind2004/reconstruction-alignment) · [官网](https://reconstruction-alignment.github.io/) · 组织维护 · 中文 README

**自监督后训练方法：提升统一多模态模型的生成与编辑能力**

ICLR 2026 论文 RecA 的官方开源实现。核心机制是让预训练统一多模态模型（UMM）从自身视觉理解特征重建原图（以原图而非 caption 为目标），该语义重建目标可迁移到文生图与图像编辑，且保持原推理接口不变。提供 BAGEL/Harmon/OpenUni/Show-o 的训练与评测代码、Hugging Face 权重、在线 Demo 及 ComfyUI 使用方式；报告 BAGEL-RecA 训练成本为 6×80GB A100 × 4.5 小时。多数代码 Apache 许可，部分组件沿用各自许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自监督重建对齐（RecA）后训练方法，保持原模型推理接口
- 已在 BAGEL、Harmon、Show-o、OpenUni、MMaDA 等架构上验证
- 提供 Hugging Face 权重库（含 INT8/NF4/DF11 量化版本）与在线 Demo
- 提供 ComfyUI 使用指南与中文版复现指南

## 适用场景

- 统一多模态模型的文生图与图像编辑能力后训练
- 在自己的 UMM 架构上复现或迁移 RecA 方法
- 在 ComfyUI 中直接使用 BAGEL-RecA 生成与编辑图片
- 多基准评测提升后的模型（GenEval/DPGBench/ImgEdit/GEdit）

## 场景标签

`图像生成` `多模态` `微调` · 领域:内容生成

## 证据(README 行号)

> L25: **Improving image generation through visual understanding.** Reconstruction Alignment (RecA) is a **self-supervised
> L59: 3. Local Setup: Follow the instructions in the BAGEL Installation Guide to set up the environment, and run `BAGEL/i

## 星数曲线

```mermaid
xychart-beta
    title "HorizonWind2004/reconstruction-alignment 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 418 --> 420
    line [419, 419]
```

2026-10-18 419 → 2026-10-22 419（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `255344570be7` · [字段定义](../../DATASET.md)*
