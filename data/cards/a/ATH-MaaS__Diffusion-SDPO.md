# ATH-MaaS/Diffusion-SDPO

⭐ 27 · Python · Apache-2.0 · 推送 2025-11-11 · [GitHub](https://github.com/ATH-MaaS/Diffusion-SDPO) · 组织维护

**扩散模型偏好对齐的插件式训练规则（SDPO）**

论文 Diffusion-SDPO 的官方实现：一种即插即用的偏好对齐训练规则，基于 winner/loser 输出空间梯度的对齐度为 loser 分支计算自适应缩放，使每次更新在一阶意义上不增加 winner 损失，从而保留偏好输出并扩大偏好间隔。该保护机制与模型无关，可嵌入 Diffusion-DPO、DSPO、DMPO。仓库基于 SD1.5 与 SDXL 提供 6 个 checkpoint、训练脚本（accelerate 自动检测 GPU 数）、一键评测脚本（PickScore/HPSv2/Aesthetics/CLIP/ImageReward）及 A/B 胜率对比。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- winner-preserving 保护规则，可嵌入 Diffusion-DPO/DSPO/DMPO
- 基于 SD1.5 与 SDXL 的 6 个 checkpoint
- 一键评测脚本计算 PickScore/HPSv2/Aesthetics/CLIP/ImageReward
- 支持两个 checkpoint 的逐指标 A/B 胜率对比

## 适用场景

- 给扩散模型 DPO 训练加上保护 winner 输出的规则
- 在 SD1.5/SDXL 上复现论文中的偏好对齐训练
- 用统一 prompt 套件评测并对比不同 DPO 变体效果

## 场景标签

`微调` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: **Diffusion-SDPO** is a plug-in training rule for preference alignment of diffusion models. It computes an adaptive 
> L11: This repository is the official implementation of paper Diffusion-SDPO.

## 星数曲线

```mermaid
xychart-beta
    title "ATH-MaaS/Diffusion-SDPO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4515ba8f7bb3` · [字段定义](../../DATASET.md)*
