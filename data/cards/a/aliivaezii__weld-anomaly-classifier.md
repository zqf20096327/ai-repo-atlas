# aliivaezii/weld-anomaly-classifier

⭐ 28 · Python · MIT · 推送 2026-03-06 · [GitHub](https://github.com/aliivaezii/weld-anomaly-classifier) · 组织维护

**多模态深度学习的焊缝缺陷自动分类系统**

面向工业焊接质量检测的多任务融合网络：同时读取传感器、音频、视频三类数据，经音频 1D-CNN、视频 MobileNetV3-Small、可选传感器分支提取 256 维特征并拼接，联合预测 7 类缺陷标签与二分类（良/缺陷）概率；训练后经类先验重平衡与置信度门控重分类两阶段后处理。提供预训练权重、端到端推理脚本与 Streamlit 监控面板；原始训练数据因体积未入库，复现需自行放置 Data/ 与 test_data/。

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

- 音频/视频/传感器三分支多任务融合（7 类 + 二分类）
- 两阶段后处理：类先验重平衡 + 置信度门控重分类
- 提供 11 MB 预训练 checkpoint 与端到端推理脚本
- Streamlit 仪表盘可视化训练指标与推理结果

## 适用场景

- 产线上自动判别焊缝缺陷类型与良/劣
- 复现并分析多模态焊接质检模型的训练流程
- 通过仪表盘查看特征分布与各类别性能

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L9: > Multimodal deep learning for automated weld quality inspection using sensor, audio, and video data.
> L76: **WeldFusionNet** is a multi-task learning fusion network that jointly predicts:

## 星数曲线

```mermaid
xychart-beta
    title "aliivaezii/weld-anomaly-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81847668f797` · [字段定义](../../DATASET.md)*
