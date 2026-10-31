# KickItLikeShika/composimplex

⭐ 16 · Python · 推送 2026-10-01 · [GitHub](https://github.com/KickItLikeShika/composimplex) · [官网](https://arxiv.org/abs/2609.34992) · 个人维护

**可组合 LLM 解码库：用正则器组合构造解码策略并评测**

论文《Composable Decoding on the Probability Simplex》的官方库，将语言模型解码表述为概率单纯形上的优化问题：每步在 logits 上组合多个正则器（KL、JS 散度、熵、覆盖度、多样性）求解下一 token 分布。贪心、温度、Top-k、Top-p 均为其特例，新解码器通过 YAML 配置混合正则器构建。后端支持 Hugging Face Transformers 与 vLLM，内置 MATH500、GPQA Diamond、IFEval、LiveCodeBench v6 基准，一条命令生成并评测。从仓库根目录 pip install -e . 安装。

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

- 解码表述为正则化优化，贪心/温度/Top-k/Top-p 皆为特例
- YAML 配置组合正则器定义新解码器
- Transformers 与 vLLM 两种后端
- 内置 MATH500/GPQA/IFEval/LiveCodeBench 基准与一键评测命令

## 适用场景

- 研究者在论文基准上评测自定义解码策略
- 通过组合正则器构造新解码器做文本生成实验
- 对比不同解码配置在数学与代码任务上的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: CompoSimplex treats language-model decoding as an optimization problem. Instead of applying a fixed sampling rule, 
> L21: - Works with Hugging Face Transformers and vLLM.

## 星数曲线

```mermaid
xychart-beta
    title "KickItLikeShika/composimplex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d524ae9c80b0` · [字段定义](../../DATASET.md)*
