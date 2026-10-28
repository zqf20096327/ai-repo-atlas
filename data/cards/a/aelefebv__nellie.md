# aelefebv/nellie

⭐ 98 · Python · NOASSERTION · 推送 2026-05-15 · [GitHub](https://github.com/aelefebv/nellie) · 个人维护

**活细胞显微图像中细胞器自动分割、追踪与特征提取工具**

面向细胞生物学科研用户的自动化流水线：读取 2D/3D 活细胞显微图像（如 .ome.tif、.nd2），依据图像元数据自适应执行层级分割以解析亚细胞器区域，通过半径自适应模式匹配做运动追踪，并输出形态特征；可用于从单通道数据分离多种细胞器、量化线粒体响应等。以 Napari 插件形式提供图形界面，无需编程经验；可选装 cupy 实现 NVIDIA GPU 加速，需 Python 3.10+。作者声明项目处于早期阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 层级分割解析亚细胞器区域，按图像元数据自适应
- 半径自适应模式匹配实现运动追踪
- Napari 图形界面，无需编程经验
- 支持 2D/3D 及时间序列数据，可选 NVIDIA GPU 加速（cupy）

## 适用场景

- 对活细胞显微图像中的细胞器做自动分割与追踪
- 提取细胞器形态与运动特征用于定量分析
- 从单通道数据中分离多种细胞器

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: ## Automated organelle segmentation, tracking, and hierarchical feature extraction in 2D/3D live-cell microscopy
> L8: **Abstract:** Cellular organelles undergo constant morphological changes and dynamic interactions that are fundament

## 星数曲线

```mermaid
xychart-beta
    title "aelefebv/nellie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-28 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `50c92df2bc21` · [字段定义](../../DATASET.md)*
