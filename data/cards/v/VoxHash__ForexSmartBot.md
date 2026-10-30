# VoxHash/ForexSmartBot

⭐ 23 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/VoxHash/ForexSmartBot) · 组织维护

**PyQt6 桌面外汇自动交易机器人：多策略、风控与回测**

面向外汇交易者的桌面应用（Python/PyQt6）：内置 17+ 交易策略（其中 7 种基于机器学习）、Kelly 准则与回撤保护的风险管理、并行回测、实时组合与盈亏监控。支持 Paper 场馆、Binance Spot 沙盒与需显式开启（FSB_LIVE_TRADING=1）的币安主网实盘，多经纪商接入含 MT4 与 REST API。可选 CUDA GPU 加速 ML 训练推理、Rust 原生指标扩展（无扩展时自动回退 NumPy）。PyPI 安装，声明仅限教育与合法商业用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17+ 内置策略，其中 7 种 ML 方法
- Kelly 准则风险管理与回撤保护
- Paper 场馆与 Binance Spot 沙盒，实盘需显式开启并配 kill-switch
- 可选 CUDA 加速与 Rust（PyO3）原生指标扩展

## 适用场景

- 在桌面端运行自动化外汇交易策略并实时监控盈亏
- 用并行回测和历史数据验证策略
- 先在沙盒环境试跑策略再选择性开启实盘

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L8: > Professional-grade desktop application for automated forex trading with advanced risk management, multiple trading
> L15: - **Multi-Strategy Trading**: 17+ built-in strategies including 7 ML-based approaches
> L20: - **GPU Acceleration**: CUDA support for 5-20x faster ML training and inference

## 星数曲线

```mermaid
xychart-beta
    title "VoxHash/ForexSmartBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `91adc0ee3ea7` · [字段定义](../../DATASET.md)*
