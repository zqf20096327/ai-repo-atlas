# alibaba/graph-gpt

⭐ 108 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/alibaba/graph-gpt) · 组织维护 · 中文 README

**面向科研的图学习生成式预训练模型（ICML2025 官方实现）**

GraphGPT 论文（ICML2025）的 PyTorch 官方实现：将图经欧拉路径可逆地转换为节点/边/属性 token 序列，用标准 Transformer 编码/解码器架构，以 NTP 或 SMTP 两种自监督任务预训练，再在图级/边级/节点级下游任务上微调，应用于分子性质预测、蛋白质相互作用等 OGB 数据集。报告可扩展至 20 亿参数，并在 README 中讨论了缩放上限、图数据质量与 few-shot 等未解决问题。通过 git clone 源码安装，依赖 conda 环境、PyTorch 与 CUDA，在 V100/A800 GPU 上测试，提供预训练/微调 shell 脚本与 ModelScope 检查点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 欧拉路径实现图到序列的可逆转换（short/long/prolonged 三种属性附着方式）
- NTP 与 SMTP（源自 MaskGIT）两种自监督预训练任务
- 图级/边级/节点级任务的预训练与微调管线，含统一 TrainingPipeline 重构
- 提供 PCQM4M-v2 预训练与微调检查点（ModelScope）

## 适用场景

- 在 OGB 分子/蛋白质图数据集上做预训练与下游任务微调
- 复现论文中的图级/边级/节点级实验结果
- 研究扩散式 LLM 目标与图模态的结合（SMTP 与 dLLM 的关联）

## 场景标签

`科研工具` `模型训练` `微调` · 领域:学习与行业

## 证据(README 行号)

> L135: We introduce GraphGPT, a novel self-supervised generative pre-trained model for graph learning based on the Graph 
> L140: The pre-trained model is then fine-tuned for downstream tasks such as graph-, edge-, and node-level prediction.

## 星数曲线

```mermaid
xychart-beta
    title "alibaba/graph-gpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-31 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `834f340bc396` · [字段定义](../../DATASET.md)*
