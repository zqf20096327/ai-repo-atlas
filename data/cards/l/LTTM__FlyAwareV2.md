# LTTM/FlyAwareV2

⭐ 21 · Python · GPL-3.0 · 推送 2026-01-16 · [GitHub](https://github.com/LTTM/FlyAwareV2) · [官网](https://medialab.dei.unipd.it/paper_data/FlyAwareV2) · 组织维护

**面向城市场景理解的多模态无人机数据集（RGB/深度/语义，10万+）**

帕多瓦大学团队发布的 UAV 城市语义分割数据集：合成部分（约290GB）由修改版 CARLA 生成，覆盖 8 个城镇、3 个飞行高度、4 种天气；真实部分（约6GB）基于 UAVid 与 VisDrone 图像，经 MonoFog、img2img-turbo 等管线增强为雨/雾/夜间条件，深度图由单目深度估计生成。仓库另含数据生成、处理与基准评测代码（PyTorch），支持合成到真实的域适应研究。完整数据集约296GB，运行基准需 Python 3.8+ 与 PyTorch 1.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RGB/深度/语义三模态，10万+ 样本，4 种天气×3 个高度×8 个城镇
- CARLA 生成合成数据 + UAVid/VisDrone 真实图像天气增强
- 提供 RGB 与多模态语义分割基准及合成到真实域适应研究
- 配套数据生成、处理与评测代码（PyTorch）

## 适用场景

- 研究恶劣天气下鲁棒的无人机航拍语义分割
- 做合成到真实的域适应实验
- 为无人机城市感知模型提供标准化评测基准

## 场景标签

 · 领域:计算机视觉/UAV 遥感

## 证据(README 行号)

> L9: To address this limitation, we present FlyAwareV2, a novel multimodal dataset encompassing both real and synthetic U
> L10: Building upon the recently introduced SynDrone and FlyAware datasets, FlyAwareV2 introduces several new key contrib

## 星数曲线

```mermaid
xychart-beta
    title "LTTM/FlyAwareV2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f04b6204fbd0` · [字段定义](../../DATASET.md)*
