# anushacodes/tennis-analysis-with-cv

⭐ 14 · Jupyter Notebook · 推送 2025-12-14 · [GitHub](https://github.com/anushacodes/tennis-analysis-with-cv) · 个人维护

**单相机网球视频分析流水线：检测球场、球员与球**

从比赛视频中检测并跟踪球场线、球员与网球的端到端计算机视觉流水线：YOLO 检测 14 个球场关键点与球员，单应性估计实现球场几何重建，TrackNet 热图回归跟踪高速球体并做时序平滑与离群点过滤，输出带实时叠加的标注视频。单输入视频即可生成完整标注结果，各模块可独立替换。作为 CS673 计算机视觉课程项目开发，通过 conda 环境与 pip 依赖安装，运行 Python 推理脚本并需提供模型权重文件。

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

- YOLO 检测 14 个球场关键点并结合单应性估计做球场重建
- TrackNet 热图回归跟踪高速网球并做时序平滑与离群过滤
- 单视频输入端到端生成标注输出视频，支持漏检轨迹外推
- 球场关键点检测约 0.98 mAP@50

## 适用场景

- 从单机位比赛视频生成含球场线、球员与球的标注视频
- 低成本替代多相机系统的网球动作分析
- 课程/科研中复用各模块做球场检测或目标跟踪实验

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: The system combines **YOLO-based detection**, **TrackNet ball tracking**, and **geometric court reconstruction** to 
> L21:  * TrackNet heatmap-based ball localization

## 星数曲线

```mermaid
xychart-beta
    title "anushacodes/tennis-analysis-with-cv 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28", "2026-10-31"]
    y-axis "stars" 10 --> 15
    line [11, 12, 14, 14]
```

2026-10-18 11 → 2026-10-31 14（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `60c7325dd7d5` · [字段定义](../../DATASET.md)*
