# bcmi/ControlCom-Image-Composition

⭐ 186 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/bcmi/ControlCom-Image-Composition) · 组织维护 · 中文 README

**基于扩散模型的可控图像合成模型，统一四种图像合成任务**

论文 ControlCom 的官方代码库：基于 Stable Diffusion 的可控图像合成模型，用一个二维指示向量统一图像融合、图像和谐化、视角合成与生成式合成四种任务，可选择性地调整前景光照和/或姿态以适配背景。提供两份微调权重（分别面向融合/和谐化与视角/合成），支持推理脚本与训练代码（训练数据需自备，已移除部分敏感信息）。README 声明改变前景姿态的模式鲁棒性较低，可能产生结构失真；要求前景物体的长宽完全延伸到图像边缘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个模型用二维指示向量统一图像融合、和谐化、视角合成、生成式合成四任务
- 两份微调检查点，分别适配不同任务组合
- 提供推理脚本（inference.py / test.sh）与自定义数据推理流程
- 发布 FOSCom 数据集（640 对前景/背景）及其扩展 MureCom

## 适用场景

- 把前景物体插入背景图并自动调整光照与姿态
- 对已有合成图做光照和谐化处理
- 按参考图调整前景视角以适配背景

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: > **ControlCom: Controllable Image Composition using Diffusion Model** [[arXiv]](https://arxiv.org/pdf/2308.10040.pd
> L23: **In our controllable image composition model, we unify four tasks in one model using an 2-dim binary indicator vec
> L33: Our method is built upon stable diffusion and the network architecture is shown as follows.

## 星数曲线

```mermaid
xychart-beta
    title "bcmi/ControlCom-Image-Composition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 185 --> 187
    line [186, 186]
```

2026-10-18 186 → 2026-10-22 186（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ad63c584236a` · [字段定义](../../DATASET.md)*
