# Open-Galapagos/evolution-fine-tuning

⭐ 30 · Python · 推送 2026-06-30 · [GitHub](https://github.com/Open-Galapagos/evolution-fine-tuning) · [官网](https://open-galapagos.github.io/evolution_finetuning/) · 组织维护

**论文代码与数据集：用进化搜索轨迹微调小模型学会发现**

NeurIPS 2026 论文『Evolution Fine-Tuning (EFT)』的官方代码、数据集与模型。做法是把进化搜索轨迹转化为监督信号，对 2B–9B 开源 LLM 做 mid-training 微调，得到 Finch 模型家族，作为进化搜索中的变异算子使用。提供 Finch Collection 数据集（371 个优化任务、约 15.7 万条轨迹，后扩至 442 任务/21.8 万轨迹），配套 SkyDiscover 框架安装、LLaMA-Factory 训练配置与评测脚本。数据集 CC-BY 4.0 限非商业学术研究，代码与模型权重 Apache 2.0。

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

- Finch Collection：371 个优化任务、156,731 条过滤后的进化轨迹（后续扩至 442 任务/217,780 条）
- Finch 模型家族（2B–9B，含 KTO 变体）托管于 Hugging Face
- 教师轨迹来自 Qwen3.5-397B-A17B，另提供 GPT-5.4 与 Gemini-3-Flash 教师轨迹
- Finch 可作为变异算子嵌入用户自有进化搜索框架

## 适用场景

- 复现论文的进化微调训练与评测流程
- 在自有进化搜索框架中用 Finch 作为变异算子
- 获取跨 10 个领域的优化任务轨迹数据集用于研究

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  A mid-training "practice phase" that teaches small open-source LLMs how to evolve solutions .
> L91: We build the **Finch Collection** — 156K trajectories across 10 domains and 371 optimization tasks — and fine-tune 

## 星数曲线

```mermaid
xychart-beta
    title "Open-Galapagos/evolution-fine-tuning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5f35176e026e` · [字段定义](../../DATASET.md)*
