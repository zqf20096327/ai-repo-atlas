# PsiACE/dohnuts

⭐ 37 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/PsiACE/dohnuts) · [官网](https://dohnuts.ai/) · 个人维护

**小型多模态决策模型：单次前向输出选择/判断/打分概率**

面向直接决策任务的小型多模态模型及 Python 工具链：输入消息、文档或图像，通过 choice/noul/score 三种模式在单次前向中返回选择、真假估计或有序打分的概率分布，多条问题可共享同一输入。工具链覆盖训练（RLCD 与交叉熵联合）、推理、评估与 agent 集成（Bub SDK）。0.8B 模型可在消费级 GPU 本地运行；checkpoint 加载时下载并合并 LoRA、应用校准。模型权重与代码分别授权，代码为 Apache-2.0。

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

- choice/noul/score 三种决策模式，单次前向返回概率分布
- 同一输入上同时回答多个问题
- 工具链覆盖数据准备、训练（RLCD+交叉熵）、校准与评估
- 0.8B 模型可在消费级 GPU 上本地运行

## 适用场景

- 对客服请求做路由分类并判断是否涉及退款
- 结合图像做视觉选择题或评分
- 作为 agent 的决策工具通过 Bub SDK 接入

## 场景标签

`多模态` `微调` `强化学习` · 领域:感知与多模态

## 证据(README 行号)

> L7: Dohnuts builds small multimodal models for direct decisions. Give the model a
> L12: The Python toolkit covers training, inference, evaluation, and agent integration.

## 星数曲线

```mermaid
xychart-beta
    title "PsiACE/dohnuts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-26 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0d67097da484` · [字段定义](../../DATASET.md)*
