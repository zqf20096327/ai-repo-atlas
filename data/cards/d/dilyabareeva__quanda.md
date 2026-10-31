# dilyabareeva/quanda

⭐ 61 · Jupyter Notebook · MIT · 推送 2026-09-30 · [GitHub](https://github.com/dilyabareeva/quanda) · [官网](https://quanda.readthedocs.io) · 个人维护

**训练数据归因（TDA）方法的定量评测工具包**

基于 PyTorch 的可解释性工具包，用于系统化评测训练数据归因（TDA）方法。提供统一接口接入 Captum、TRAK、Representer Point Selection、Kronfluence、Dattri 等库的归因方法，并实现 11 种评测指标（Linear Datamodeling Score、Class Detection、Mislabeled Data Detection、Shortcut Detection、MRR 等），附预计算 benchmark 可即插即用。开发中状态，要求 Python 3.10-3.12，本地克隆后 pip install -e . 安装。面向研究人员与从业者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 TDA 接口，可切换 Captum/TRAK/Kronfluence/Dattri 等 5 个库的方法
- 11 种评测指标，覆盖 Ground Truth、下游任务评估器与启发式三类
- 预计算 benchmark（MNIST/CIFAR-10/AWA2/QNLI/GPT-2）即插即用
- 可生成带 ground truth 的受控评测环境并对比多种 TDA 方法

## 适用场景

- 对比评测不同训练数据归因方法的表现
- 复用预计算 benchmark 快速验证新归因方法
- 模型调试、误标数据检测、事实溯源等场景中的归因质量评估

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3:  Interpretability toolkit for quan titative evaluation of d ata a ttribution methods in PyTorch .
> L33:  quanda is designed to meet the need of a comprehensive and systematic evaluation framework, allowing practitioners
> L38: - **Metrics**: **quanda** provides a set of metrics to evaluate the effectiveness of TDA methods. These metrics are

## 星数曲线

```mermaid
xychart-beta
    title "dilyabareeva/quanda 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-31 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1ca9f9230844` · [字段定义](../../DATASET.md)*
