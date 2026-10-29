# Trustworthy-ML-Lab/ThinkEdit

⭐ 21 · Python · 推送 2026-08-24 · [GitHub](https://github.com/Trustworthy-ML-Lab/ThinkEdit) · [官网](https://lilywenglab.github.io/ThinkEdit/) · 组织维护

**面向科研者的 LLM 权重编辑方法：缓解推理模型的过短思考**

EMNLP 2025 论文 ThinkEdit 的官方代码库。提供两套流程：一是从 GSM8K 响应中提取逐层推理长度方向（Self-Attn/MLP）并对模型做转向实验；二是定位对短推理方向贡献大的注意力头（4%），对其 o_proj 层做权重编辑，生成 ThinkEdit 模型并评估准确率。覆盖 DeepSeek-Qwen-1.5B/14B/32B 与 DeepSeek-Llama3-8B 四个模型，编辑后模型发布于 Hugging Face，评估用 vllm 加速。流程分步脚本运行，需指定 GPU 与张量并行参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Self-Attn/MLP 提取推理长度方向并做转向实验
- 按注意力头贡献定位短推理头并对 o_proj 做权重编辑
- 提供 4 个尺寸的 ThinkEdit 模型（Hugging Face 可下载）
- 支持 GSM8K/MMLU Elem./MATH 系列数据集评估，评估用 vllm 加速

## 适用场景

- 复现论文中的权重编辑与评估实验
- 对推理模型做过短思考问题的机制研究
- 获取已编辑的 ThinkEdit 模型并评测效果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This is the official repository for the paper: **ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Th
> L81: ## ThinkEdit models: Weight editing short reasoning heads

## 星数曲线

```mermaid
xychart-beta
    title "Trustworthy-ML-Lab/ThinkEdit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `21190b1fe649` · [字段定义](../../DATASET.md)*
