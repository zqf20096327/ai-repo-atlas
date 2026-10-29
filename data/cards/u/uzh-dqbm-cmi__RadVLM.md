# uzh-dqbm-cmi/RadVLM

⭐ 20 · Python · NOASSERTION · 推送 2026-08-02 · [GitHub](https://github.com/uzh-dqbm-cmi/RadVLM) · [官网](https://arxiv.org/abs/2502.03333) · 组织维护

**面向放射学的多任务对话式视觉语言模型及其数据与训练评测代码**

苏黎世大学团队发布的放射学 VLM 项目：基于 LLaVA-OneVision 微调，覆盖报告生成、异常分类、解剖与异常定位、短语定位和对话交互五类任务。提供完整流水线：用 Azure OpenAI GPT-4o 过滤报告并生成对话数据，构建 111.5 万对图文指令数据集（MIMIC-CXR、CheXpert、VinDr-CXR、MS-CXR 等），转换 LLaVA 格式后微调，再在标准基准上与 RaDialog、CheXagent、MAIRA-2 等模型对比评测。安装依赖 conda 环境加 pip，训练与推理需 GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 111.5 万对图文指令数据集，覆盖 5 类视觉语言任务
- 基于 LLaVA-OneVision 微调，权重可转换为 HuggingFace 格式
- 用 Azure GPT-4o 过滤报告并生成合成对话数据
- 内置基线模型复现与多任务评测脚本（含 GREEN 指标）

## 适用场景

- 我要构建并微调一个放射学多任务视觉语言模型
- 我想生成放射学报告生成/定位任务的指令数据集
- 我要在 MIMIC-CXR 等基准上对比放射学 VLM 性能

## 场景标签

`多模态` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L14: The instruction dataset comprises 1,115,021 image-instruction pairs spanning multiple vision-language tasks, includ
> L103: In the `finetuning` directory, we forked from the official LLaVA-OneVision repo and adapted for the case of finetu

## 星数曲线

```mermaid
xychart-beta
    title "uzh-dqbm-cmi/RadVLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `17e800d1de98` · [字段定义](../../DATASET.md)*
