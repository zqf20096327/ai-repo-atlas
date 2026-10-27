# lt-asset/selp

⭐ 24 · Python · BSD-3-Clause · 推送 2026-05-17 · [GitHub](https://github.com/lt-asset/selp) · 组织维护

**ICRA 2025 论文 SELP：LLM 生成安全高效机器人任务规划**

论文配套代码库（ICRA 2025，Best Paper Award Finalist）。SELP 用大语言模型从自然语言生成 LTL 公式与机器人任务规划：流水线包含解释、改写、局部 LTL 翻译、等价性投票、基于自动机的约束解码计划生成与最终计划评估。使用 OpenAI API key 运行完整流水线，也提供独立工具直接做 NL-to-LTL 推理（CodeLlama/Llama-2 tokenizer）与语义等价投票。依赖 conda 安装的 spot 库做 LTL 语义等价与自动机校验；微调模型权重尚未发布（coming soon）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言到 LTL 翻译与语义等价投票
- 基于自动机与 trie 解码的在线约束解码生成计划
- 流水线可分阶段停止（--stop-after）
- 提供 NL-to-LTL 推理、投票、约束生成等独立脚本

## 适用场景

- 复现 ICRA 2025 SELP 论文实验
- 研究生成安全且高效机器人任务规划的方法
- 对自然语言任务做 NL-to-LTL 推理与等价性验证

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository provides artifacts for the paper ["SELP: Generating Safe and Efficient Task Plans for Robot Agents w
> L51: The full SELP pipeline runs explanation, paraphrase, local LTL translation,
> L82: The plan-generation stage follows the online constrained-decoding design: it builds the automaton from the combined

## 星数曲线

```mermaid
xychart-beta
    title "lt-asset/selp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `44ba130591a0` · [字段定义](../../DATASET.md)*
