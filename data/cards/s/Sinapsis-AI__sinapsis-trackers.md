# Sinapsis-AI/sinapsis-trackers

⭐ 15 · Python · AGPL-3.0 · 推送 2026-04-24 · [GitHub](https://github.com/Sinapsis-AI/sinapsis-trackers) · [官网](https://sinapsis.tech/) · 组织维护

**多目标跟踪模块包集合：提供 CoTracker/ByteTrack/SORT 等模板与演示**

Sinapsis 生态下的多目标跟踪 mono repo，含三个 Python 包：sinapsis-cotracker（Facebook Research Co-Tracker，支持离线/在线/可视化模式）、sinapsis-supervision（ByteTrack 实时多目标跟踪）、sinapsis-rf-trackers（SORT 与 DeepSORT，DeepSORT 可经 timm 配置 Re-ID 模型）。各包以模板形式提供，通过 pip/uv 从私有 PyPI 索引安装，附 Gradio 演示 webapp，可用 Docker Compose 或 uv 运行。采用 AGPLv3 许可并声明商业许可获取渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个模块包分别接入 CoTracker、ByteTrack、SORT/DeepSORT 跟踪算法
- DeepSORT 支持经 timm 库配置多种 Re-ID 模型
- 提供 Gradio 多目标跟踪演示 webapp，支持 Docker 与 uv 两种运行方式
- 通过 AGENT_CONFIG_PATH 环境变量切换 agent 配置

## 适用场景

- 在视频流中做实时多目标跟踪与可视化
- 对比或组合不同跟踪算法（CoTracker/ByteTrack/SORT/DeepSORT）
- 快速搭建跟踪演示应用验证算法效果

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11:  Mono repo with modular packages for multi-object tracking using advanced algorithms.
> L21: This mono repo consists of modular packages for implementing and visualizing multi-object tracking using various tr
> L119: This repository is organized into modular packages, each designed for specific integration with different tracking

## 星数曲线

```mermaid
xychart-beta
    title "Sinapsis-AI/sinapsis-trackers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b3e63916db52` · [字段定义](../../DATASET.md)*
