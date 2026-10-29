# ChiShengChen/neural-signals-101

⭐ 19 · Jupyter Notebook · MIT · 推送 2026-05-30 · [GitHub](https://github.com/ChiShengChen/neural-signals-101) · 个人维护 · 中文 README

**面向初学者的 EEG 机器学习与信号处理教程（可运行 notebooks）**

面向无 ML 与神经科学基础的大学初学者，以 16 章 Jupyter notebook 讲解从原始 EEG 记录到诚实评估的完整流程：数据加载、滤波/ICA 去噪、特征构建（CSP、黎曼协方差）、经典模型与深度网络（EEGNet、Transformer 等），全部可在笔记本 CPU 上数分钟内运行。核心主题是避免数据泄漏与诚实评估，规则在共享代码库中用代码强制执行（如仅提供被试级划分）。支持 Colab 一键运行或本地 make setup 安装，数据集由代码自动下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 章 notebook 覆盖从预处理到深度模型与诚实评估
- 反数据泄漏规则以代码强制执行（Leave-One-Subject-Out、leakage_safe_pipeline）
- 全部章节 CPU 数分钟可运行，数据集自动下载
- 提供 Colab 一键运行路径与三条学习路径分流

## 适用场景

- 神经 AI/ML 零基础学生系统学习 EEG 信号处理与建模
- ML 或神经背景研究者补齐对方的入门知识
- 学习如何做无泄漏的诚实评估以避免虚高分数

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L15: > Go from **raw brain recordings → preprocessing → features → models → an honest
> L17: > students new to neuro-AI/ML** — you only need basic Python. We assume **no** prior
> L103: - **Work through the notebooks in order** (`notebooks/00_*` → `15_*`). Each one is

## 星数曲线

```mermaid
xychart-beta
    title "ChiShengChen/neural-signals-101 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6e8cfb44c748` · [字段定义](../../DATASET.md)*
