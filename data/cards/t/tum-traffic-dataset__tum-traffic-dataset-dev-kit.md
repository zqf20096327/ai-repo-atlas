# tum-traffic-dataset/tum-traffic-dataset-dev-kit

⭐ 102 · Python · MIT · 推送 2026-04-24 · [GitHub](https://github.com/tum-traffic-dataset/tum-traffic-dataset-dev-kit) · [官网](https://innovation-mobility.com/tumtraf-dataset) · 组织维护

**TUM 交通数据集官方开发工具：数据加载、可视化与评测脚本**

面向自动驾驶与路侧感知研究者的数据集开发套件，配套慕尼黑附近 Providentia 测试场采集的 TUMTraf 多模态数据（相机图像、LiDAR 点云、3D 边界框标注、OpenLABEL 格式）。提供数据集加载器、内外参标定读取与投影矩阵计算、2D/3D 标注可视化、train/val 数据划分、点云配准与去噪、OpenLABEL 与 KITTI/nuScenes/YOLO/COCO 等格式互转，以及 3D 目标检测模型评测脚本。安装需 conda 环境加 PyTorch3D 等依赖，从源码以 PYTHONPATH 方式运行，无 pip 包发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 相机/LiDAR 数据与标定加载器，支持 2D/3D 标注可视化
- OpenLABEL 与 KITTI/nuScenes/OpenPCDet/COCO/YOLO 格式双向转换
- 点云配准、去噪与 train/val 划分等预处理脚本
- 3D 目标检测模型评测脚本（KITTI/OpenLABEL 预测格式）

## 适用场景

- 在 TUMTraf 数据集上训练和评测 3D 目标检测模型
- 将数据集标注转换为 KITTI/nuScenes/YOLO 等格式接入其他框架
- 可视化相机图像与点云中的 3D 边界框标注

## 场景标签

`目标检测` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  🚀 The TUM Traffic Dataset (`TUMTraf`) is based on roadside sensor data from the 3 km long Providentia Test Field fo
> L12: The Development Kit provides a dataset loader for images, point clouds, labels and calibration data. The calibratio
> L220: Finally, some model evaluation scripts are provided to benchmark your models on the TUMTraf Dataset.

## 星数曲线

```mermaid
xychart-beta
    title "tum-traffic-dataset/tum-traffic-dataset-dev-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-28 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6a59b2ee0d01` · [字段定义](../../DATASET.md)*
