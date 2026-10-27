# domschl/HuggingFaceGuidedTourForMac

⭐ 205 · Jupyter Notebook · MIT · 推送 2025-12-23 · [GitHub](https://github.com/domschl/HuggingFaceGuidedTourForMac) · 个人维护

**Apple Silicon Mac 上运行 HuggingFace LLM 的安装与实验教程**

面向 Apple Silicon Mac 用户的实操教程仓库：通过 homebrew 安装 python/uv/git，用 uv 管理虚拟环境，分步安装带 MPS（Metal）加速的 PyTorch，并可选安装 Apple MLX、JAX（jax-metal，锁定 0.4.34 旧版本）、TensorFlow 与 Jupyter Lab，最终用 transformers 加载预训练语言模型做简单聊天机器人实验。附框架对比说明（PyTorch/JAX/MLX/TensorFlow/corenet）与矩阵乘法基准 notebook。仓库本身为教程与 notebook 集合，非软件产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分步安装 MPS 加速 PyTorch 及可选 MLX/JAX/TensorFlow
- Version 4 改用 uv 包管理器，旧版 pip/venv 流程仍保留
- 含框架对比说明与 02-Benchmarks 性能对比 notebook
- 以 transformers 加载预训练 LLM 做简单 chatbot

## 适用场景

- 在 Mac 上从零搭建本地深度学习实验环境
- 比较 PyTorch/JAX/MLX 框架并选择适合自己的
- 运行 HuggingFace 预训练语言模型的入门实验

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: # HuggingFace and Deep Learning guided tour for Macs with Apple Silicon
> L5: A guided tour on how to install optimized `pytorch` and optionally Apple's new `MLX` and Google's `JAX` on Apple Sil
> L9: We will perform the following steps:

## 星数曲线

```mermaid
xychart-beta
    title "domschl/HuggingFaceGuidedTourForMac 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-27 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `604d5b5646ee` · [字段定义](../../DATASET.md)*
