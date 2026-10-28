# VG-GUI-TASKER/VG-GUI-TASKER

⭐ 20 · Python · 推送 2026-07-18 · [GitHub](https://github.com/VG-GUI-TASKER/VG-GUI-TASKER) · [官网](https://vg-gui-tasker.github.io/) · 组织维护

**视频引导 GUI agent 基准与关键帧提取算法 TASKER 的官方代码库**

ECCV 2026 论文的官方仓库，包含两部分：VG-GUI-Bench 是评测 MLLM GUI agent 能否依据教学视频完成长程交互任务的基准，含 1,000 个测试用例、标准化动作空间（CLICK/SCROLL/TYPE/PRESS/ZOOM/FINISH）与四项指标；TASKER 是将关键帧提取表述为广义图搜索的算法，利用 MLLM 评估代价函数与终止置信度来选取关键帧，覆盖 VideoQA 与 GUI 教程两阶段，提供 BFS/GBFS/Dijkstra/A* 变体。基于 MONDAY 数据集构建，面向视频理解与 GUI agent 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VG-GUI-Bench：1,000 个长程测试用例与四项评测指标
- TASKER 将关键帧提取表述为广义图搜索，含 BFS/GBFS/Dijkstra/A* 变体
- 同一搜索范式覆盖 VideoQA 与视频引导 GUI 任务两阶段
- 提供 Hugging Face 数据集与在线关键帧提取 Demo

## 适用场景

- 评测 MLLM GUI agent 依据视频教程完成交互任务的能力
- 为 VideoQA 或视频引导 agent 任务提取任务相关关键帧
- 复现论文实验或提交排行榜结果

## 场景标签

`模型评测` `图像视频处理` · 领域:评测与运维

## 证据(README 行号)

> L26: Recent Multimodal Large Language Models (MLLMs) achieve remarkable performance on Video Question Answering (VideoQA
> L28: We further observe that performance on both VideoQA and video-guided agentic tasks critically depends on effective 
> L42: |📱 **VG-GUI-Bench**|The Video-Guided GUI Agent benchmark: data pipeline, reference-frame modes, evaluation, and lea

## 星数曲线

```mermaid
xychart-beta
    title "VG-GUI-TASKER/VG-GUI-TASKER 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `590ab1f5fb03` · [字段定义](../../DATASET.md)*
