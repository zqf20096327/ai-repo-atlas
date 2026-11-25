# limi124/Geo-ML

⭐ 9 · Jupyter Notebook · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/limi124/Geo-ML) · 个人维护 · 中文 README

**面向地理/GIS/遥感方向读者的中文机器学习实战教程（8 章 Notebook）**

面向地理、GIS、遥感方向的中文开源实战教程，由 8 个 Jupyter Notebook 组成，覆盖从 GeoTIFF 数据检查、多源栅格对齐、训练表构建、空间分块验证到回归/树模型/XGBoost/KNN/SVR/MLP 建模与预测制图的完整流程，并以 SHAP 做变量归因解释。读者只需基础 Python 与栅格概念即可跟随。环境建议通过 Conda 安装以避免 GDAL 等二进制依赖冲突；案例数据经百度网盘分发，不在 MIT 许可范围内，也提供合成数据脚本免下载跑通。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 章循序渐进的 Jupyter Notebook 实战教程
- 多源异构栅格（26.7 m–10 km）对齐到统一参考网格
- 空间分块交叉验证应对空间自相关泄漏
- XGBoost 与 SHAP 可解释性分析及边界讨论

## 适用场景

- 学习遥感/地理栅格数据的机器学习建模全流程
- 掌握空间分块交叉验证以避免验证指标虚高
- 复现甘南县多源栅格回归预测制图案例

## 场景标签

`教程课程` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: 这是一套面向**地理、GIS、遥感方向**读者的中文开源实战教程。你不需要先啃完机器学习理论：只要有基础 Python 语法，能看懂经纬度、投影、栅格与像元，就可以跟着 8 个循序渐进的 Jupyter Notebook 完成从原
> L44: |**03**|构建训练表|怎样把二维栅格变成结构化样本表？|保留 `row/col/x/y` 定位、缺测统计、防泄漏 `Pipeline` 思想|
> L62: 地理空间依赖（GDAL、Rasterio、GeoPandas、PROJ）强烈建议通过 Conda 安装，避免单独 `pip install` 引发二进制依赖冲突：


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `802dbd16bff4` · [字段定义](../../DATASET.md)*
