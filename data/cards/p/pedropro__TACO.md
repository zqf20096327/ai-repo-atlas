# pedropro/TACO

⭐ 775 · Jupyter Notebook · MIT · 推送 2026-10-20 · [GitHub](https://github.com/pedropro/TACO) · [官网](http://tacodataset.org) · 组织维护

**野外垃圾图像数据集与工具包：训练评估垃圾检测算法**

TACO（Trash Annotations in Context）是持续扩充的野外垃圾图像数据集：在森林、道路、海滩等多环境采集垃圾图像，按层级分类法人工标注并提供实例分割标注，格式兼容 COCO，用于训练和评估目标检测算法。配套 Python API 提供 download.py 下载脚本、jupyter notebook 检查与可视化标注，并附带基于 Matterport Mask R-CNN 的检测实现与数据集划分脚本。另有未标注图像 URL 列表与网站提交的未审核标注文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多环境垃圾图像，按层级分类法人工标注与分割
- 标注采用 COCO 格式，附带 paper（arXiv:2003.06975）
- 提供 download.py 下载脚本与 demo notebook 检查标注
- 附 Matterport Mask R-CNN 检测实现与 split_dataset.py 划分脚本

## 适用场景

- 训练和评估垃圾/废弃物目标检测模型
- 获取多环境带实例分割标注的垃圾图像数据
- 利用未标注图像 URL 列表扩展自建数据集

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: TACO is a growing image dataset of waste in the wild. It contains images of litter taken under
> L3: according to a hierarchical taxonomy to train and evaluate object detection algorithms. Currently,

## 星数曲线

```mermaid
xychart-beta
    title "pedropro/TACO 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-24"]
    y-axis "stars" 774 --> 776
    line [775, 775]
```

2026-10-22 775 → 2026-10-24 775（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `7acf76480f7b` · [字段定义](../../DATASET.md)*
