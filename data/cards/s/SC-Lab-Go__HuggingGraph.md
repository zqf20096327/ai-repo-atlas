# SC-Lab-Go/HuggingGraph

⭐ 14 · Python · 推送 2026-10-15 · [GitHub](https://github.com/SC-Lab-Go/HuggingGraph) · [官网](https://ai-supply-chain.github.io/) · 组织维护

**LLM 生态供应链的有向异构图数据集与构建管线**

CIKM 2025 论文配套仓库，提供 Hugging Face 模型、数据集、Spaces、库、许可、任务、agent 框架与 GitHub 仓库之间供应链关系的 DOT 格式异构图（v3 含 17 类关系、766 万条边、311 万个节点），并附 17 个 Python 脚本的构建管线、NetworkX 加载示例与 Graphviz 可视化说明。面向研究者、审计者与政策制定者做来源追溯与继承性风险调查。完整 v3 图较大，建议流式解析或抽取子图加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- v3 图含 17 类关系、7,666,919 条边、3,117,399 个节点
- 17 个 Python 脚本的图构建管线（模型谱系、数据集训练引用、Space 关系等）
- 带类型前缀的节点 ID 防止同名模型/数据集坍缩
- 提供 v0→v3 迁移兼容说明与 NetworkX/Graphviz 使用示例

## 适用场景

- 追溯模型微调、量化、合并的上游来源
- 审计模型/数据集继承的许可、安全与偏见风险
- 研究 Hugging Face 生态中库、任务、GitHub 仓库的关联结构

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: HuggingGraph is a directed, heterogeneous graph of supply-chain relationships
> L12: This repository contains artifacts related to the CIKM 2025 paper:
> L269: HuggingGraph supports forward and backward tracing of dependencies, helping

## 星数曲线

```mermaid
xychart-beta
    title "SC-Lab-Go/HuggingGraph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `84e7b70138e4` · [字段定义](../../DATASET.md)*
