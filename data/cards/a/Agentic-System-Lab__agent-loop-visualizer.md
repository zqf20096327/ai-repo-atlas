# Agentic-System-Lab/agent-loop-visualizer

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Agentic-System-Lab/agent-loop-visualizer) · [官网](https://agentic-system-lab.github.io/agent-loop-visualizer/) · 组织维护 · 中文 README

**可视化展示 agent 循环内部机制的教学交互应用**

面向学习者的 Streamlit 交互页面：在聊天界面旁逐步绘制 agent 循环——模型读取上下文、提出动作、harness 执行、结果写回上下文直至停止，并逐 token 展示概率、候选与特殊 token。模型（Gemma 4 E2B / Qwen3.5 0.8B）在本机以 transformers 运行，或通过 vLLM（Docker）运行；循环可用自带 harness 或交给 pi。支持多模态附件、MTP 投机解码与 Docker 沙箱内 run_python 工具。页面结构与 Agent Atlas 课程 Unit 01 阅读对应，提供中英文界面。限制：本地运行需要相应磁盘与内存（Gemma 约 10GB 权重、16GB 以上内存）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐步绘制 agent 循环并逐 token 显示概率、rank 与 top-5 候选
- 模型以 Hugging Face transformers 本地运行或通过 vLLM（Docker）服务运行
- 支持多模态附件（图像/视频/音频）与 MTP 投机解码可视化
- 可选 run_python 工具在 Docker 沙箱执行模型生成的 Python 代码

## 适用场景

- 学习 agent 循环的内部机制，对照课程阅读逐步观察每一步
- 对比不同模型（Gemma 4 / Qwen3.5）的 token 格式与停止条件
- 观察 MTP 投机解码的猜测与保留过程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: This project is for learning: it shows how an agent loop works underneath, in a way more intuitive and visual than r
> L9: - Models: pick google/gemma-4-E2B-it or Qwen/Qwen3.5-0.8B in the sidebar; they run on your machine with Hugging Face

## 星数曲线

```mermaid
xychart-beta
    title "Agentic-System-Lab/agent-loop-visualizer 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32]
```

2026-10-29 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `116a6b04b625` · [字段定义](../../DATASET.md)*
