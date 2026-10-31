# Haiderkhan64/H64LM

⭐ 19 · Jupyter Notebook · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/Haiderkhan64/H64LM) · 个人维护

**面向研究的从零实现 MoE LLM 训练栈（249M，PyTorch）**

用 PyTorch 从零实现的现代 LLM 栈：GQA 注意力、RoPE、SwiGLU、奇偶交替的 dense/MoE 层（每 MoE 层 8 专家取 Top-2）、三个 MoE 辅助损失（负载均衡/多样性/Z-loss）、RMSNorm、因果+滑窗掩码。训练循环显式编写 AMP、梯度累积、AdamW 与线性调度，无 Trainer 抽象；单文件包含分词器加载、数据管道与检查点原子写入。附带的 249M 模型在 WikiText-103 切片上训练以验证流程，作者声明非生产框架：无分布式训练/专家并行，内置 generate 仅对 batch size 1 正确。

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

- GQA+RoPE+SwiGLU+稀疏 MoE 的单文件全显式实现
- MoE 三辅助损失（负载均衡/多样性/Z-loss）仅在训练时计算
- 检查点原子写入与断点续训（含 DataParallel 前缀剥离）
- Flash Attention 两级回退（不可导入或内核调用失败均回退标准注意力）

## 适用场景

- 逐行学习现代 LLM 架构各组件的实现机制
- 在小规模数据上端到端复现 MoE 训练流程
- 作为可检查的 MoE/注意力机制实验代码底座

## 场景标签

`模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A research-oriented, from-scratch implementation of a modern LLM stack in PyTorch. Every component attention, expert
> L9: - Full MoE implementation with three auxiliary routing losses not stubbed or approximated

## 星数曲线

```mermaid
xychart-beta
    title "Haiderkhan64/H64LM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `70a8305f6d69` · [字段定义](../../DATASET.md)*
