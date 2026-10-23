# lucidrains/mimic-video

⭐ 125 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/lucidrains/mimic-video) · 个人维护

**Mimic-Video 机器人控制模型实现：视频生成动作**

Mimic-Video 论文（Video-Action Models for Generalizable Robot Control Beyond VLAs）的 PyTorch 实现，以视频模型骨干生成机器人动作。支持替换视频骨干为 MiniMax H3，处理 Qwen3-VL 层-50 隐状态、3D MM-RoPE 位置网格、rectified-flow 时间步与流 ODE 采样，LoRA 微调与固定前缀开箱可用；支持麦克风音频条件输入，并提供 LIBERO 数据集训练的额外依赖与 LiberoDataset。以 pip 包与 Python API 形式提供，面向机器人学习研究者与开发者。

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

- 视频模型骨干驱动的机器人动作生成实现
- 可切换 MiniMax H3 视频骨干，支持 LoRA 微调
- 视频与麦克风音频联合条件输入
- 提供 LIBERO 基准数据集训练支持（LiberoDataset）

## 适用场景

- 在 LIBERO 基准上训练视频-动作机器人控制策略
- 研究视频模型作为机器人控制骨干的用法
- 结合音频与视频条件进行机器人动作生成实验

## 场景标签

 · 领域:机器人/具身智能

## 证据(README 行号)

> L5: Implementation of Mimic-Video, Video-Action Models for Generalizable Robot Control Beyond VLAs
> L41: The wrapper handles Qwen3-VL layer-50 hidden states, packed `[text | audio | video]` sequences with 3D MM-RoPE posi

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/mimic-video 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-23 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `938dde5610ab` · [字段定义](../../DATASET.md)*
