# sandseb123/local-lora-cookbook

⭐ 14 · Python · MIT · 推送 2026-03-06 · [GitHub](https://github.com/sandseb123/local-lora-cookbook) · 个人维护

**本地 LoRA 微调教程工程：用自己的应用数据微调 LLM 并在设备上运行**

提供一套在本地微调小规模 LLM 的流水线工程：先通过应用已有 RAG 管线从 SQLite 数据生成问答样本（Ollama 本地推理，免费），再用 Claude 一次性将基线回答改写为标准回答（唯一云端调用，约 $2-5），随后用 LoRA 微调 Qwen3.5-4B 等模型（Apple Silicon 走 mlx-lm，Linux/NVIDIA 走 Unsloth + TRL），最终融合模型在本机长期提供推理服务。内置个人财务教练完整示例，可按 domain.py/rag.py/schema.sql 三文件结构适配自有领域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流水线：RAG 采集→Claude 标注→LoRA 微调→本机部署
- Apple Silicon 用 mlx-lm、Linux/NVIDIA 用 Unsloth + TRL，训练后零云端
- 默认微调 Qwen3.5-4B，可替换任意 HuggingFace 因果语言模型
- 内置 finance_coach 端到端示例，含硬件耗时对照表与低内存模式

## 适用场景

- 我想用自己应用的数据库数据微调一个本地小模型
- 把云端 LLM 调用替换为免费的本机推理服务
- 为自己的领域快速生成训练数据并完成 LoRA 微调

## 场景标签

`教程课程` `微调` · 领域:学习与行业

## 证据(README 行号)

> L51: **Train**: `train_lora.py` fine-tunes Qwen3.5-4B (or any HuggingFace model)
> L54: **Serve**: The fused model is served via mlx-lm (port 8080) on Mac or
> L55: exported to GGUF and registered with Ollama on Linux.

## 星数曲线

```mermaid
xychart-beta
    title "sandseb123/local-lora-cookbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `937c31e60bb9` · [字段定义](../../DATASET.md)*
