# Jouqio/climate-aware-pv-forecasting

⭐ 10 · Python · NOASSERTION · 推送 2026-08-03 · [GitHub](https://github.com/Jouqio/climate-aware-pv-forecasting) · 个人维护

**面向科研的印尼多站点光伏发电量预测与目标泄漏量化框架**

基于 NASA POWER 数据、XGBoost 与 SHAP 的可复现光伏输出预测研究框架，覆盖印尼 10 个地点、6 种气候类型。核心工作是量化确定性目标泄漏（各站点泄漏比 1.72×–3.43×）并评估气候驱动的可预测性，采用 9 折 walk-forward 验证、固定随机种子并在每折运行泄漏检查以保障可复现。新增站点只需放入 CSV 即可自动发现并重跑，无需改代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 量化 10 站点的确定性目标泄漏（1.72×–3.43×）并与 GHI 变率关联
- NASA POWER 数据 + XGBoost + SHAP 的完整可复现流水线
- 9 折 walk-forward 验证，每折每站运行泄漏检查，90/90 notebook 执行通过
- 新增站点零代码修改（CSV 自动发现）

## 适用场景

- 研究不同气候条件下光伏发电预测的特征泄漏问题
- 评估气象异常因子（GHI_anom、温度、湿度）对光伏预测的贡献
- 在新增站点上复用现有流水线做光伏预测实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: **Deterministic target leakage quantification and climate-aware
> L16: XGBoost
> L82: |Random seed|`np.random.seed(42)` for all stochastic components|

## 星数曲线

```mermaid
xychart-beta
    title "Jouqio/climate-aware-pv-forecasting 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-29 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d5c215dbf36c` · [字段定义](../../DATASET.md)*
