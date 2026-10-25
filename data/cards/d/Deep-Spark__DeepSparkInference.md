# Deep-Spark/DeepSparkInference

⭐ 36 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Deep-Spark/DeepSparkInference) · [官网](https://gitee.com/deep-spark/deepsparkinference) · 组织维护 · 中文 README

**面向国产 GPU 的推理模型库：300 个模型的推理示例与评测**

DeepSpark 开源社区的推理模型库，2024 年 3 月开源，收录约 300 个小模型与大模型的推理示例和指导文档。模型在天数智芯的推理引擎 IGIE（基于 TVM）或 ixRT 下运行，部分模型附智铠 100 GPU 评测结果；LLM 部分涉及 vLLM、TGI、LMDeploy、TRT-LLM 等框架。覆盖 CV（分类/检测/分割/OCR/姿态/跟踪）、NLP、语音、多模态、推荐系统，按季度更新。需前往天数开发者社区获取配套软件栈与容器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 300 个模型在 IGIE/ixRT 推理引擎下的运行示例与文档
- LLM 覆盖 vLLM、TGI、LMDeploy、TRT-LLM、FastDeploy 等多种引擎
- CV 任务细分至分类、检测、人脸、OCR、姿态、实例/语义分割、多目标跟踪
- 标注各模型所需 IXUCA SDK 版本，部分附国产 GPU 评测结果

## 适用场景

- 在国产通用 GPU 上部署 CV/NLP/语音/LLM 推理任务
- 查找某模型在 IGIE 或 ixRT 下的支持情况与 SDK 版本要求
- 获取不同推理框架（vLLM/TGI/LMDeploy 等）下的大模型运行示例

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12: `DeepSparkInference`推理模型库作为 DeepSpark 开源社区的核心项目，于 2024 年 3 月正式开源，一期甄选了 48 个推理模型示例，涵盖计算机视觉，自然语言处理，语音识别等领域，后续将逐步拓展更多 
> L14: `DeepSparkInference`中的模型提供了在国产推理引擎`IGIE`或`ixRT`下运行的推理示例和指导文档，部分模型提供了基于国产通用 GPU 智铠 100 的评测结果。
> L16: `IGIE`（Iluvatar GPU Inference Engine）是基于 TVM 框架研发的高性能、高通用、全流程的 AI 推理引擎。支持多框架模型导入、量化、图优化、多算子库支持、多后端支持、算子自动调优等特性，为推理场

## 星数曲线

```mermaid
xychart-beta
    title "Deep-Spark/DeepSparkInference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c457b264372b` · [字段定义](../../DATASET.md)*
