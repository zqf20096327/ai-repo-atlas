# tangkai-RS/AnytimeFormer

⭐ 53 · Jupyter Notebook · 推送 2026-01-13 · [GitHub](https://github.com/tangkai-RS/AnytimeFormer) · [官网](https://doi.org/10.1016/j.rse.2025.115120) · 组织维护

**融合不规则 SAR-光学时序、重建任意时刻地表反射率的深度学习模型**

AnytimeFormer 是发表于 Remote Sensing of Environment 的遥感时序重建模型：将不规则光学与异步 SAR 时间序列融合，输出任意给定时间的无缺失地表反射率时序，支持 sequence-to-sequence 与 anytime 两种训练/推理模式。提供 Germany 站点预处理数据用于快速测试，其余站点可经 shapefile 与 Google Earth Engine 获取并预处理。通过 git clone 源码安装，依赖 Python 3.8、PyTorch (cu116) 与 GDAL 3.4.3，Linux 用 shell 脚本、Windows 直接修改 main.py 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持不规则光学与异步 SAR 时间序列融合
- 任意给定时刻的反射率重建（anytime 模式）
- 提供 Germany 站点预处理数据与 GEE 预处理脚本
- 输出填补图像、完整重建图像与精度指标

## 适用场景

- 重建云遮挡等原因造成缺失的卫星反射率时序
- 在任意指定日期生成无缝地表反射率产品
- 复现论文实验或开展 SAR-光学融合时序研究

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L24: 1.	Proposes AnytimeFormer for gap-free surface reflectance time series reconstruction.
> L26: 3.	AnytimeFormer supports reflectance reconstruction at any given time.
> L16: - **[2025-11-07]** **AnytimeFormer** has been accepted by *Remote Sensing of Environment (RSE)* ! [[Paper]](https:/

## 星数曲线

```mermaid
xychart-beta
    title "tangkai-RS/AnytimeFormer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d67baa33f065` · [字段定义](../../DATASET.md)*
