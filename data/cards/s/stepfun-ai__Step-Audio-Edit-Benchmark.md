# stepfun-ai/Step-Audio-Edit-Benchmark

⭐ 21 · Python · 推送 2025-11-22 · [GitHub](https://github.com/stepfun-ai/Step-Audio-Edit-Benchmark) · 组织维护 · 中文 README

**可控语音编辑的评测基准：数据集+Gemini 自动评分**

Step-Audio-EditX 技术报告配套的评测基准仓库：提供 8 位中英双语说话人（男女均衡）的提示音频、覆盖情感（2,000 条文本）、说话风格（2,800 条）与副语言现象（4,000 条）的转写数据，另含论文使用的长音频克隆评测样本。评测以 Gemini-2.5-Pro 为核心模型：情感与风格任务用固定类别的强制选择分类并计算准确率，副语言任务按 1-3 分打分。提供推理与指标计算脚本，需 Gemini API key。代码采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中英双语 8 说话人提示音频，来源 WenetSpeech4TTS / Libri-Light / GLOBE_V2
- 情感/风格/副语言三类转写数据（2,000/2,800/4,000 条文本）
- Gemini-2.5-Pro 评测：分类准确率与 1-3 分评分
- 提供 gemini_infer.py 等评测与指标计算脚本

## 适用场景

- 评测语音编辑/合成模型在情感与风格控制上的表现
- 对比闭源模型的语音克隆能力
- 为语音编辑研究提供标准化评测数据与流程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: We introduce **step-audio-edit-benchmark**, a comprehensive evaluation framework covering emotion, speaking style, a
> L82: We utilize Gemini-2.5-Pro as the core model for all our evaluation tasks. The assessment protocol and metrics vary 

## 星数曲线

```mermaid
xychart-beta
    title "stepfun-ai/Step-Audio-Edit-Benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b9f2e456e268` · [字段定义](../../DATASET.md)*
