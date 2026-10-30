# alchemistyzz/PeRL

⭐ 30 · Python · 推送 2026-03-30 · [GitHub](https://github.com/alchemistyzz/PeRL) · 组织维护 · 中文 README

**交错图文推理的强化学习训练框架（NeurIPS'25 论文官方代码）**

论文官方实现，提出面向交错多模态任务的通用强化学习框架：通过图像序列置换增强探索（覆盖跨图像位置推理），通过 rollout 过滤低质量轨迹以稳定训练，在 8 个基准上以 7B 模型（Qwen2.5-VL）训练。提供 git clone + conda 安装与 scripts/train.sh 训练脚本。面向开展多模态强化学习研究的科研人员，需自备 GPU 训练环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像序列置换增强探索与顺序不变性约束
- rollout 过滤机制筛选高质量轨迹
- 8 个基准（5 多图 VQA + 3 单图推理）评估，平均提升 3.23 分
- 基于 Qwen2.5-VL-7B 训练，不增加模型参数

## 适用场景

- 复现论文中多图推理的强化学习训练
- 在自有多模态任务上应用置换增强 RL 策略
- 比较多图/单图文本推理基准性能

## 场景标签

`科研工具` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L19: Inspired by the impressive reasoning capabilities demonstrated by reinforcement learning approaches like DeepSeek-R
> L21: **PeRL** introduces a general reinforcement learning framework tailored for interleaved multimodal tasks, featuring
> L85: Run `scripts/train.sh` to train Qwen2.5-VL model.

## 星数曲线

```mermaid
xychart-beta
    title "alchemistyzz/PeRL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a5f695faf190` · [字段定义](../../DATASET.md)*
