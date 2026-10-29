# apple-aiml-research/ml-space-benchmark

⭐ 29 · Python · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/apple-aiml-research/ml-space-benchmark) · [官网](https://machinelearning.apple.com/research/cognition-emerge-frontier-models) · 组织维护

**评测前沿模型空间认知能力的 SPACE 基准：代码与数据集**

ICLR 2025 论文 "Does Spatial Cognition Emerge in Frontier Models?" 的配套基准与数据集，系统评测大语言模型与多模态模型的空间认知能力，覆盖大规模导航（基于 habitat-sim）、物体形状布局推理、空间注意与记忆（QA、CSWM、迷宫补全等任务），多数任务提供文本与图像两种呈现方式。支持 GPT、Claude、Llama、Mixtral 等模型的评测命令，需配置 OpenAI/Anthropic API key 并通过 mamba 环境安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个 QA 任务覆盖文本与图像双通道评测
- 导航任务基于 habitat-sim 构建（路线重走/捷径发现）
- 多模态与纯文本两套模型支持列表
- 数据集经 Apple CDN 发布，代码与数据分许可

## 适用场景

- 评测自有的 LLM/VLM 的空间认知能力
- 复现论文中的基准实验结果
- 研究空间认知任务上模型与动物认知的对照

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: We present SPACE, a benchmark that systematically evaluates spatial cognition in frontier models. Our benchmark buil
> L47: ### SPACE QA tasks

## 星数曲线

```mermaid
xychart-beta
    title "apple-aiml-research/ml-space-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `05c5e05cb5a9` · [字段定义](../../DATASET.md)*
