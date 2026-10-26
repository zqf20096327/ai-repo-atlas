# gauravvij/AutoPrompter

⭐ 58 · Python · 推送 2026-04-16 · [GitHub](https://github.com/gauravvij/AutoPrompter) · [官网](https://heyneo.com) · 个人维护

**闭环自动优化 LLM 提示词的系统，含 Web 仪表盘**

由优化器 LLM 与目标 LLM 组成的迭代提示词优化系统：优化器按任务描述生成合成数据集，目标模型在当前提示词下测试，按 Accuracy/F1/语义相似度等指标评估，优化器分析成败生成改进提示词，循环迭代直至收敛。所有实验记入 JSON 账本以避免重复并提供上下文管理。支持 OpenRouter、Ollama、llama.cpp 三种后端（含自动探测），提供 CLI 与 Flask Web 仪表盘（实时进度、配置构建、检查点、提示词差异对比）。默认模型为 Gemini Flash（优化器）与 Qwen 3.5 9b（目标）。

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

- 优化器 LLM 生成合成数据集并迭代改进目标 LLM 的提示词
- 实验账本记录全部迭代，语义去重与统计显著性检验防止噪声驱动切换
- 支持 OpenRouter/Ollama/llama.cpp 后端，backend: auto 自动探测
- Flask Web 仪表盘：实时图表、检查点管理、提示词 diff 可视化

## 适用场景

- 自动迭代改进我写好的任务提示词并跟踪每次得分
- 本地 Ollama/llama.cpp 环境下无 API key 运行提示词优化
- 用对抗输入鲁棒性测试验证提示词的稳定性

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: AutoPrompter is an autonomous system designed to iteratively improve LLM prompts through a closed-loop optimization 
> L11: The system operates in a continuous loop where an **Optimizer LLM** refines prompts for a **Target LLM** based on e
> L62: ### Supported Backends

## 星数曲线

```mermaid
xychart-beta
    title "gauravvij/AutoPrompter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c98cc657c486` · [字段定义](../../DATASET.md)*
