# Tencent-Hunyuan/Hy-Embodied-0.5-VLA

⭐ 312 · Python · NOASSERTION · 推送 2026-08-04 · [GitHub](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA) · 组织维护 · 中文 README

**端到端视觉-语言-动作机器人操作系统：从数据到真机部署**

腾讯 Robotics X 与混元团队发布的端到端 VLA（视觉-语言-动作）系统，覆盖数据采集、模型设计、预训练、监督微调、RL 后训练与真机部署全流程。基于 Hy-Embodied-0.5 MoT 骨干与双塔流匹配动作专家（370M 参数），采用 delta-chunk 动作表示实现跨本体迁移；配套发布 2K+ 小时 UMI 双臂操作数据集（250K+ episodes 中的约五分之一，Lance/LeRobot v3.0 格式）、UMI 与 RoboTwin 两个检查点及训练评测脚本，支持 RoboTwin 2.0 与 RoboDojo 基准。运行需 Linux、Python 3.12、CUDA 12.x、NVIDIA GPU（建议 ≥16GB 显存）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双塔流匹配动作专家生成连续动作块，与 VLM 塔共享注意力
- delta-chunk 动作表示解耦本体运动学，支持四平台跨本体迁移
- Hy-UMI-10K 数据集 10K+ 小时，公开 2K+ 小时（Lance/LeRobot v3.0 格式）
- FlowPRO 无评论家偏好优化与异步推理部署框架

## 适用场景

- 在 RoboTwin 2.0 / RoboDojo 仿真基准上训练评测 VLA 策略
- 基于 UMI 检查点微调迁移到真机双臂操作任务
- 加载公开 UMI 数据集进行机器人操作数据研究与可视化

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L24: We introduce **Hy-Embodied-0.5-VLA (Hy-VLA)** — an end-to-end Vision-Language-Action system that spans the full rob
> L32:  * 🧠 **Unified VLA Architecture:** Extends the Hy-Embodied-0.5 MoT backbone with a dual-tower flow-matching action 

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Hy-Embodied-0.5-VLA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 308 --> 313
    line [309, 311, 312]
```

2026-10-18 309 → 2026-10-28 312（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9b2a75b820e7` · [字段定义](../../DATASET.md)*
