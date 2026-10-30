# OceanGPT/OceanGPT

⭐ 116 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/OceanGPT/OceanGPT) · [官网](http://OceanGPT.org/) · 组织维护 · 中文 README

**面向海洋科学的领域大模型系列（沧渊），支持问答、图像解读与代码生成**

浙大 ZJUNLP 团队维护的海洋领域基础模型项目（ACL 2024 论文），基于 Qwen/MiniCPM/LLaMA 训练多个开源模型：OceanGPT-basic（海洋专业问答）、OceanGPT-o（声呐与海洋科学图像多模态解读）、OceanGPT-coder（水下机器人 MOOS 代码生成），规模 0.6B–30B。提供 transformers 推理示例、vLLM/sglang/ollama/llama.cpp 部署路径、本地 Gradio WebUI、MCP 声呐图像服务，以及基于 Llama Factory 的定制问答微调教程。限制：可能幻觉、仅支持部分图像类型与 MOOS 代码生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多尺寸模型系列：basic 问答 / o 多模态图像解读 / coder MOOS 代码生成
- 提供 HuggingFace 与 ModelScope 双渠道权重与 OceanInstruct 指令数据
- 支持 transformers、vLLM、sglang、ollama、llama.cpp 多种推理方式
- MCP Server 支持声呐图像解读，附微调构建领域问答系统的教程

## 适用场景

- 我需要做海洋科学领域的专业问答
- 我想用多模态模型解读海洋声呐或科学图像
- 我要生成水下机器人 MOOS 框架代码
- 我想基于领域模型微调自己的海洋问答系统

## 场景标签

`代码生成` `多模态` `教程课程` · 领域:编码与开发

## 证据(README 行号)

> L73: This is the OceanGPT (沧渊) project, which aims to build ocean foundation model.
> L171: You can use OceanGPT-o for marine science image interpretation.
> L187: You can use OceanGPT-coder for moos code generation.

## 星数曲线

```mermaid
xychart-beta
    title "OceanGPT/OceanGPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-30 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `51ad1cfe12aa` · [字段定义](../../DATASET.md)*
