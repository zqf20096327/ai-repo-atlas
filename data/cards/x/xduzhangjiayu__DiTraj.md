# xduzhangjiayu/DiTraj

⭐ 21 · Python · 推送 2025-12-11 · [GitHub](https://github.com/xduzhangjiayu/DiTraj) · [官网](https://xduzhangjiayu.github.io/DiTraj_Project_Page/) · 组织维护

**DiT 视频生成模型的免训练轨迹控制框架（论文官方实现）**

论文 DiTraj 的官方代码实现：在 DiT 架构的视频扩散模型上实现免训练的轨迹控制，输入 bbox 关键帧轨迹引导，生成与目标轨迹对齐的视频。支持适配 Wan2.1、CogVideoX 等 DiT 视频生成模型，流程为提示词扩展/精炼、在 run.py 中定义 bbox 轨迹、运行 run.py 生成视频。基于 diffusers v0.33.1 构建，需替换其中的 transformer_wan.py 文件。许可为 CC BY-NC 4.0，仅限研究用途、禁止商用；Gradio 交互 demo 尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免训练的轨迹控制，不修改模型权重
- 以 bbox 关键帧序列定义轨迹（支持复杂轨迹）
- 可适配 Wan2.1、CogVideoX 等 DiT 视频生成模型
- 基于 diffusers（v0.33.1）构建并替换 transformer 模块

## 适用场景

- 按指定轨迹生成可控视频内容
- 在 DiT 视频生成模型上复现论文实验
- 研究生成结果的轨迹对齐与视频质量

## 场景标签

 · 领域:AI 生成/视频扩散模型

## 证据(README 行号)

> L12: We propose DiTraj, the first training-free trajectory control framework for DiT-based video generation model. Given
> L13: an input bbox trajectory guidance, DiTraj enables generating high-quality videos that align with the target traject

## 星数曲线

```mermaid
xychart-beta
    title "xduzhangjiayu/DiTraj 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a9fd20f0b821` · [字段定义](../../DATASET.md)*
