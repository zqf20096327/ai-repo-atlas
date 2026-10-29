# naturalis/sdmdl

⭐ 31 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/naturalis/sdmdl) · 组织维护

**用深度神经网络做物种分布建模的 Python 库**

面向生态学与生物多样性研究的面向对象 Python 包：从物种种群出现表与环境栅格图层出发，自动生成存在图、伪缺失样本与训练/预测数据集；训练带 dropout 的二分类 DNN（每物种多副本取最高 AUC），用 AUC 与自助置信区间评估，用 SHAP 估计变量重要性，输出 GeoTIFF 分布图与 PNG 可视化。超参数由 config.yml 控制。需自行安装系统级 GDAL 依赖，通过 git clone 加 pip 安装。方法基于 2019 年 bioRxiv 预印本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从出现表与环境栅格自动生成训练/预测数据集与伪缺失样本
- 每物种训练多副本 DNN 并保留最高 AUC 模型
- SHAP 变量重要性分析与自助置信区间评估
- 生成 GeoTIFF 物种分布图与 PNG 可视化

## 适用场景

- 根据环境变量建模物种的潜在地理分布
- 比较物种对环境因子的依赖程度（SHAP 重要性）
- 批量处理多物种出现数据并生成分布图

## 场景标签

 · 领域:生态学/生物多样性信息学

## 证据(README 行号)

> L7: An object-oriented Python package for species distribution modelling (SDM) using deep neural
> L16: trains binary classification DNNs with dropout regularisation, evaluates model performance using AUC

## 星数曲线

```mermaid
xychart-beta
    title "naturalis/sdmdl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `6df156509cdf` · [字段定义](../../DATASET.md)*
