# krnel-ai/krnel-graph

⭐ 23 · Python · Apache-2.0 · 推送 2026-05-27 · [GitHub](https://github.com/krnel-ai/krnel-graph) · [官网](https://krnel.ai) · 组织维护

**面向机制可解释性研究的 Python 计算图工具箱**

基于强类型轻量计算图规范的机制可解释性研究工具箱：可通过 HuggingFace Transformers、TransformerLens、Ollama 等运行语言模型并保存残差流激活，从缓存激活训练线性探针并评估，获取护栏模型的 logit 分数，另含数据集加载、UMAP 高维嵌入可视化与全量缓存与溯源追踪。支持 macOS(arm64/MPS)、Linux/Windows(amd64/CUDA) 平台，可在 notebook、CLI 或任务编排框架中运行。以 Python 包形式从 PyPI 安装，附可选 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 HuggingFace Transformers / TransformerLens / Ollama 运行语言模型并保存残差流激活
- 从缓存激活训练线性探针并评估结果
- 全量缓存与结果溯源追踪
- 内置 UMAP 高维嵌入散点图可视化

## 适用场景

- 训练线性探针构建基于模型内部的护栏
- 按语义相似度分组探索大规模数据集
- 在 notebook 或 GPU 机器上管理可解释性实验并缓存结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: A **Python toolbox for mechanistic interpretability research** built on a **lightweight strongly-typed computation g
> L11: - **Run language models** using HuggingFace Transformers, TransformerLens, Ollama, *etc.,* and save activations fro

## 星数曲线

```mermaid
xychart-beta
    title "krnel-ai/krnel-graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d711cc62321a` · [字段定义](../../DATASET.md)*
