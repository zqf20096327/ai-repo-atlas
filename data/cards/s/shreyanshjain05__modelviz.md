# shreyanshjain05/modelviz

⭐ 26 · Python · Apache-2.0 · 推送 2026-04-02 · [GitHub](https://github.com/shreyanshjain05/modelviz) · [官网](https://shreyanshjain05.github.io/modelviz/) · 个人维护

**把 PyTorch/Keras 网络结构渲染成 2D 图与交互式 3D 的可视化库**

面向深度学习初学者与研究者的 Python 可视化库：传入 PyTorch 或 TensorFlow/Keras 模型对象，自动检测框架并生成 Graphviz 2D 架构图（含层类型、形状、参数、ResNet 式跳跃连接、Conv+BN+ReLU 模式合并），或基于 Three.js 的交互式 3D 模型（每种层有对应几何形状），另有 Plotly 3D 备选渲染。可在 Jupyter/Colab/VSCode notebook 内联渲染，导出 PNG/SVG/PDF/HTML。2D 功能需安装 Graphviz 系统包，3D 无系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测 PyTorch 与 TensorFlow/Keras 模型
- Graphviz 2D 图支持跳跃连接、分支结构与常见层组合自动合并
- Three.js 交互式 3D 可视化，每种层类型对应特定几何形状
- 导出 PNG/SVG/PDF/交互式 HTML，内联渲染于 Jupyter/Colab

## 适用场景

- 为论文或报告生成网络架构图
- 在 notebook 中交互浏览模型结构以理解架构
- 对比展示含残差连接、分支的网络拓扑

## 场景标签

 · 领域:深度学习/可视化工具

## 证据(README 行号)

> L16: **modelviz** generates beautiful, publication-ready neural network architecture diagrams from your PyTorch and Tens
> L22: |🔍 **Auto-detection**|Automatically detects PyTorch and TensorFlow/Keras models|

## 星数曲线

```mermaid
xychart-beta
    title "shreyanshjain05/modelviz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ba4a34e4f892` · [字段定义](../../DATASET.md)*
