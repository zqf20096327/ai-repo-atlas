# WinfredGe/EventTSF

⭐ 22 · Python · Apache-2.0 · 推送 2026-07-20 · [GitHub](https://github.com/WinfredGe/EventTSF) · [官网](https://arxiv.org/abs/2508.13434v2) · 组织维护

**事件感知的非平稳时间序列预测框架（IJCAI 2026 论文官方实现）**

自回归扩散框架，通过联合建模历史观测与文本事件进行非平稳时间序列预测，捕获事件引发的分布突变。核心组件包括事件同步表示、AR-Diffusion 预测器、事件感知时间步调度器与多模态 U 型扩散 Transformer（M-U-DiT），并提供 7 个事件感知预测数据集（合成信号、大气物理、交通、天气）。面向时序预测研究者：Python 3.11 + PyTorch 2.5.0 + CUDA 12.1.1 环境，支持 Docker 构建，实验通过 Hydra 配置、run.sh 脚本复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 细粒度文本事件与时间序列段对齐的多模态表示
- 自回归扩散预测器生成不确定性感知的预测
- 可学习的事件条件时间步重参数化调度
- 附带 7 个事件感知预测数据集

## 适用场景

- 预测受节假日、天气、促销、新闻等外部事件影响的时序数据
- 研究非平稳时间序列中的分布突变建模
- 复现 IJCAI 2026 论文实验结果

## 场景标签

 · 领域:机器学习/时间序列预测

## 证据(README 行号)

> L11: **EventTSF is an event-aware autoregressive diffusion framework that forecasts non-stationary time series by jointl
> L22: EventTSF uses an autoregressive diffusion framework with event-aware timestep sampling to generate uncertainty-awar

## 星数曲线

```mermaid
xychart-beta
    title "WinfredGe/EventTSF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e9f8e2efa0b` · [字段定义](../../DATASET.md)*
