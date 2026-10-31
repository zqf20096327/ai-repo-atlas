# mooch443/trex

⭐ 127 · C++ · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/mooch443/trex) · [官网](https://trex.run) · 个人维护

**多动物追踪软件：计算机视觉追踪、无标记识别与姿态估计**

基于计算机视觉与机器学习的多动物追踪软件，通过背景减除实现实时追踪（可追踪 256 条鱼），支持最多 100 个个体的视觉识别与机器学习自动纠错。自 2.0 版起支持 ultralytics 兼容的检测模型（如 YOLO），覆盖边界框、关键点、分割等任务，可导入自有 .pt 模型。支持从视频文件或摄像头采集，通过 Miniforge/conda 在 Windows/Linux/macOS 安装，提供 GUI 与命令行两种使用方式。面向动物行为学等科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 背景减除追踪 256 条鱼快于视频回放速度
- 最多 100 个个体的无标记视觉识别与自动纠错
- 支持 ultralytics 兼容检测模型（YOLO、关键点、分割）
- 同界面支持加载视频与摄像头直接录制

## 适用场景

- 追踪并识别群体动物个体的行为轨迹
- 对动物视频做姿态与视野的 2D 估计
- 用自有 YOLO .pt 模型替代背景减除做检测

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L13: Welcome to the git repository of **TRex** (https://trex.run) -- a software designed to track and identify individua
> L15: TRaditionally, using background-subtraction, TRex can track 256 fish faster than the video plays back, and for up t
> L17: Since version 2.0, TRex also supports machine-learning based detection models. Out of the box we support models com

## 星数曲线

```mermaid
xychart-beta
    title "mooch443/trex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 126 --> 128
    line [127, 127]
```

2026-10-18 127 → 2026-10-31 127（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b516e45a08ac` · [字段定义](../../DATASET.md)*
