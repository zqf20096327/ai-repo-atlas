# sylvain-wei/TIME

⭐ 33 · Python · 推送 2026-09-29 · [GitHub](https://github.com/sylvain-wei/TIME) · [官网](https://sylvain-wei.github.io/TIME/) · 组织维护

**评测 LLM 真实场景时序推理的多级基准数据集**

NeurIPS 2025 (Spotlight) Datasets & Benchmarks 论文的配套基准：TIME 含 38,522 个 QA 对，覆盖 3 个层级、11 项细粒度任务，分为 TIME-Wiki、TIME-News、TIME-Dial 三个场景组，分别对应密集时序信息、快速变化事件动态与社交对话中的复杂时序依赖。另提供人工标注子集 TIME-Lite（943 QA 对）用于标准化评测。仓库提供 Git LFS 克隆、脚本下载 Hugging Face 数据集与评测脚本，提示词模板未随仓库发布，需本地适配脚本参数。

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

- 38,522 QA 对、3 层级 11 项细粒度时序任务
- TIME-Wiki / TIME-News / TIME-Dial 三个真实场景组
- 人工标注子集 TIME-Lite（943 QA 对）用于标准化评测
- 数据集发布于 Hugging Face，附评测脚本

## 适用场景

- 评测 LLM 在真实场景下的时序推理能力
- 研究测试时扩展（test-time scaling）对时序推理的影响
- 对比推理型与非推理型模型的时序表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L33: **TIME** is a benchmark for temporal reasoning in real-world scenarios. It contains **38,522 QA pairs** across **3 
> L35: We evaluate reasoning and non-reasoning models across these scenarios and tasks, and study how test-time scaling af

## 星数曲线

```mermaid
xychart-beta
    title "sylvain-wei/TIME 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d7a01590b66c` · [字段定义](../../DATASET.md)*
