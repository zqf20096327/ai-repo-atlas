# NVIDIA-BioNeMo/bionemo-recipes

⭐ 875 · Python · 推送 2026-10-23 · [GitHub](https://github.com/NVIDIA-BioNeMo/bionemo-recipes) · [官网](https://nvidia-bionemo.github.io/bionemo-recipes/) · 组织维护

**面向药物发现的生物基础模型训练配方与模型检查点库**

NVIDIA 维护的生物基础模型规模化训练资源库：提供使用 TransformerEngine 层的 HuggingFace 兼容模型检查点（ESM-2、AMPLIFY、Geneformer、Llama 3、Mixtral 风格 MoE、Qwen 等）与自包含 Docker 训练配方，展示 FP8 训练、FSDP/megatron-FSDP、上下文并行、序列打包等特性，支持单 GPU 到多节点扩展，并兼容 HuggingFace Accelerate、PyTorch Lightning 与原生 PyTorch。另含可解释性研究工具与三级测试体系。部分特性需 Hopper/Blackwell 架构 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 TransformerEngine 的 HuggingFace 兼容模型检查点，可用 AutoModel.from_pretrained 直接加载
- 自包含 Docker 训练配方，覆盖 FP8/megatron-FSDP/上下文并行/序列打包
- 支持单 GPU 原型到多节点训练的扩展
- 三级测试体系（L0 预合并/L1 性能/L2 发布验证），基准覆盖 A100 至 B200

## 适用场景

- 生物基础模型开发者将原型扩展到多节点高效训练
- 领域科学家用私有数据微调 ESM-2 等模型用于药物发现
- 研究者参考配方实现 FP8 与 FSDP 训练模式

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L3: BioNeMo Recipes provides an easy path for the biological foundation model training community to scale up transformer
> L79: Self-contained training examples demonstrating best practices for scaling biological foundation models. Each recipe
> L83: - **Scaling strategies**: Single-GPU to multi-node training patterns

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-BioNeMo/bionemo-recipes 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 869 --> 876
    line [870, 871, 874, 875]
```

2026-10-18 870 → 2026-10-24 875（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `80f81745a037` · [字段定义](../../DATASET.md)*
