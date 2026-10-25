# HanxunH/CognitiveDistillation

⭐ — · [GitHub]() · 个人维护

**ICLR 2023 论文代码：提取图像内认知后门模式以检测后门样本**

论文《Distilling Cognitive Backdoor Patterns within an Image》的官方实现，通过在输入图像上提取受 L_p 范数约束的掩码来蒸馏认知后门模式，用于后门样本检测。以 Python 库形式调用（传入预训练模型与图像批，输出掩码），默认 PyTorch，另支持 PaddlePaddle、MindSpore、TensorFlow。提供 configs 目录的实验配置复现论文结果，可运行 CD/ABL/STRIP/FCT 等多种检测方法并计算 AUPRC/AUROC；部分触发器与模型权重需另行从外部仓库或网盘下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对预训练模型与图像批提取认知后门掩码
- 支持 PyTorch/PaddlePaddle/MindSpore/TensorFlow 四种框架
- 提供论文实验配置复现与多基线检测方法（CD/ABL/FCT/STRIP 等）对比
- 输出 AUPRC/AUROC 检测指标

## 适用场景

- 检测深度模型中被植入的后门样本
- 复现 ICLR 2023 论文实验结果
- 与其他后门检测基线方法做对比实验

## 场景标签

 · 领域:AI 安全/深度学习

## 证据(README 行号)

> L1: # Distilling Cognitive Backdoor Patterns within an Image: A SOTA Method for Backdoor Sample Detection
> L3: Code for ICLR 2023 Paper "Distilling Cognitive Backdoor Patterns within an Image"

## 星数曲线

```mermaid
xychart-beta
    title "HanxunH/CognitiveDistillation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b4f567bb3ded` · [字段定义](../../DATASET.md)*
