# oliversefrin/soil-texture-processing

⭐ 14 · Jupyter Notebook · NOASSERTION · 推送 2026-02-01 · [GitHub](https://github.com/oliversefrin/soil-texture-processing) · 组织维护

**从 Sentinel-2 影像生成机器学习训练与分类数据**

由 Oliver Sefrin、Felix M. Riese 与 Sina Keller 编写的 Python/shell 脚本集：读取多光谱 Sentinel-2 卫星影像与同区域的 shapefile，用 GDAL 完成裁剪、栅格化、掩膜生成与波段合并，把地面真值作为最后一条波段合并进 GeoTIFF；再按指定 tile 尺寸与间隙切分像素瓦片，用固定随机种子拆分为 train/test/validation 三个 CSV 子集，或输出全量像素 CSV 供预测使用。面向做遥感机器学习（土地分类等）的开发者与科研用户，需自行准备 Sentinel-2 数据与 shapefile，按指定目录结构组织文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GDAL 完成裁剪、栅格化、掩膜生成与波段合并的完整流水线
- 地面真值作为最后波段合并，X 为 Sentinel-2 波段、Y 为 Ground Truth
- 固定随机种子的 tile 级 train/test/validation 随机切分
- 输出带索引的全像素 CSV，可按 C-ordering 还原为 2D 地图

## 适用场景

- 为遥感土地分类模型准备训练数据集
- 把 shapefile 中的地面真值参数栅格化并与卫星影像波段对齐
- 将影像切成瓦片并做可复现的训练/验证/测试划分

## 场景标签

 · 领域:遥感/地理空间数据处理

## 证据(README 行号)

> L9: This git repository provides tools to generate training and classification data for machine learning purposes from m
> L138: Setting *USE*=*TRAIN* allows to use the result for training of a Machine Learning model with the Sentinel-2 bands 

## 星数曲线

```mermaid
xychart-beta
    title "oliversefrin/soil-texture-processing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8f4dc48e8d13` · [字段定义](../../DATASET.md)*
