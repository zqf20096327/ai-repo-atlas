# MLRichter/receptive_field_analysis_toolbox

⭐ 118 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/MLRichter/receptive_field_analysis_toolbox) · 个人维护

**神经网络架构感受野分析与可视化库**

RFA-Toolbox 是一个 Python 库，通过感受野分析（RFA）在无需训练的情况下检测卷积神经网络中的低效层，并用 GraphViz 生成架构图可视化。支持从 PyTorch、TensorFlow/Keras 导入模型，或以自有图格式手动定义架构；可视化中自动将预测无效的层标红、临界层标橙。还可计算网络的可行输入分辨率范围。面向从事 CNN 架构设计与优化的开发者和研究人员。PyTorch 导入基于 JIT 反推计算图，forward 中不允许循环逻辑；TensorFlow 侧仅支持 keras.Model 对象。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需训练即可检测卷积网络中的无效层（unproductive/critical）
- 支持 PyTorch、TensorFlow/Keras 模型导入及自有图格式定义
- GraphViz 架构图可视化，按层状态自动标色
- 计算网络的可行输入分辨率范围

## 适用场景

- 在低分辨率训练前找出网络中无效的层以裁剪架构
- 可视化 CNN 架构并标注各层感受野状态
- 确定模型适用的输入分辨率上下限

## 场景标签

 · 领域:深度学习/模型分析

## 证据(README 行号)

> L29: This is RFA-Toolbox, a simple and easy-to-use library that allows you to optimize your neural network architectures
> L45: This library allows you to look for certain inefficiencies withing your convolutional neural network setup without

## 星数曲线

```mermaid
xychart-beta
    title "MLRichter/receptive_field_analysis_toolbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-26 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9f08793c621c` · [字段定义](../../DATASET.md)*
