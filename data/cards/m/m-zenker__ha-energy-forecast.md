# m-zenker/ha-energy-forecast

⭐ 21 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/m-zenker/ha-energy-forecast) · 个人维护

**Home Assistant 用电预测应用：48 小时家庭耗电 ML 预报**

运行于 AppDaemon 4.x 的 Home Assistant 应用，基于用户自有电网累计用电数据与本地天气训练两阶段机器学习模型（LightGBM，缺失时回退 scikit-learn GBR），逐小时更新未来 48 小时用电预测并带校准预测区间。包含 SHAP 特征解释、异常用电检测、滚动 MAE、热泵/热水意图建模、用电日模式聚类，以及可叠加电器运行计划的 what-if 场景 API。需要累计 kWh 传感器（total_increasing）、经纬度配置，无回填时需积累 48 小时数据才产出预测，2-4 周后精度提升。树莓派 armv7 需移除 lightgbm 自动回退。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段模型：日模式聚类先验 + 逐时天气/滞后特征微调
- 48 小时逐时预测，含校准 80% 预测区间与滚动 MAE
- Scenario API 可叠加电器运行计划做 what-if 计算
- SHAP 特征重要度与自然语言解释输出到 HA 传感器

## 适用场景

- 预测未来 48 小时家庭用电以规划电动车充电时段
- 对比实际用电检测异常耗电
- 模拟在不同时段运行洗碗机等电器对用电的影响

## 场景标签

 · 领域:家庭自动化/能源预测

## 证据(README 行号)

> L8: Plan EV charging, avoid bill surprises, and know your daily energy use before the day starts — using a two-stage mac
> L78: - **LightGBM with scikit-learn GBR fallback** — works on any hardware including armv7 Raspberry Pi (automatic fallb

## 星数曲线

```mermaid
xychart-beta
    title "m-zenker/ha-energy-forecast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e76edb52d381` · [字段定义](../../DATASET.md)*
