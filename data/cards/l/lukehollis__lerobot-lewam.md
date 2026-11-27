# lukehollis/lerobot-lewam

⭐ 11 · Python · NOASSERTION · 推送 2026-09-19 · [GitHub](https://github.com/lukehollis/lerobot-lewam) · [官网](https://github.com/huggingface/lerobot) · 个人维护

**从零训练的 31.5M World Action Model，用于 SO-101 机械臂抓取控制**

以 LeRobot policy 插件形式实现的 World Action Model，参数量 31.5M，全部从随机权重开始训练，不依赖任何预训练 VAE、ResNet、视频模型或 VLM。单一 diffusion transformer 通过双噪声时钟同时输出动作与未来帧预测，可给出 policy、视频预测、正/逆动力学四种分布。任务为 MuJoCo 仿真中 SO-101 抓取 30mm 立方体，含 200 条脚本示范、从零训练脚本与四项世界模型有效性检验工具。尚处研究进行中状态，检查点未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 31.5M 参数 World Action Model，完全从零训练
- 一套权重输出 policy/视频预测/正逆动力学四种分布
- 四项检验区分世界模型学习与外观过拟合
- 以 LeRobot 第三方 policy 插件打包，附 DGX Spark 容器化运行笔记

## 适用场景

- 学习 World Action Model 的完整实现与训练流程
- 在 MuJoCo 中复现 SO-101 抓取任务并评估策略
- 检验未来帧预测损失是否真正学到动作条件依赖

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L12: **A small World Action Model, trained from scratch, so you can see how every piece works.**
> L14: LeRobot-WAM is a 31.5M parameter World Action Model packaged as a LeRobot
> L70: |simulator|MuJoCo, `robotstudio_so101` from MuJoCo Menagerie|

## 星数曲线

```mermaid
xychart-beta
    title "lukehollis/lerobot-lewam 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-16", "2026-11-27"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-13 10 → 2026-11-27 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `b6aaf4a92982` · [字段定义](../../DATASET.md)*
