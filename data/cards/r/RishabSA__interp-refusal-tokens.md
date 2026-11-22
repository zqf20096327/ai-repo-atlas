# RishabSA/interp-refusal-tokens

⭐ 10 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/RishabSA/interp-refusal-tokens) · [官网](https://rishabsa.github.io/interp-refusal-tokens/) · 组织维护

**LLM 拒绝行为的类别化转向向量研究仓库**

论文配套仓库，研究在经分类拒绝 token 微调的 Refuse-Llama（Llama 3 8B）上，从残差流按类别提取拒绝方向并构建转向向量，推理时由线性探针决定转向符号；另提出白化正交基下的低秩组合干预，可零样本迁移到同架构模型（Llama 3 8B Instruct、DeepSeek R1 Distill Llama）。面向可解释性与 AI 安全研究者，附项目页、arXiv 论文、PDF 海报与模型链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 CoCoNot 五类拒绝分别提取第 18 层类别转向向量
- 线性探针逐 prompt 决定增强或抑制拒绝的转向符号
- 低秩组合干预可零样本迁移到同架构模型
- 在 14 个基准上报告过度拒绝与有害拒绝率数据

## 适用场景

- 研究安全对齐中的过度拒绝问题
- 复现类别化拒绝转向的实验结果
- 在不重训模型的前提下调整拒绝行为

## 场景标签

 · 领域:AI 安全/可解释性研究

## 证据(README 行号)

> L13: **Read the 2026 COLM preprint on arXiv.**
> L21: ## Abstract

## 星数曲线

```mermaid
xychart-beta
    title "RishabSA/interp-refusal-tokens 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `1900251eb8c7` · [字段定义](../../DATASET.md)*
