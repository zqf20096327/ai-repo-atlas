# westlake-repl/NineRec

⭐ 113 · Python · 推送 2026-10-29 · [GitHub](https://github.com/westlake-repl/NineRec) · 组织维护 · 中文 README

**多模态可迁移推荐系统的基准数据集套件（TPAMI 2024）**

西湖大学 ReLLIE 实验室发布的多模态多领域推荐基准数据集套件：包含 Bili_2M/Bili_500K 源数据集（含封面图像 JPG、用户-物品交互序列、中英文物品文本等格式文件）与九个下游跨域/跨平台数据集，用于评测推荐模型的可迁移性。数据经 Google Drive、百度网盘与 Zenodo 发布；仓库同时提供 PyTorch 环境说明、数据预处理脚本（get_lmdb.py、get_behaviour.py）与训练/测试脚本入口。配套 TransRec 模型采用端到端训练范式。限制：禁止私自修改数据集后提供二次下载。

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

- 多模态数据格式：封面图像（JPG）+ 用户-物品交互序列 + 中英文物品文本
- 覆盖跨域/跨平台迁移场景的源数据集与九个下游数据集
- 提供 PyTorch 代码环境说明与训练/测试脚本
- 数据经 Google Drive / 百度网盘 / Zenodo 三渠道发布

## 适用场景

- 我在做多域/跨域推荐模型研究，需要标准基准数据集评测迁移能力
- 我想预训练多模态推荐基础模型并做下游迁移实验
- 我需要带图像与文本的多模态推荐公开数据

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L1: # [TPAMI 2024] NineRec: A Benchmark Dataset Suite for Evaluating Transferable Recommendation
> L4: Multi-Modal
> L7: Recommendation
> L33: - Google Drive: Source Datasets, Downstream Datasets


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1d07a03124cc` · [字段定义](../../DATASET.md)*
