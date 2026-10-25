# codewithdark-git/Building-LLMs-from-scratch

⭐ 135 · Jupyter Notebook · MIT · 推送 2025-10-29 · [GitHub](https://github.com/codewithdark-git/Building-LLMs-from-scratch) · [官网](https://gist.github.com/codewithdark-git/e204e6c06546f652e76ced9d479d9) · 个人维护

**30 天用 PyTorch 从零构建 GPT 风格 LLM 的教学仓库**

受 Sebastian Raschka 著作《Build a Large Language Model (From Scratch)》启发的四周学习课程仓库：第一周覆盖分词、嵌入与因果语言建模基础；第二周实现注意力、多头注意力、残差与归一化等 Transformer 组件并搭建 decoder-only 架构；第三周处理 TinyShakespeare 等数据集与训练流程；第四周实现多种采样策略的文本生成，并转换为 Hugging Face Transformers 兼容格式，经 Hub 与 Gradio Space 部署。另列出 FaseehGPT、Urdu-LM 两个配套模型项目。面向想动手理解 LLM 内部实现的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四周课程：分词→Transformer decoder→训练→生成与部署
- 文本生成支持 greedy、top-k、top-p 与 temperature 采样
- 提供转换为 Transformers 兼容格式并部署到 Hugging Face Hub / Gradio Space 的脚本
- 配套 FaseehGPT（阿拉伯语）与 Urdu-LM（乌尔都语 MoE）训练管线

## 适用场景

- 跟随 30 天课程动手实现一个 GPT 风格模型
- 学习 attention、训练循环与文本采样等 LLM 基础组件
- 将自己的小模型转换为 Hugging Face 格式并部署演示

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository guides you through the process of building a GPT-style **Large Language Model (LLM)** from scratch u
> L17: ### 🔹 Week 1: Foundations of Language Models

## 星数曲线

```mermaid
xychart-beta
    title "codewithdark-git/Building-LLMs-from-scratch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-25 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `5b52260bfbee` · [字段定义](../../DATASET.md)*
