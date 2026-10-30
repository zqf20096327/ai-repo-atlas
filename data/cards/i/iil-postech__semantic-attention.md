# iil-postech/semantic-attention

⭐ 16 · Jupyter Notebook · 推送 2026-01-22 · [GitHub](https://github.com/iil-postech/semantic-attention) · [官网](https://doi.org/10.1109/JIOT.2024.3440313) · 组织维护

**注意力感知语义通信协同推理的论文官方实现（IEEE IoTJ 2024）**

论文 "Attention-aware Semantic Communications for Collaborative Inference"（IEEE Internet of Things Journal 2024）的官方代码实现：边缘设备运行 DeiT-Tiny 弱分类器，按注意力分数选择图像 patch 传输给服务器端 DeiT-Base 强分类器，结合基于最小熵的不确定性度量决定是否发送整图，从而降低通信开销并提升协同分类准确率。提供多种注意力度量、patch 选择规则与不确定性度量的对比实验，含 shell 脚本、CPU 终端命令与 Colab 可视化笔记本。限非商业研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 边缘 DeiT-Tiny 与服务器 DeiT-Base 的协同推理
- 基于注意力分数的 patch 选择（均值注意力/attention rollout、阈值/top-k 等规则）
- 基于最小熵等度量的不确定性感知整图传输
- 提供 run.sh、CPU 运行命令与 Colab 可视化笔记本

## 适用场景

- 复现论文中注意力感知语义通信的协同推理实验
- 比较不同注意力度量与 patch 选择规则的通信开销与准确率
- 可视化注意力热图以分析 patch 选择过程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository provides the official implementation of "Attention-aware Semantic Communications for Collaborative I
> L10: - Edge device model: DeiT-Tiny
> L11: - Server model: DeiT-Base

## 星数曲线

```mermaid
xychart-beta
    title "iil-postech/semantic-attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cd370a213916` · [字段定义](../../DATASET.md)*
