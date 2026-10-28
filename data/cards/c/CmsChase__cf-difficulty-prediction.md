# CmsChase/cf-difficulty-prediction

⭐ 33 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/CmsChase/cf-difficulty-prediction) · [官网](https://cmschase.github.io/cf-difficulty-prediction/) · 个人维护

**预测 Codeforces 题目难度评分的可复现 ML 研究流水线**

从 Codeforces 官方 API 元数据、解题统计、曝光感知特征与题面结构特征出发，训练回归模型预测题目评分，区分发布后预测与冷启动（无解题统计）两种设定，并进行时间序验证与滚动窗口分析。含公开勘误：早期论文因切分配置错配与测试知情选型被标记为回顾性结果，另提供冻结的 statement-only 回测及 SHA-256 清单校验器。以 Python 源码仓库形式提供，包含 fetch/preprocess/features 等模块化命令与 pytest 测试，CI 在 Windows 和 Linux 上运行。

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

- 区分发布后与冷启动两种预测设定的评估流水线
- 含勘误声明与冻结 statement-only 回测（MAE 477.2→401.3）
- SHA-256 清单校验器可复核已提交的锁定结果
- 题面结构特征覆盖 99.3%（10,906/10,979 行）

## 适用场景

- 复现或审计 Codeforces 难度预测实验
- 研究冷启动与时间漂移设定下的难度预测方法
- 作为带勘误与锁定证据的研究流水线参考实现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: A research pipeline for predicting Codeforces problem ratings from official API
> L76: How well can Codeforces problem difficulty be predicted across

## 星数曲线

```mermaid
xychart-beta
    title "CmsChase/cf-difficulty-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2384e9a8e85a` · [字段定义](../../DATASET.md)*
