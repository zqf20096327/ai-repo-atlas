# mts-ai/OpenAutoNLU

⭐ 58 · Python · NOASSERTION · 推送 2026-06-19 · [GitHub](https://github.com/mts-ai/OpenAutoNLU) · [官网](https://openautonlu.dev) · 组织维护 · 中文 README

**面向从业者与科研的 NLU 模型自动训练流水线**

由 MWS AI 维护的 Python 流水线，面向文本多分类与 NER 训练：用户提供训练数据后，按数据规模自动选择训练方法（2-5 样本用 AncSetFit，6-80 用 SetFit，更大用微调）。内置数据质量诊断（cartography/不确定性/重标注等）、多种 OOD 检测方法、可选 LLM 数据增强与合成测试生成、ONNX 导出，并附 Streamlit 应用与 CPU/GPU Docker 镜像。已验证英/俄/法/中/阿拉伯/印地语，非默认语言须手动指定 HuggingFace 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按数据规模自动选择 AncSetFit/SetFit/微调训练方法
- 多种数据质量诊断与 5 种 OOD 检测方法
- 可选 LLM 数据增强与合成测试集生成
- ONNX 导出与 Streamlit 应用、CPU/GPU Docker 镜像

## 适用场景

- 小样本场景下训练意图分类或 NER 模型
- 训练前诊断训练数据质量并检测分布外输入
- 无测试集时用 LLM 生成合成测试数据

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: OpenAutoNLU is an open-source pipeline for training natural language understanding (NLU) models for **text classific
> L9: You provide train (and optionally test) data; high-level pipelines (`TextClassificationTrainingPipeline`, `TokenClas

## 星数曲线

```mermaid
xychart-beta
    title "mts-ai/OpenAutoNLU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-29 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e00e361ab65e` · [字段定义](../../DATASET.md)*
