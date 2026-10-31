# xinluo2018/WatNetv2

⭐ 15 · Jupyter Notebook · GPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/xinluo2018/WatNetv2) · 个人维护

**遥感地表水体提取模型：支持 Sentinel-2 与 Landsat 系列影像**

WatNetv2 是 WatNet 的改进版本，用于卫星影像的地表水体提取（surface water mapping），将数据适用范围从 Sentinel-2 影像扩展到 Landsat-5、7、8、9 影像。训练数据集在 WatSet 仓库（github.com/Hydrological-Observation-Group/WatSet）中准备。README 列出的待办项包括多尺度分块分割测试、DINOv3+decoder 结构测试与 SAM 模型尝试，表明仍在开发迭代中。README 未提供安装命令或使用说明细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 地表水体提取深度学习模型
- 支持 Sentinel-2 与 Landsat-5/7/8/9 影像
- 配套数据集 WatSet 单独仓库提供

## 适用场景

- 用 Landsat 历史影像提取地表水体
- 大范围地表水制图与水文分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: 1. The WatNetv2 is not applicable for Sentinel-2 image but also applicable for the Landsat series (Landsat-5, 7, 8 a
> L6: 2. The WatNetv2 achieved improved surface water mapping by comparing with WatNet.

## 星数曲线

```mermaid
xychart-beta
    title "xinluo2018/WatNetv2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3c3e03cb639a` · [字段定义](../../DATASET.md)*
