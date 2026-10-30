# hassanrrraza/crowd-analysis-yolo

⭐ 20 · Jupyter Notebook · 推送 2026-05-14 · [GitHub](https://github.com/hassanrrraza/crowd-analysis-yolo) · [官网](https://ieeexplore.ieee.org/document/11204071) · 个人维护

**基于 YOLOv8 的公交站人群检测计数系统，附论文**

针对白沙瓦 BRT 公交站的人群分析系统，用 YOLOv8 与 OpenCV 对视频做实时人员检测与计数，支持自定义 ROI 与阈值触发的人群监控。提供带色彩状态指示（正常/警告/危险）、统计面板与计数历史图的图形界面，另含抽帧建数据集工具与自定义模型训练的 Jupyter notebook。随附 IEEE Xplore 论文（文档号 11204071），README 称特定 ROI 内检测计数准确率 98%。CLI 与 Python API 两种用法，视频素材仅限教育与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 实时人员检测与计数，支持自定义 ROI 与阈值告警
- 图形界面含状态色指示、统计面板与实时计数历史图
- 帧抽取工具与自定义模型训练 notebook
- 随附 IEEE Xplore 同行评审论文（文档号 11204071）

## 适用场景

- 对车站等场所的视频做实时人群密度监控与告警
- 用自有视频训练定制 YOLOv8 检测模型
- 抽取视频帧构建检测数据集

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L21: An advanced crowd analysis system for Peshawar's Bus Rapid Transit (BRT) using YOLOv8 and computer vision technique
> L32:  - Accurate people detection using YOLOv8

## 星数曲线

```mermaid
xychart-beta
    title "hassanrrraza/crowd-analysis-yolo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1fc732f6312e` · [字段定义](../../DATASET.md)*
