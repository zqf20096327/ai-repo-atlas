# krishnanlab/obnb

⭐ 22 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/krishnanlab/obnb) · [官网](https://obnb.readthedocs.io) · 组织维护

**生物医学网络基准图数据集构建的 Python 工具包**

OBNB 面向网络生物学研究者，提供基于生物医学网络与基因注释构建基准图数据集的高层构造器，默认采用按研究偏置划分的 6/2/2 训练/验证/测试切分。数据集对象可转换为兼容 PyTorch Geometric 与 Deep Graph Library 的形式，并提供 trainer 对象评估逻辑回归、标签传播及 GNN 模型。支持自定义网络与标签加载、数据划分和过滤组合。通过 pip 从 PyPI 安装，PyG/DGL 为可选依赖，另附安装脚本（含 CUDA 选项）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 高层数据集构造器，默认 study-bias holdout 6/2/2 切分
- 提供兼容 PyG 与 DGL 的数据集对象
- 内置评估逻辑回归、标签传播与 GNN 的 trainer
- 支持自定义网络/标签加载、划分与过滤组合

## 适用场景

- 为图神经网络模型准备生物医学网络基准数据
- 在基因功能与疾病关联任务上评估 GNN 或图嵌入方法
- 按自定义规则构建带切分的生物网络数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: The Open Biomedical Network Benchmark (OBNB) is a comprehensive resource for setting up benchmarking graph datasets
> L15: To make this adoption convenient, OBNB also provides dataset objects compatible with popular graph deep learning fr

## 星数曲线

```mermaid
xychart-beta
    title "krishnanlab/obnb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `67cf56c6930d` · [字段定义](../../DATASET.md)*
