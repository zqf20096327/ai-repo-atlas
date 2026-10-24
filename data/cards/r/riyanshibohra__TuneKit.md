# riyanshibohra/TuneKit

⭐ 151 · Python · MIT · 推送 2026-07-18 · [GitHub](https://github.com/riyanshibohra/TuneKit) · [官网](https://tunekit.app/) · 个人维护

**上传数据即生成 Colab 微调笔记本的工具，免费微调 SLM**

基于 FastAPI 的 Web 应用：用户上传 JSONL 对话数据，回答两个问题后生成预配置的 Google Colab 笔记本，点击 Run All 即在免费 T4 GPU 上完成小型语言模型微调（约 15 分钟），产物可导出为 LoRA、GGUF 或合并权重。训练栈为 Unsloth、Transformers、PEFT。支持 Phi-4 Mini、Llama 3.2、Mistral 7B、Qwen 2.5、Gemma 2 五个模型系列；数据需 JSONL 格式且至少 50 条示例。可本地以源码运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传 JSONL → 生成 Colab 笔记本 → 免费 T4 GPU 微调的流程
- 导出格式支持 LoRA、GGUF、合并权重
- 支持 5 个模型系列（Phi-4 Mini/Llama 3.2/Mistral 7B/Qwen 2.5/Gemma 2）
- 训练栈基于 Unsloth + Transformers + PEFT

## 适用场景

- 没有本地 GPU 时低成本微调小型语言模型
- 零代码生成可复现的微调 Colab 笔记本
- 快速试验结构化输出、分类、对话等任务的模型定制

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L31: TuneKit eliminates all of that. Upload your data, answer two questions, and get a ready-to-run Colab notebook. Clic
> L107: - **Training:** Unsloth, Transformers, PEFT

## 星数曲线

```mermaid
xychart-beta
    title "riyanshibohra/TuneKit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 150 --> 152
    line [151, 151]
```

2026-10-18 151 → 2026-10-24 151（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `33885666303a` · [字段定义](../../DATASET.md)*
