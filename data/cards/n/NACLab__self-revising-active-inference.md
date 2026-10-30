# NACLab/self-revising-active-inference

⭐ 65 · Python · 推送 2026-08-05 · [GitHub](https://github.com/NACLab/self-revising-active-inference) · [官网](https://shorturl.at/bEBTn) · 组织维护

**稀疏奖励机器人任务的主动推断智能体官方实现（论文代码）**

ICRA 2025 论文 SR-AIF 的官方实现：在部分可观测、连续动作、稀疏奖励的像素级机器人控制环境中，基于主动推断（AIF）与世界模型构建智能体，引入先验偏好学习与自我修正机制。提供从 PPO 专家采集种子数据、训练 AIF 智能体、tensorboard 日志查看、robosuite 键盘数据采集的脚本流程。要求 Linux 与 NVIDIA GPU（RTX 3060/A100 测试），经 conda + install.sh 安装，gcc 为构建 robosuite 所需。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向像素级 POMDP、连续动作、稀疏奖励的主动推断框架 SR-AIF
- 先验偏好学习与自我修正（self-revision）机制
- 覆盖 gymnasium 山地车与 robosuite 机器人任务（如开门）的实验脚本
- 提供实现细节文档（数学框架与代码逻辑）

## 适用场景

- 复现论文中的稀疏奖励机器人控制实验
- 研究 POMDP 场景下的深度主动推断方法
- 基于已有框架开展主动推断与世界模型的后续研究

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L6: There is relatively little work that builds general active inference (AIF) models in the context of partially observ
> L40: * In order to run the R-AIF agent for the Open-AI gymnasium mountain car problem, we need to first collect expert d

## 星数曲线

```mermaid
xychart-beta
    title "NACLab/self-revising-active-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-30 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cddb3854c352` · [字段定义](../../DATASET.md)*
