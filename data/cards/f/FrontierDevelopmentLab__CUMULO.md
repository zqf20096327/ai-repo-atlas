# FrontierDevelopmentLab/CUMULO

⭐ 31 · Jupyter Notebook · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/FrontierDevelopmentLab/CUMULO) · [官网](https://www.dropbox.com/sh/i3s9q2v2jjyk2it/AACxXnXfMF5wuIqLXqH4NJOra?dl=0) · 组织维护

**全球云分类基准数据集：30 万+ 标注多光谱卫星图像**

面向全球云分类模型训练与评测的基准数据集：融合 A-train 卫星星座的 MODIS（Aqua）与 2B-CLDCLASS-LIDAR（CloudSat CPR + CALIPSO CALIOP）两类卫星产品，包含 30 万以上 1km×1km 分辨率标注多光谱图像，覆盖 2008、2009、2016 年的逐日全球观测。数据以 NetCDF 格式存储，每 5 分钟一个 1354×2030 像素的 swath 文件；提供 Dropbox/rclone 同步下载方式（直接下载已标记弃用）、由 MODIS/CloudSat 原始文件生成 swath 的 pipeline.py 脚本及机器学习基线示例链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 万+ 标注多光谱图像，1km 分辨率，覆盖 2008/2009/2016 逐日全球
- 融合 MODIS 与 CloudSat/CALIPSO 两种卫星产品
- 提供从原始卫星文件生成 swath 的 pipeline.py 与特征提取源码
- NetCDF 格式，每个 swath 1354×2030 像素、每 5 分钟一个文件

## 适用场景

- 训练全球云分类模型并与其他工作对比
- 从 MODIS/CloudSat 原始数据复现或扩展数据集
- 研究云类型与气候相关的大规模遥感分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: a benchmark dataset for training and evaluating global cloud classification models.
> L10: It contains over 300k annotated multispectral images at 1km x 1km resolution, providing daily full coverage of the 

## 星数曲线

```mermaid
xychart-beta
    title "FrontierDevelopmentLab/CUMULO 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-29 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5e1c5ea1e5af` · [字段定义](../../DATASET.md)*
