# fchavelli/tsseg

⭐ 15 · Python · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/fchavelli/tsseg) · [官网](https://fchavelli.github.io/tsseg) · 组织维护

**Python 时间序列分割库：30+ 变点/状态检测算法统一 API**

tsseg 将变点检测（22 个检测器）与状态检测（9 个检测器）的 30 余种经典与近期算法整合到统一的 scikit-learn 风格接口（fit/predict），支持无监督与给定段数的引导模式，并配套 F1、Covering、Hausdorff、ARI/WARI、SMS 等评估指标。核心依赖仅 NumPy/pandas/SciPy/scikit-learn/statsmodels，PyTorch/TensorFlow/Prophet/numba 作为按需 extra 安装。面向时间序列分析与机器学习研究者及工程师，论文发表于 ECML-PKDD 2026 Demo Track，附带 Hugging Face Spaces 浏览器交互演示与 TSB-SEG 基准。限制：tsseg[all] 受 TensorFlow 版本约束需 Python 3.10-3.12；个别检测器（如 PatssDetector）已弃用且依赖需手动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 31 个检测器（22 变点 + 9 状态）统一 scikit-learn 风格 API
- 支持无监督与引导（给定段数）两种模式
- 变点与状态两类任务的完整评估指标集（含 WARI/WNMI/SMS）
- 浏览器交互演示（Hugging Face Spaces），无需安装

## 适用场景

- 对传感器或动作捕捉序列做变点检测定位行为转变
- 为每个时间点分配递归状态标签（状态检测）
- 在同一基准下比较多分割算法并计算评估指标

## 场景标签

 · 领域:机器学习/时间序列分析

## 证据(README 行号)

> L26: **tsseg** gathers classic and recent algorithms for **time series segmentation**
> L43: - **One API for every method.** Each detector is a scikit-learn estimator that

## 星数曲线

```mermaid
xychart-beta
    title "fchavelli/tsseg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bcdec8b0eec2` · [字段定义](../../DATASET.md)*
