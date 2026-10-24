# csinva/imodelsX

⭐ 177 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/csinva/imodelsX) · [官网](https://csinva.io/imodelsX/) · 个人维护

**面向文本数据的可解释建模与转向库（sklearn 兼容）**

imodelsx 是一个 Python 库，提供用 LLM 对文本数据/模型进行解释、预测与转向（steering）的方法集合：Tree-Prompt、iPrompt、AutoPrompt、D3、SASC 生成自然语言解释或可引导的 prompt；Aug-Linear/Aug-Tree 用 LLM 在训练期增强特征以拟合线性模型与决策树（推理期快速且透明）；QAEmb 生成可解释嵌入。所有方法通过统一的 get_llm 接口调用本地 HuggingFace 模型或 OpenAI/Anthropic/Azure/Claude Code/Codex API。附带数据集包装器、LLM 调用包装器（带缓存）与 ngram 线性基线。pip 安装即可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tree-Prompt/iPrompt/SASC 等方法生成自然语言解释与转向 prompt
- Aug-Linear/Aug-Tree：训练期用 LLM 增强特征，推理期透明且快速
- 统一 get_llm 接口支持本地 HuggingFace 模型与多家 API 提供商，输出带缓存
- 附带 HuggingFace 数据集加载、LLM 包装器与 sklearn 风格基线

## 适用场景

- 为文本数据集自动生成自然语言模式的解释
- 训练推理期透明、可解释的线性/树模型
- 解释黑盒文本模块（如分析某层对什么概念敏感）

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Scikit-learn friendly library to explain, predict, and steer text models/data. Also a bunch of utilities for gettin
> L11: |Tree-Prompt|🗂️, 🔗, 📄, 📖,|Explanation + Steering|Generates a tree of prompts to steer an LLM (*Official*)|
> L63: Methods that need next-token probabilities or embeddings (e.g. Tree-Prompt, Aug-Linear, linear finetuning) require 

## 星数曲线

```mermaid
xychart-beta
    title "csinva/imodelsX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 176 --> 178
    line [177, 177]
```

2026-10-18 177 → 2026-10-24 177（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8ea0a95b9d1f` · [字段定义](../../DATASET.md)*
