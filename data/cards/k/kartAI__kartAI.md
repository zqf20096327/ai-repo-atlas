# kartAI/kartAI

⭐ 19 · Python · 推送 2025-12-12 · [GitHub](https://github.com/kartAI/kartAI) · 组织维护

**面向挪威建筑地图数据改进的航拍图像分割模型研究项目**

研究型仓库：用 AI 改进挪威建筑地图数据。通过配置文件定义图像源（WMS/WCS、Postgres、GDAL 可读文件）与矢量数据，生成训练数据集（默认懒加载），训练多种 TensorFlow 分割模型（unet、resnet、CSP 等，含三种自定义架构），并提供 Data teacher 模块迭代扩充数据集。面向项目贡献者，需访问图像数据源、Azure 资源及开发者提供的密钥文件与 IP 白名单方可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从多种图像源与矢量数据按配置文件生成训练数据集
- 7 种已实现的 TensorFlow 模型（含 3 种自定义架构）
- Data teacher 模块：模型与数据集迭代式共同改进
- compare_models 脚本批量测试模型与超参数

## 适用场景

- 为建筑分割任务生成训练数据并训练模型
- 迭代扩充训练数据集直至模型收敛
- 批量对比不同模型与超参数的表现

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L3: KartAi is a research project with the objective to use AI to improve the map data for buildings in Norway.
> L7: The repository allows you to easily create training data for any sort of vector data and a set of different image da
> L52: - unet

## 星数曲线

```mermaid
xychart-beta
    title "kartAI/kartAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9e62a72ddc0e` · [字段定义](../../DATASET.md)*
