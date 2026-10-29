# Marker-Inc-Korea/KO-VLM-Benchmark

⭐ 32 · Python · 推送 2026-07-28 · [GitHub](https://github.com/Marker-Inc-Korea/KO-VLM-Benchmark) · 组织维护

**韩语文档 VLM 评测基准数据集（3 套，KO-VQA/VDC/OCRAG）**

由 Marker Inc. Korea 制作的韩语视觉语言模型评测基准，含三个子数据集：KO-VQA 评估韩语文档理解与文档问答推理（15 个领域），KO-VDC 评估表格/图表/图形理解与说明文生成（含 Long-Context 问答），KO-OCRAG 评估复杂结构文档 OCR 与视觉信息描述生成（面向 RAG parsing）。数据取自 AI-Hub 与韩国公共数据门户的真实文档。README 附 Gemini、Qwen-VL、Ovis、Gemma 等模型在单卡 A100 40/80GB 上的评测结果。受韩国 KIAT/MOTIE 资助。

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

- 三个子基准分别覆盖文档 VQA、图表说明生成、OCR/视觉描述
- 基于 AI-Hub 与公共数据门户的真实韩语文档构建
- 给出 17 个闭源/开源 VLM 的评测结果表（含 WER/CER/sBERT/ROUGE 组合指标）

## 适用场景

- 评测 VLM 对韩语文档与图表的理解能力
- 为韩语场景挑选合适的开源视觉语言模型
- 检验模型生成 RAG 解析用文档描述的能力

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L9: 저희는 AI-Hub에서 제공하는 2가지 데이터셋과 공동데이터포털에서 제공하는 여러가지 문서들을 수집 및 활용하여 **🔱KO-VLM Benchmark dataset🔱** 제작하였습니다.
> L12: **KO-VLM Benchamrk dataset🔱**은 총 3가지 데이터셋으로 구성되어 있습니다.
> L14: - KO-VQA🔱: `다양한 도메인의 한국어 문서 이해 능력` 및 `문서 기반의 답변 추론 능력`에 대해 평가

## 星数曲线

```mermaid
xychart-beta
    title "Marker-Inc-Korea/KO-VLM-Benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81946f7abd1f` · [字段定义](../../DATASET.md)*
