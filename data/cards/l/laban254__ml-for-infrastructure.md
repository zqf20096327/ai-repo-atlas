# laban254/ml-for-infrastructure

⭐ 27 · Jupyter Notebook · 推送 2026-08-16 · [GitHub](https://github.com/laban254/ml-for-infrastructure) · [官网](https://colab.research.google.com/github/laban254/ml-for-infrastructure/blob/main/05_sre_applications/anomaly_detection/prometheus_anomaly.ipynb) · 个人维护

**面向 SRE/DevOps 的机器学习教学 notebook 集（27 本）**

27 本 Jupyter notebook 组成的教学仓库，用基础设施真实场景（CPU 尖刺、日志流、延迟分布、模型漂移）讲授机器学习：Isolation Forest 异常检测、TF-IDF+KMeans 日志聚类、回归预测性扩容、KS-test 漂移检测等。notebook 内置交互滑块与练习，多数带已渲染输出可直接在 GitHub 阅读。可通过 Colab/Binder 免安装运行，或本地 git clone 后 pip 安装依赖，附 fetch_data.py 数据获取脚本与快速/完整双执行模式。

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

- Isolation Forest 异常检测与 KS-test 漂移检测，含交互滑块
- TF-IDF + KMeans 日志聚类与自动簇命名
- 每本 notebook 带 Open in Colab / Open in Binder 徽章，免安装运行
- fetch_data.py 带 MD5 校验，支持 quick/full 双执行模式

## 适用场景

- SRE/数据工程师通过真实运维场景学习机器学习
- 在 Colab 上免安装体验异常检测与漂移检测
- 事故复盘时参考可交互的可视化图表

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: 27 Jupyter notebooks that teach machine learning through real infrastructure scenarios — not Iris, not Titanic. Eve
> L57: Every notebook has **Open in Colab** and **Open in Binder** badges at the top — click one and it runs in a free clo

## 星数曲线

```mermaid
xychart-beta
    title "laban254/ml-for-infrastructure 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2cc981029b94` · [字段定义](../../DATASET.md)*
