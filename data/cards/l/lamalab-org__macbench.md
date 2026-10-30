# lamalab-org/macbench

⭐ 25 · Python · MIT · 推送 2026-02-01 · [GitHub](https://github.com/lamalab-org/macbench) · 组织维护

**化学与材料科学多模态语言模型评测基准**

面向化学与材料研究领域多模态语言模型（VLM）的评测基准：人工策划覆盖科学生命周期全流程的任务，包括数据提取、实验执行与数据分析。本仓库收录评测报告并用于收集新贡献，基准数据集托管于 HuggingFace，通过 ChemBench 评测引擎运行；使用需 Python 3.10+ 并安装 chembench 包，配置模型供应商 API key 后以脚本方式执行，目前仅支持 batch_size=1，提供消融研究数据集与 HuggingFace Spaces 排行榜。

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

- 覆盖数据提取、实验执行到数据分析的科学生命周期任务
- 数据集托管于 HuggingFace，经 ChemBench 引擎运行
- 提供消融研究数据集（MaCBench-Ablations）与在线排行榜
- 附带论文与引用信息

## 适用场景

- 评测多模态语言模型在化学/材料任务上的表现
- 对比不同模型在科学数据分析任务中的结果
- 通过消融数据集研究任务设计对评测结果的影响

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L34: *MaCBench* is a benchmark for multimodal language models in chemistry and materials research. We manually curated a
> L37: The benchmark dataset itself is hosted on HuggingFace and can be run using the *ChemBench* benchmark engine. You ca

## 星数曲线

```mermaid
xychart-beta
    title "lamalab-org/macbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `870e7f4ea72a` · [字段定义](../../DATASET.md)*
