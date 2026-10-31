# rfonod/deepsleep2

⭐ 22 · Jupyter Notebook · MIT · 推送 2026-07-10 · [GitHub](https://github.com/rfonod/deepsleep2) · [官网](https://doi.org/10.3390/ai3010010) · 个人维护

**从整夜 PSG 记录逐 5ms 分割睡眠觉醒事件的轻量 U-Net**

PyTorch 实现的一维全卷积编解码网络（740,551 参数），输入整夜 13 通道多导睡眠图（200 Hz，零填充至 2²³ 采样），单次前向传播输出每个 5ms 时间步的觉醒概率，无需分窗。训练/评测基于 PhysioNet/CinC 2018 数据集（约 135 GB，需自行下载），使用 Masked BCE 损失与官方 score2018.py 评分，最佳配置在 249 条测试记录上达到 AUPRC 0.4504 / AUROC 0.9012。仓库附带 4 组预训练检查点，全部流程通过单一 Jupyter notebook 运行，面向睡眠医学 AI 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 740,551 参数的 5 级一维 U-Net，整夜 PSG 端到端处理
- 原生 5ms 分辨率逐样本觉醒概率输出，无推理分窗
- 附带 4 组预训练检查点，可免训练复现结果表
- AUPRC 优先评测，使用官方 PhysioNet score2018.py 评分

## 适用场景

- 复现论文中睡眠觉醒分割的评测结果
- 在 PhysioNet/CinC 2018 数据上训练或微调觉醒分割模型
- 用预训练检查点对整夜 PSG 记录做觉醒概率预测

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: **DeepSleep 2.0** is a compact, U-Net-inspired **1D fully convolutional network** that segments non-apnea **sleep ar
> L16: Sleep arousals are brief intrusions of wakefulness that fragment sleep. Detecting them from PSG is laborious to do 

## 星数曲线

```mermaid
xychart-beta
    title "rfonod/deepsleep2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c9bda4cb48f0` · [字段定义](../../DATASET.md)*
