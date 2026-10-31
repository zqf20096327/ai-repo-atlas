# zou-group/metatextgrad

⭐ 16 · Python · MIT · 推送 2025-11-05 · [GitHub](https://github.com/zou-group/metatextgrad) · [官网](https://arxiv.org/abs/2505.18524) · 组织维护

**NeurIPS 2025 论文代码：自动优化 LLM 优化器的元优化器**

研究代码库，对 TextGrad、ADAS 等 LLM 文本优化器做元层面的提示词与结构自动优化，生成面向特定任务分布的优化器，替代手工设计。基于修改版 TextGrad 代码库构建（需从本仓库安装而非官方版），提供 zero-shot/few-shot CoT、self-consistency、best-of-n、TextGrad TGD、ADAS-TG、MIPROv2 等基线复现脚本，支持 MMLU、BBH、GPQA 等任务。元结构优化默认关闭，开启后 API 花费可能达数十美元以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 LLM 优化器做元提示与元结构自动优化
- 附带 TextGrad/ADAS-TG/DSPy MIPROv2 等基线运行脚本
- 支持 MMLU/BBH word_sorting/BBH dyck_languages/GPQA_diamond 任务
- NeurIPS 2025 接收，代码与论文公开发布

## 适用场景

- 复现论文中的元优化实验与各基线对比
- 在 BBH/MMLU/GPQA 任务上研究生成任务对齐的优化器
- 基于修改版 TextGrad 代码库做 LLM 优化研究

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: A meta-optimizer — for optimizing LLM optimizers!
> L9: metaTextGrad automatically optimizes LLM-based optimizers like TextGrad and ADAS through meta prompt and structure o
> L52: Such alignment helps the optimizer produce better programs even when the feedback remains noisy. Therefore, rather 

## 星数曲线

```mermaid
xychart-beta
    title "zou-group/metatextgrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `32b0e3ebfb2b` · [字段定义](../../DATASET.md)*
