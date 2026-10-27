# pritom007/Network-Traffic-Classification

⭐ 42 · Jupyter Notebook · 推送 2026-06-02 · [GitHub](https://github.com/pritom007/Network-Traffic-Classification) · 个人维护

**面向科研的 SDN 网络流量分类：ML 实验、模型与数据集说明**

存储 Docker SDN 实验网络中采集的 30 万+网络流（nDPI 分析、100+协议归为 10 类）的机器学习研究工件：包含原始实验脚本、已保存模型、混淆矩阵，以及可复现实验的 Python CLI 工作流。使用 7 个流级特征训练 Decision Tree、Random Forest、KNN 等监督模型，论文报告 KNN 准确率 97.24%、PAA 99.29%。原始 pcap 与 CSV 数据集不在仓库内，需另行按说明获取。部分旧脚本含 Windows 机器路径，建议用新 CLI。

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

- 30 万+ 流量样本、100+ 协议归为 10 类的数据集（需另行获取）
- 提供现代 CLI 训练 decision-tree/random-forest/knn 模型并输出分类报告
- 保留原始研究脚本、模型与混淆矩阵供追溯
- 配套论文发表于 Connection Science (2021)

## 适用场景

- 复现论文中的网络流量分类实验
- 基于流级特征训练监督式流量分类模型
- 获取 SDN 环境下的标注流量数据做方法研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: Machine-learning experiments for classifying network traffic flows collected from a Docker-based SDN lab network. T
> L12: This repository includes the original research artifacts, saved models, confusion matrices, and a cleaner Python wo

## 星数曲线

```mermaid
xychart-beta
    title "pritom007/Network-Traffic-Classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `646c380ff6b6` · [字段定义](../../DATASET.md)*
