# RozhakDev/SmartCropAdvisor

⭐ 10 · Jupyter Notebook · MIT · 推送 2026-11-14 · [GitHub](https://github.com/RozhakDev/SmartCropAdvisor) · [官网](http://localhost:8501/) · 个人维护

**农民/农业决策者用 7 项土壤气候参数预测 22 种适种作物**

端到端农业推荐系统：离线训练部分用 Jupyter Notebook 从 2,200 行数据集训练 sklearn Pipeline（GaussianNB 为选中模型，测试集 accuracy 0.9955），实验配置集中在 settings.yaml 保证可复现；线上部分为 Streamlit 应用，通过 ArtifactLoader 加载模型工件，提供单样本预测（Top-K 概率图）、批量 CSV 推理（大小/行数限制与 CSV 注入防护）和模型评估展示三类界面。README 为印尼语。限制：模型仅覆盖训练数据相似的土壤气候条件，应用不自动重训模型。

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

- GaussianNB 模型从 7 项土壤/气候参数预测 22 种作物
- 单样本 Top-K 排名与批量 CSV 推理，含 Pydantic 输入校验与域界警告
- 实验配置集中 settings.yaml，提供 pytest 自动化测试
- 批量上传限制文件大小与行数，导出做 formula injection 防护

## 适用场景

- 根据土地的氮磷钾、pH 与气候数据获取适种作物建议
- 批量上传农田样本 CSV 一次性得到种植推荐
- 复现模型训练与评估流程做教学或研究

## 场景标签

`推荐系统` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L5: SmartCropAdvisor adalah aplikasi rekomendasi tanaman berbasis machine learning untuk memprediksi 22 jenis tanaman da
> L7: Proyek ini terdiri dari alur pelatihan model (`GaussianNB` dengan `0.9955` test accuracy dan `0.9954` F1 macro) dan 

## 星数曲线

```mermaid
xychart-beta
    title "RozhakDev/SmartCropAdvisor 星数(近 2 点)"
    x-axis ["2026-11-14", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-14 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `10e8422f6ad4` · [字段定义](../../DATASET.md)*
