# inseq-team/inseq

⭐ 477 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/inseq-team/inseq) · [官网](https://inseq.org) · 组织维护

**面向研究者的序列生成模型事后可解释性分析工具包**

基于 PyTorch 的 Python 工具包，对 Hugging Face Transformers 的编码器-解码器与解码器-only 模型做事后特征归因分析：支持梯度类、内部信息类、扰动类共十余种归因方法（扩展 Captum），并提供 logits/概率/熵/困惑度等步骤函数提取与对比归因。可视化覆盖 Jupyter、浏览器与命令行；附带 CLI 支持单例与整个 🤗 数据集的批量归因。要求 Python 3.10–3.13，经 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 🤗 Transformers 的 ForConditionalGeneration 与 ForCausalLM 模型归因
- 十余种归因方法（saliency、integrated_gradients、lime、value_zeroing 等），扩展 Captum
- 归因图的后处理、过滤与合并（Aggregator 类）及多端可视化
- CLI 支持 inseq attribute / attribute-dataset / attribute-context 批量归因

## 适用场景

- 对翻译或生成模型做 token 级特征归因分析
- 用对比归因研究模型对上下文的依赖
- 在命令行对整个 Hugging Face 数据集批量归因并保存结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L17: Inseq is a Pytorch-based hackable toolkit to democratize access to common post-hoc **in**terpretability analyses of
> L80: - 🚀 Feature attribution of sequence generation for most `ForConditionalGeneration` (encoder-decoder) and `ForCausal

## 星数曲线

```mermaid
xychart-beta
    title "inseq-team/inseq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 476 --> 478
    line [477, 477]
```

2026-10-18 477 → 2026-10-24 477（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2410c8e47e28` · [字段定义](../../DATASET.md)*
