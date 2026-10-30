# zer0int/CLIP-fine-tune

⭐ 274 · Python · 推送 2026-06-09 · [GitHub](https://github.com/zer0int/CLIP-fine-tune) · 个人维护

**CLIP 模型微调工具套件：训练、评测与几何诊断**

面向开发者的 CLIP 微调代码库：以 all_in_one_clip_fine_tune.py 为主脚本，支持从 .safetensors、OpenAI pickle 或 HuggingFace Hub 加载 CLIP（含 Long-CLIP 248 tokens），通过数据集启发式自动识别 sidecar/txt/csv/tsv/json/mat/parquet 等标签格式，可免配置运行。包含作者提出的 Regression-CLIP（含 Teachers）与 KO-CLIP 方法、typographic 攻击与零样本评测基准、嵌入几何分析（秩、各向异性等）及单编码器坍塌修复工具。训练速度优化包括预分词、持久 worker 与 EMA 支持；示例环境为 Windows + RTX 4090。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 .safetensors / OpenAI pickle / HF Hub 加载，含 Long-CLIP 248 tokens
- 数据集启发式自动识别多种标签格式，提供免配置 auto 模式
- 含 Regression-CLIP、KO-CLIP 方法及 typographic 攻击评测基准
- 提供嵌入几何分析与单编码器坍塌修复工具

## 适用场景

- 微调 CLIP 文本/视觉编码器以缓解图文误分类（typographic attack）
- 在带文字标签的商品图、漫画等数据上训练 CLIP
- 对 CLIP 嵌入做几何诊断与零样本/检索评测

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: The config .json are in `utils_xconfigs_examples` --- Training code: `all_in_one_clip_fine_tune.py` --- To reproduce
> L19: - All-in-one complete fine-tuning suite
> L36: - Supports HuggingFace models and Long-CLIP 248 tokens

## 星数曲线

```mermaid
xychart-beta
    title "zer0int/CLIP-fine-tune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 273 --> 275
    line [274, 274]
```

2026-10-18 274 → 2026-10-30 274（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dc9163ddc8fd` · [字段定义](../../DATASET.md)*
