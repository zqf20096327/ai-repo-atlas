# yagyeshVyas/personalforge

⭐ 95 · Python · 推送 2026-03-21 · [GitHub](https://github.com/yagyeshVyas/personalforge) · 个人维护

**无代码离线微调工具：把个人文档训练进 LLM 并导出 GGUF**

面向无编程经验用户的本地 Web 应用（Flask，浏览器访问 localhost:5000）：从文件上传、HuggingFace 数据集流式加载、网页抓取等 6 类来源收集数据，经 17 项清洗技术处理，按模型规模自动配置 LoRA 参数（rsLoRA、NEFTune、4-bit 量化等），生成可在免费 Colab T4 上运行的训练 notebook，最终导出 GGUF 供 LM Studio / Ollama 离线使用，并内置 BGE-M3 + ChromaDB 的 RAG。58 个模型预配置，支持粘贴任意 HuggingFace 模型 ID。限制：需 20 万+样本才有较好效果，免费 T4 单次约处理 10 万对，7B 模型需 14GB VRAM（4-bit 可缓解）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 项数据清洗技术（PII 移除、MinHash 近似去重、质量门控等）
- 按模型规模自动生成 LoRA 配置与训练 notebook，免费 Colab T4 上运行
- 导出 GGUF，可在 LM Studio / Ollama 离线推理
- 内置 BGE-M3 嵌入 + ChromaDB 的 RAG 管道

## 适用场景

- 把个人文档、代码或网页资料微调进一个专属小模型
- 不写代码、零成本在 Colab 上完成 LoRA 微调
- 导出 GGUF 后完全离线地与自有知识对话

## 场景标签

`微调` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L11: **Upload files → Stream datasets → Clean data → Pick any model → Train on free Colab → Download GGUF → Chat offline
> L115: ## Fine-Tuning Pipeline
> L232: |Unsloth|2x faster training, 60% less VRAM|

## 星数曲线

```mermaid
xychart-beta
    title "yagyeshVyas/personalforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-30 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `99464c1b4f9b` · [字段定义](../../DATASET.md)*
