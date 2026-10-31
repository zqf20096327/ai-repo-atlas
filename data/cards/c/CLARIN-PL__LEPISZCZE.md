# CLARIN-PL/LEPISZCZE

⭐ 15 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/CLARIN-PL/LEPISZCZE) · [官网](https://clarin-pl.github.io/LEPISZCZE/) · 组织维护

**波兰语综合 NLP 基准：代码、数据集与排行榜**

NeurIPS 2022 论文的官方代码实现，构建并运行覆盖波兰语 NLU 任务的 LEPISZCZE 基准：含情感分析、命名实体识别、词性标注、抽取式问答、文本蕴含等 13+ 数据集（HuggingFace 托管）、GitHub Pages 静态排行榜、W&B 实验面板。实验通过 DVC repro 与 W&B 日志复现，官方声明全流程在单 GPU 上需超 2,000 小时。另维护法律 AI（JuDDGES、AITAX）数据集注册表，数据集经版本冻结、许可与泄漏审查后进入排行榜。面向 NLP 研究者，支持 Poetry 与 Docker 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖分类、序列标注、问答等 13+ 波兰语任务数据集
- DVC repro + W&B 日志的实验复现机制
- GitHub Pages 静态排行榜（快照式构建，Actions 校验 schema）
- 法律 AI 数据集注册表：版本冻结、许可与泄漏审查后晋升排行榜

## 适用场景

- 在波兰语任务上评测和对比 NLP 模型
- 复现基准论文实验或查看公开排行榜
- 追踪波兰法律 AI 项目数据集的发布状态

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L2: This is the official code implementation for the LEPISZCZE benchmark experiments.
> L3: **"This is the way: designing and compiling LEPISZCZE, a comprehensive NLP benchmark for Polish"** (NeurIPS 2022)
> L18: |Datasets|LEPISZCZE Datasets are accessible through our HuggingFace Hub organization page.|HuggingFace|

## 星数曲线

```mermaid
xychart-beta
    title "CLARIN-PL/LEPISZCZE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `743f4ba849bb` · [字段定义](../../DATASET.md)*
