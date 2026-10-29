# mauriceqch/pcc_geo_cnn_v2

⭐ 78 · Python · MIT · 推送 2026-02-06 · [GitHub](https://github.com/mauriceqch/pcc_geo_cnn_v2) · 组织维护

**基于 CNN 的点云几何压缩研究代码：训练、编解码与评测**

Université Paris-Saclay 团队发布的论文《Improved Deep Point Cloud Geometry Compression》配套实现：以卷积模型对点云八叉树块进行有损几何压缩与解压，支持 D1/D2 两种优化目标，并提供训练、批量实验、失真度量、BD-Rate 对比与 LaTeX 表格生成等脚本。实验对比 MPEG G-PCC（trisoup/octree）。依赖 TensorFlow 1.15 + CUDA 10.0，部分 MPEG 工具（tmc13、dmetric）需在 MPEG Gitlab 注册获取；提供论文全部训练模型与结果数据下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 点云八叉树块的 CNN 有损几何压缩/解压（D1/D2 可选优化）
- 提供训练、批量实验、评测与论文图表生成全流程脚本
- 与 MPEG G-PCC（trisoup/octree）对比实验与 BD-Rate 计算
- 公开论文全部训练模型与实验数据（DOI 下载）

## 适用场景

- 复现论文的点云压缩实验与对比结果
- 训练自己的点云几何压缩模型
- 研究深度学习点云压缩的率失真表现

## 场景标签

 · 领域:多媒体信号处理/3D 点云压缩

## 证据(README 行号)

> L29: * Tensorflow 1.15.0 with CUDA 10.0.130 and cuDNN 7.4.2
> L31: * MPEG G-PCC codec mpeg-pcc-tmc13: necessary only to compare results with G-PCC,
> L165:  ├── compress_octree.py [Coding] Compress a point cloud

## 星数曲线

```mermaid
xychart-beta
    title "mauriceqch/pcc_geo_cnn_v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-29 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a7a4089c71bf` · [字段定义](../../DATASET.md)*
