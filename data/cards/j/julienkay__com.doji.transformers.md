# julienkay/com.doji.transformers

⭐ 25 · C# · MIT · 推送 2026-04-04 · [GitHub](https://github.com/julienkay/com.doji.transformers) · 个人维护

**Unity 包：在 Unity Sentis 上运行预训练 transformer 模型**

基于 Unity Sentis 的 C# 包，功能定位为 Hugging Face transformers 库的 C# 移植，提供 CLIPTokenizer、LLamaTokenizer、GPT2Tokenizer 等分词器实现，并支持在 Unity 中运行 Phi-3 等小型 LLM（标注为 WIP）。当前两大用途：供 com.doji.diffusers 包运行 Stable Diffusion 模型（提示词分词），以及直接运行小 LLM。通过 OpenUPM scoped registry 安装，API 设计对齐 Hugging Face transformers 的使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 CLIPTokenizer / LLamaTokenizer / GPT2Tokenizer，T5Tokenizer 在路线图中
- 支持在 Unity 中运行 Phi-3 等小型 LLM（WIP）
- API 设计对齐 Hugging Face transformers（AutoTokenizer.FromPretrained 风格）
- 作为 com.doji.diffusers 运行 Stable Diffusion 的依赖组件

## 适用场景

- 在 Unity 项目中本地运行小型 LLM 生成文本
- 为 Unity 中的 Stable Diffusion 管线提供分词器
- 在 Unity 内复用 Hugging Face 风格的模型加载 API

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: A Unity package to run pretrained transformer models with Unity Sentis
> L12: This is essentially a C# port of Hugging Face’s [transformers] library.

## 星数曲线

```mermaid
xychart-beta
    title "julienkay/com.doji.transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c169dd99c1d3` · [字段定义](../../DATASET.md)*
