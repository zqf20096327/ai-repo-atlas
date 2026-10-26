# cuicaihao/split_raster

⭐ 27 · Jupyter Notebook · MIT · 推送 2026-09-03 · [GitHub](https://github.com/cuicaihao/split_raster) · [官网](https://cuicaihao.github.io/split_raster/) · 个人维护

**给深度学习任务切分大图为小瓦片的 Python 库**

Python 包 splitraster，将大尺寸栅格图像（含遥感 GeoTIFF）切分为可指定尺寸与重叠度的瓦片，自动处理边缘填充与输出命名（0001.png 起顺序编号），支持 RGB 图与真值（GT）图同步切分、多波段多光谱影像，并提供随机采样函数生成固定数量瓦片用于早期实验。面向做图像分割（尤其卫星遥感）的开发者，作为深度学习/计算机视觉的数据预处理工具。核心依赖 numpy/tqdm/scikit-image，GeoTIFF 支持为可选扩展（需另装 GDAL）。安装方式为 pip/uv，提供 io 与 geo 两个模块及示例 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 大图切瓦片，可自定义瓦片尺寸与重叠度，自动填充与命名
- RGB 图与 GT 真值图同步切分，适配图像分割任务
- geo 模块支持多波段 GeoTIFF 遥感影像
- 随机采样函数生成固定数量瓦片用于早期实验

## 适用场景

- 把卫星影像切成小瓦片用于分割模型训练
- 为遥感图像分割任务同步切分输入图与标注图
- 实验初期用随机采样快速获取少量瓦片样本

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L16: Split Raster is an open-source and highly versatile Python package designed to easily break down large images into 
> L18: Initially developed by the author to provide optimal support for deep learning and computer vision tasks, Split Ras

## 星数曲线

```mermaid
xychart-beta
    title "cuicaihao/split_raster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `96a12c28422c` · [字段定义](../../DATASET.md)*
