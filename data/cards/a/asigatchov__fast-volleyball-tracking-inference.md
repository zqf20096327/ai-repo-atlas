# asigatchov/fast-volleyball-tracking-inference

⭐ 72 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/asigatchov/fast-volleyball-tracking-inference) · 个人维护

**CPU 实时排球检测追踪管线，自动生成 9:16 竖屏集锦**

基于 ONNX/OpenVINO 模型的排球球体检测与追踪流水线，在 Intel i5-10400F CPU 上进行推理，提供四个步骤：球体检测输出 ball.csv、轨迹计算与回合提取、回合视频合成/切分、以球轨迹为中心生成竖屏 reels。另含场地感知变体（结合球员检测识别触球与回合）、OpenVINO 运行时与球员+球联合检测脚本，并附模型 F1/Precision/Recall/CPU FPS 基准表（最高 1140 FPS）。通过 git clone 与 uv sync 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 球体检测输出 CSV 坐标与可选视频可视化
- 球场感知变体结合球员检测识别触球动作与回合边界
- OpenVINO 运行时支持 CPU/GPU/AUTO 设备选择与球员+球+头部联合检测
- 四个模型附带 F1/精确率/召回率与 CPU FPS 基准及复现脚本

## 适用场景

- 从比赛录像中提取排球回合并自动生成竖屏集锦视频
- 获取逐帧球体坐标数据用于运动分析
- 复现和评测不同检测模型在 CPU 上的速度与精度

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: High-speed pipeline for volleyball ball detection, rally extraction, and automatic generation of 9:16 reels.
> L12: 1. `src/inference_onnx_seq_gray_v2.py` -> detects ball and writes `ball.csv` (and optional `predict.mp4`).

## 星数曲线

```mermaid
xychart-beta
    title "asigatchov/fast-volleyball-tracking-inference 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 70 --> 73
    line [71, 72, 72]
```

2026-10-18 71 → 2026-10-26 72（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6345f0490d8b` · [字段定义](../../DATASET.md)*
