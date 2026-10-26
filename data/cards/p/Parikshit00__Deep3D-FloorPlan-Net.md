# Parikshit00/Deep3D-FloorPlan-Net

⭐ 43 · Python · 推送 2026-06-28 · [GitHub](https://github.com/Parikshit00/Deep3D-FloorPlan-Net) · 个人维护

**室内 3D 点云转矢量平面图：RandLANet 分割+RANSAC 后处理**

面向室内扫描 .ply 点云的处理管线：先用 Open3D-ML 中预训练于 S3DIS 的 RandLANet 做逐点语义分割（14 类标签），再用迭代 RANSAC 拟合平面/圆柱几何基元，从 clutter 类回收误分点以精修结构元素；最后经曼哈顿正则化生成房间多边形，输出带尺寸标注的 DXF/PDF 工程图与参数化 IFC/BIM 模型，全程保持度量单位。给需要从扫描数据生成 CAD 就绪平面图的开发者/科研用户使用。README 未见安装命令细节（窗外标注 pypi）。圆柱精修为可选步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RandLANet 逐点语义分割（S3DIS 14 类标签）
- 迭代 RANSAC 平面/圆柱拟合从 clutter 池回收误分点
- 输出曼哈顿正则化的 DXF/PDF 工程图与 IFC/BIM 参数化模型
- 预训练权重缺失时自动通过 HTTP 下载

## 适用场景

- 把室内 3D 扫描点云转成 CAD 可用的矢量平面图
- 为 BIM 建模流程生成参数化 IFC 墙体/开洞模型
- 对点云分割结果做几何精修以补全墙体等结构元素

## 场景标签

 · 领域:计算机视觉/3D 重建

## 证据(README 行号)

> L15: 1. **Semantic Understanding:** The pipeline first employs a powerful 3D semantic segmentation model (**RandLANet**)
> L17: 3. **Engineering Floor Plan:** Finally, the refined 3D structural cloud is reduced to a metric, Manhattan-regulariz

## 星数曲线

```mermaid
xychart-beta
    title "Parikshit00/Deep3D-FloorPlan-Net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e18a1f4f7cb8` · [字段定义](../../DATASET.md)*
