# LSX-UniWue/SuperGLEBer

⭐ 23 · Python · 推送 2025-12-11 · [GitHub](https://github.com/LSX-UniWue/SuperGLEBer) · [官网](https://supergleber.professor-x.de/) · 组织维护

**德语理解评测基准套件：29 个任务评估德语 LLM**

面向德语自然语言理解评测的基准套件 SuperGLEBer，包含文档分类、序列标注、句子相似度、问答等 29 个任务，用于考察德语 LLM 的现状；更新分支新增 GermEval 2025 共享任务的 8 个任务，并支持 LLM2Vec 模型与双向掩码集成。实验通过 python src/train.py 以 yaml 配置驱动，可生成 k8s/slurm 集群调度文件；有配套论文（NAACL 2024）与在线榜单网站。

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

- 29 个德语 NLU 任务，覆盖分类/标注/相似度/问答
- 新增 GermEval 2025 共享任务的 8 个任务
- 支持 LLM2Vec 模型与双向掩码集成
- yaml 配置驱动实验，支持 k8s/slurm 集群调度

## 适用场景

- 用统一基准评测德语 LLM 或语言模型的表现
- 在集群上批量运行模型-任务实验
- 追踪德语理解任务的公开榜单结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: SuperGLEBer (German Language Understanding Evaluation Benchmark) is a broad Natural Language Understanding benchmark
> L4: Our benchmark consists of 29 different tasks ranging over different types like document classification, sequence tag

## 星数曲线

```mermaid
xychart-beta
    title "LSX-UniWue/SuperGLEBer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b7f395d30a79` · [字段定义](../../DATASET.md)*
