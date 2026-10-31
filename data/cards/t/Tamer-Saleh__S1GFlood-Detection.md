# Tamer-Saleh/S1GFlood-Detection

⭐ 56 · Python · CC0-1.0 · 推送 2026-05-23 · [GitHub](https://github.com/Tamer-Saleh/S1GFlood-Detection) · [官网](https://github.com/Tamer-Saleh/S1GFloods) · 组织维护 · 中文 README

**SAR 影像洪水检测模型 DAM-Net 与 S1GFloods 基准数据集**

武汉大学团队发表的 ISPRS JP&RS 2024 论文官方仓库：提出基于差分注意力度量的视觉 Transformer 网络 DAM-Net，从 Sentinel-1 SAR 前后事件影像对中检测新增淹没区域；孪生结构提取前后时相特征。随附 S1GFloods 基准数据集：5,360 对 256×256、10 米分辨率的影像对，覆盖 2015-2022 年六大洲 46 场洪水事件，含人工标注二值标签。仓库提供训练/测试脚本及 10 个基线模型链接。数据集仅限非商业与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DAM-Net：差分注意力度量视觉 Transformer 的 SAR 洪水检测网络
- S1GFloods 数据集：5,360 对影像、46 场洪水事件、六大洲分布
- 训练集 4,300 / 验证集 530 / 测试集 530 的固定划分
- 提供 train.py 与 eval.py 脚本及 10 个基线模型

## 适用场景

- 训练与评估 SAR 影像洪水制图模型
- 在 S1GFloods 基准上复现论文结果或对比基线
- 获取全球分布的洪水事件标注数据开展研究

## 场景标签

`目标检测` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L27: * **S1GFloods** is the first open-access, globally distributed, event-diverse Sentinel-1 SAR dataset specifically d
> L59: An overview of the proposed DAM-Net. The feature maps of the pre-and post-event image pairs are extracted through a

## 星数曲线

```mermaid
xychart-beta
    title "Tamer-Saleh/S1GFlood-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-31 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0377598d181b` · [字段定义](../../DATASET.md)*
