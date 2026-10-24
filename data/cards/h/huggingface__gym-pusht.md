# huggingface/gym-pusht

⭐ 206 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/huggingface/gym-pusht) · 组织维护

**PushT 推块任务的 Gymnasium 仿真环境，供强化学习训练评测**

Hugging Face 维护的 Gymnasium 环境，实现 PushT 推块任务：圆形 agent 在 512x512 场景中将 T 形块推入目标区域，覆盖率达 95% 即视为成功。提供连续二维动作空间，观测支持 state（5 维向量）、keypoint、96x96 像素图像等四种类型，可配置阻尼、重心、渲染尺寸，并支持重置到指定状态。以 pip 包发布，用于机器人操作策略（如 diffusion policy）的训练与评测。

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

- PushT 推块任务：T 形块覆盖目标区 95% 即成功
- 四种观测类型：state/keypoint/pixels/pixels_agent_pos
- 连续 [x, y] 动作空间，场景 512x512
- 可配置阻尼系数、块重心、渲染分辨率与重置到指定状态

## 适用场景

- 训练与评测机器人操作类强化学习或模仿学习策略
- 作为 diffusion policy 等方法的仿真基准任务
- 像素或状态观测下的策略泛化实验

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: A gymnasium environment PushT.
> L5: Diffusion policy on PushT env
> L32: The goal of the agent is to push the block to the goal zone. The agent is a circle and the block is a tee shape.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/gym-pusht 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 203 --> 207
    line [204, 205, 206]
```

2026-10-18 204 → 2026-10-24 206（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2f3731b9e463` · [字段定义](../../DATASET.md)*
