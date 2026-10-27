# WenjieDu/TSDB

⭐ 241 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/WenjieDu/TSDB) · [官网](https://pypots.com/ecosystem/#TSDB) · 个人维护

**一行代码加载 173 个公开时间序列数据集的 Python 工具箱**

TSDB 是面向研究者与工程师的时间序列数据集加载工具箱，从 PyPOTS 项目分离而来，用于数据集与学习算法解耦。用户通过一行代码即可下载并加载 173 个公开数据集，覆盖医疗、电力、交通、空气质量等领域的预测、插补、分类任务。数据加载仅含通用步骤（如移除无效样本），不做归一化等处理，也可仅下载保存原始数据。以 Python 包形式提供，支持 pip、conda 与源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码下载并加载 173 个公开时间序列数据集
- 覆盖 UCR & UEA 全部 163 个分类数据集等多个领域
- 加载函数不做归一化等预处理，保留原始数据
- 用户可通过 issue/PR 申请集成新的开源数据集

## 适用场景

- 研究时间序列预测/插补/分类时快速获取标准数据集
- 跳过数据收集下载环节，专注数据处理细节
- 批量获取原始时间序列数据集用于本地预处理

## 场景标签

 · 领域:时间序列数据集/机器学习数据基础设施

## 证据(README 行号)

> L3: * load 173 public time-series datasets with a single line of code ;-) *
> L51: TSDB is created to help researchers and engineers get rid of data collecting and downloading, and focus back on dat

## 星数曲线

```mermaid
xychart-beta
    title "WenjieDu/TSDB 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 239 --> 242
    line [240, 241, 241]
```

2026-10-18 240 → 2026-10-27 241（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9f42b9c574d1` · [字段定义](../../DATASET.md)*
