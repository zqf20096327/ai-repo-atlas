# jakobtroidl/neuron-shape-reasoning

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-10-29 · [GitHub](https://github.com/jakobtroidl/neuron-shape-reasoning) · [官网](https://jakobtroidl.github.io/neuron-shape-reasoning/) · 个人维护

**神经元形态点云建模的 PyTorch 库：Point Affinity Transformer**

论文《Global Neuron Shape Reasoning with Point Affinity Transformers》的 PyTorch 实现，以 point-affinity-transformer 包发布于 PyPI（导入名 pat）。库读取 SWC 格式神经元形态文件生成点云，输入形状为 (B, N, 3+D) 的坐标加特征张量，仅需每点一个标签即可训练；提供 pad_batch、expand_features 等预处理工具与 config.yaml 训练入口，预设模型从 4.5M 到 1.4B 参数。面向神经科学研究与开发者，需先安装匹配 CUDA 版本的 PyTorch。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SWC 神经元文件读取并转为点云输入
- 支持 4.5M–1.4B 参数的多档预设模型与 depth 等自定义
- 3D 模型可扩展至 D 维特征后微调
- 提供 quickstart notebook 端到端示例

## 适用场景

- 对神经元形态点云做形状建模与推理
- 从 SWC 重建文件训练自定义形状模型
- 在已有 3D 模型上追加特征（如半径）微调

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L6: ## Point Affinity Transformers
> L25: Point clouds of shape `(B, N, 3)` with `D` extra features are passed to the model as `(B, N, 3 + D)`. Training only

## 星数曲线

```mermaid
xychart-beta
    title "jakobtroidl/neuron-shape-reasoning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c8e561e905c7` · [字段定义](../../DATASET.md)*
