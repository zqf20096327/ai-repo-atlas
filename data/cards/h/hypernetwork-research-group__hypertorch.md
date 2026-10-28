# hypernetwork-research-group/hypertorch

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/hypernetwork-research-group/hypertorch) · [官网](https://hypernetwork-research-group.github.io/hypertorch/) · 组织维护

**超图学习模型的训练与基准评测 Python 库**

面向研究者的超图学习库：提供超图数据集加载（HIF 格式转类型化张量）、训练、评测与结果导出（Markdown/LaTeX）的标准化流程，覆盖超边预测与节点分类两类任务。模型可实现为标准 Lightning 模块，内置数据集、采样、负采样、特征增强组件与多个基线模型。需 Python 3.10+，CPU 安装需先装平台对应的 PyTorch 与 PyG，再从 PyPI 安装；源码安装用 make setup。可选 TensorBoard 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HIF 格式（.json/.json.zst）加载并转为类型化 HData 张量对象
- 超边预测与节点分类的即用训练管线
- 可复用 trainers/samplers/metrics/loggers 与 Markdown/LaTeX 结果导出
- 内置模型、层、聚合器、损失等神经组件，支持自定义 Lightning 模块对比基线

## 适用场景

- 在共享数据集上基准评测已有超图学习模型
- 开发自定义 PyTorch/Lightning 模型并与内置基线对比
- 加载本地或远程 HIF 数据集运行统一训练、评测与报告流程

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L63: HyperTorch is a library for hypergraph learning and benchmarking. It provides standardized workflows for loading hy
> L82: |**Hyperlink prediction**|Use ready-to-train hyperlink prediction pipelines|`hypertorch.hyperlink_prediction`|
> L83: |**Node classification**|Use ready-to-train node classification pipelines|`hypertorch.node_classification`|

## 星数曲线

```mermaid
xychart-beta
    title "hypernetwork-research-group/hypertorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e9a560479c6c` · [字段定义](../../DATASET.md)*
