# huggingface/optimum-furiosa

⭐ 27 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/huggingface/optimum-furiosa) · 组织维护

**在 FuriosaAI NPU 上加速运行 Hugging Face 模型推理的库**

Hugging Face Optimum 的硬件后端扩展：将 Transformers 模型加载到 FuriosaAI NPU 芯片上运行推理，用户把 AutoModelForXxx 替换为对应的 FuriosaAIModelForXxx 类即可。使用前需启用 Furiosa SDK 环境（按 Furiosa 官方安装指南配置）。项目处于快速迭代阶段，README 建议从源码安装，开发者模式需同时克隆并可编辑安装 optimum 与 optimum-furiosa 两个仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 以 FuriosaAIModelForXxx 类替换 AutoModelForXxx 即可在 NPU 上推理
- 需预先配置 Furiosa SDK 环境
- 提供源码安装与开发者可编辑安装方式

## 适用场景

- 在 FuriosaAI NPU 硬件上运行 Transformers 模型推理
- 开发者在 optimum/optimum-furiosa 源码上做二次开发与调试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4: Accelerated inference of 🤗 models using FuriosaAI NPU chips.
> L28: To load a model and run inference with Furiosa NPU, you can just replace your `AutoModelForXxx` class with the corr

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/optimum-furiosa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d67564194499` · [字段定义](../../DATASET.md)*
