# DavidHamlyn/GateFormer

⭐ 4 · HTML · 推送 2026-10-23 · [GitHub](https://github.com/DavidHamlyn/GateFormer) · [官网](https://davidhamlyn.github.io/GateFormer/) · 组织维护

**面向光伏科研人员的天空图太阳辐照预测论文页**

GateFormer 是发表于 Energy and AI (2026) 的论文项目页：从天空图像与近期辐照测量预测 GHI。共享的 GHI 条件化 Vision Transformer 输出轨迹预测与终点变化预测两个分支，经学习到的门控融合后做残差校正。仓库目前仅承载论文链接、结果摘要、引用信息与相关研究，代码尚未发布（coming soon）。结果在 NREL-TSI、Chilbolton、SIRTA 三个数据集上按论文评估协议报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于天空图像与 GHI 测量的短临（intra-hour）辐照预测模型
- Vision Transformer 双预测分支 + 学习门控融合 + 残差校正
- 论文结果：NREL-TSI +30min 125.01 W/m² RMSE，较 SIAT 低 9.6% RMSE
- 提供论文 DOI、arXiv、开放 PDF 与 BibTeX 引用

## 适用场景

- 查找天空图像太阳辐照预测的论文与引用信息
- 关注代码发布以复现论文结果
- 了解多模态（图像+时序）辐照预测的架构设计

## 场景标签

`科研工具` `多模态` · 领域:学习与行业

## 证据(README 行号)

> L25: GateFormer forecasts global horizontal irradiance (GHI) from sky imagery and recent irradiance measurements. A shar
> L43: **Code coming soon.** This repository currently serves as the paper’s project page. The implementation will be adde
> L8:  University of Southampton

## 星数曲线

```mermaid
xychart-beta
    title "DavidHamlyn/GateFormer 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-08", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-28 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a80eb36c334a` · [字段定义](../../DATASET.md)*
