# AdilShamim8/AI-for-Digital-Safety

⭐ 6 · Jupyter Notebook · MIT · 推送 2026-10-11 · [GitHub](https://github.com/AdilShamim8/AI-for-Digital-Safety) · 个人维护

**有害内容分类竞赛结果与实验记录的复现审计库**

保存 HerWILL 有害内容分类任务的 notebook 与数据集，并记录对评估、推理与参数计算的回顾性审计。核心机制包括：SHA-256 结果台账、无需重训的验证脚本（make verify 系列仅用标准库检查引用、数据与清单）、可独立重跑全部实验的 runner 与作者复现 notebook。论文基于 ICIEV/IJCVSP 模板，尚有伦理措辞与独立复现等待完成，包未经直接投稿认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SHA-256 科学台账记录折叠、概率、诊断与实际执行记录
- make verify 仅用 Python 标准库，检查引用、数据、ZIP 与清单
- 保留预测可重打分，无需重训 TF-IDF 基础模型
- 提供顺序执行的独立复现 runner 与未执行的复现 notebook

## 适用场景

- 核验已保存的分类实验结果而不重跑训练
- 独立重跑实验并与历史记录对比后认证复现
- 查阅 LR/TF-IDF 源算力对比的审计配置与结果

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L1: # LightBanglaHC harmful-content classification audit
> L3: This repository preserves the supplied HerWILL notebooks and datasets and records a retrospective audit of evaluatio

## 星数曲线

```mermaid
xychart-beta
    title "AdilShamim8/AI-for-Digital-Safety 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-22"]
    y-axis "stars" 5 --> 7
    line [6, 6]
```

2026-10-30 6 → 2026-11-22 6（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d0087f12fdaa` · [字段定义](../../DATASET.md)*
