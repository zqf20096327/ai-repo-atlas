# PhysiologicAILab/iBVP-Dataset

⭐ 27 · Python · NOASSERTION · 推送 2026-04-07 · [GitHub](https://github.com/PhysiologicAILab/iBVP-Dataset) · [官网](https://doi.org/10.3390/electronics13071334) · 组织维护

**RGB-热红外 rPPG 数据集：372 分钟视频与高分辨率信号质量标签**

面向学术研究的远程生理测量数据集：采集 124 个会话共 372 分钟同步 RGB（640×480）与热红外（640×512）视频，配以耳部 PPG 真值信号、人工标注及 SQA-PhysMD 模型生成的逐样本信号质量标签。每名参与者经历慢呼吸休息、简单/困难数学任务与头部运动四种条件。数据压缩后约 400 GB，仅限学术用途，需由学术导师签署 EULA 向作者申请获取。配套代码集成于 rPPG-Toolbox，另提供 iBVPNet 模型、MACC 评估指标与 SQA-PhysMD 推理代码链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RGB 与热红外视频同步采集，各 30 FPS，共 372 分钟
- 人工标注 + SQA-PhysMD 模型的逐样本信号质量标签
- 四种实验条件诱发心理生理状态与头部运动变化
- 配套 dataloader 集成于 rPPG-Toolbox

## 适用场景

- 训练与评测 rPPG（远程光电容积描记）方法
- 基准测试 PPG 信号质量评估算法
- 研究心理生理状态变化下的生理信号测量

## 场景标签

 · 领域:计算机视觉/生理计算

## 证据(README 行号)

> L9: The iBVP dataset is a collection of synchronized RGB and thermal infrared videos with PPG ground-truth signals acqui
> L13: We have released the iBVP dataset **only for academic research purposes**. The dataset can be requested from the au

## 星数曲线

```mermaid
xychart-beta
    title "PhysiologicAILab/iBVP-Dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7b835f4e5de3` · [字段定义](../../DATASET.md)*
