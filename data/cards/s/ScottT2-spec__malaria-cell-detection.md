# ScottT2-spec/malaria-cell-detection

⭐ 15 · Python · 推送 2026-05-28 · [GitHub](https://github.com/ScottT2-spec/malaria-cell-detection) · [官网](https://www.kaggle.com/scottantwi) · 个人维护

**疟疾血液涂片 AI 筛查平台：CNN 检测+LLM 临床辅助**

面向疟疾流行地区医疗工作者的临床决策支持工具：3 层 CNN（TensorFlow.js，浏览器内离线运行）对血细胞显微图像分类为感染/未感染，报告 95.43% 准确率（NIH 数据集 27,558 张）。LLM 层（可配置 OpenAI 兼容 API）生成临床摘要、治疗指引与多语言患者教育；TF-IDF 检索的 RAG 管线引入 WHO/CDC 指南，医生纠错实时写入知识库。后端 Python/FastAPI，前端为可离线 PWA。声明仅用于教育与科研，非医疗设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 层 CNN 在浏览器端离线运行，分类感染/未感染血细胞
- RAG 引入 WHO/CDC 指南，医生纠错实时更新知识库
- LLM 生成临床摘要、治疗指引与多语言患者教育
- 提供 /api/analyze、/api/correct、/api/chat 等 REST 接口

## 适用场景

- 显微图像的疟疾筛查辅助判断
- 乡村诊所或社区医疗中生成治疗指引与患者教育材料
- 医生通过纠错接口持续完善知识库

## 场景标签

`目标检测` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: 1. **🔬 CNN Detection** — A 3-layer CNN (95.43% accuracy, trained on 27,558 NIH images) classifies blood cell microsc
> L21:   [CNN Detection] ← TensorFlow.js (runs in-browser, works offline)

## 星数曲线

```mermaid
xychart-beta
    title "ScottT2-spec/malaria-cell-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `89631494ef82` · [字段定义](../../DATASET.md)*
