# Neyt/How-To-Backtest-Correctly

⭐ 16 · MIT · 推送 2026-03-05 · [GitHub](https://github.com/Neyt/How-To-Backtest-Correctly) · 个人维护

**量化回测方法论库：实现 AFML 的标签、CV 与统计检验工具**

基于 Lopez de Prado《Advances in Financial Machine Learning》方法论的 Python 框架，面向量化交易员、资产管理人与数据科学家。实现 Triple-Barrier 标签、Meta-Labeling 双模型架构（方向与置信度分离）、Purging/Embargoing 防泄漏交叉验证、CPCV 组合回测路径生成、PSR/DSR/MinTRL 统计推断与 PBO 过拟合检测。以源码方式提供，git clone 后 pip 安装依赖运行，定位为原书伴生指南而非替代。

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

- Triple-Barrier 路径感知标签与 Meta-Labeling 双模型架构
- Purging/Embargoing 消除时间序列交叉验证信息泄漏
- CPCV 生成多条回测路径替代单一 Walk-Forward
- PSR/DSR/MinTRL/PBO 等统计检验工具

## 适用场景

- 在实盘前用 CPCV 与 PBO 检验策略是否过拟合
- 用 Triple-Barrier 与 Meta-Labeling 替代朴素标签训练模型
- 按 AFML 方法做可复现的量化研究

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **The open-source implementation of Marcos Lopez de Prado's *Advances in Financial Machine Learning* methodologies.*
> L34: |**Meta-Labeling (Corrective AI)**|Splits side prediction from size/confidence -- dramatically improves F1-score|Re
> L59: - **Meta-Labeling (Corrective AI):** A two-model architecture that separates *direction* from *conviction*:

## 星数曲线

```mermaid
xychart-beta
    title "Neyt/How-To-Backtest-Correctly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b8b1e8bd4bff` · [字段定义](../../DATASET.md)*
