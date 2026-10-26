# WeikaiTan/Toronto-3D

⭐ 303 · 推送 2025-10-30 · [GitHub](https://github.com/WeikaiTan/Toronto-3D) · 组织维护 · 中文 README

**城市道路移动激光雷达点云语义分割数据集（约1公里、7830万点）**

由滑铁卢大学 Geospatial Intelligence Lab 发布的大规模室外点云语义分割数据集：MLS 系统在多伦多采集，覆盖约 1 公里道路、约 7830 万个点，含 XYZ/RGB/Intensity/GPS 时间等 10 个属性，标注 8 类物体（道路、标线、建筑、电杆线、汽车、栅栏等）。README 提供公开论文链接、多方法基准结果表、UTM 坐标偏移的数据准备提示、已知标注问题清单，以及 OneDrive/百度网盘下载渠道。数据按 CC BY-NC 4.0 分发，附 RandLA-Net 与 KPFCNN 训练代码链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 7830 万点、8 个标注类别的移动 LiDAR 点云
- 收录 PointNet++/RandLA-Net 等数十种方法的分割基准结果
- 提供 UTM 坐标偏移的数据准备提示与已知问题说明

## 适用场景

- 我要在公开城市道路点云上训练和评测语义分割网络
- 我要对比我的模型与已发表方法的 mIoU 结果
- 我在做道路基础设施（标线/电杆线/栅栏）提取研究

## 场景标签

 · 领域:三维点云/遥感数据集

## 证据(README 行号)

> L7: Toronto-3D is a large-scale urban outdoor point cloud dataset acquired by an MLS system in Toronto, Canada for seman
> L115: Toronto-3D belongs to Geospatial Intelligence Lab), University of Waterloo. Toronto-3D is distributed under the CC

## 星数曲线

```mermaid
xychart-beta
    title "WeikaiTan/Toronto-3D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 302 --> 304
    line [303, 303]
```

2026-10-18 303 → 2026-10-26 303（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `66a79a1fb55c` · [字段定义](../../DATASET.md)*
