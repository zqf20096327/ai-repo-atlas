# huawei-csl/AC-LoRA

⭐ 21 · Jupyter Notebook · CC0-1.0 · 推送 2025-11-14 · [GitHub](https://github.com/huawei-csl/AC-LoRA) · [官网](https://arxiv.org/abs/2505.11557) · 组织维护

**免训练的 LLM 访问控制方法：按权限检索并合并敏感 LoRA**

NeurIPS 2025 论文的官方代码库。AC-LoRA 将敏感数据分散到互不重叠的多个 LoRA 中微调，基座模型只用公开数据训练；推理时依据用户查询与权限，用余弦相似度从被允许的 LoRA 中检索并合并输出，避免单一模型记忆导致的泄露，当最相关 LoRA 因权限不可得时向用户给出提示。支持多模态（含 stable diffusion 图像生成实验），实验环境为两块 48GB VRAM GPU，通过 conda 环境与 Python 脚本复现论文结果，RepLiQA 评测使用 ollama 作为评分 judge 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 敏感数据分散到不重叠 LoRA，按权限检索合并，无需重新训练或路由门控
- 基于用户查询与各 LoRA 微调数据嵌入的余弦相似度合并输出
- 支持多模态，覆盖文本与 stable diffusion 图像生成实验
- 提供 RepLiQA / FlanV2 / WikiArts 实验脚本与 LoRA 微调代码

## 适用场景

- 企业内多权限域 LLM 部署时防止敏感信息泄露
- 复现论文中的检索与推理实验结果
- 用自己的 LoRA 集合实现按权限的问答

## 场景标签

`网络安全` `微调` · 领域:学习与行业

## 证据(README 行号)

> L19: **AC-LoRA** (Access Control-Low Rank Adaptation) is a **novel, secure and training-free** method to enforce strong 
> L50: Separate LoRAs are fine-tuned with non-overlapping sensitive data.
> L61: We ran our experiments on two GPUs with 48GB VRAM each. A different setup might require some changes.

## 星数曲线

```mermaid
xychart-beta
    title "huawei-csl/AC-LoRA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4436bfe833ab` · [字段定义](../../DATASET.md)*
