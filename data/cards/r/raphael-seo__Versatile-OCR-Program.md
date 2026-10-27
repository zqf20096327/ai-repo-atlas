# raphael-seo/Versatile-OCR-Program

⭐ 674 · Python · NOASSERTION · 推送 2026-05-13 · [GitHub](https://github.com/raphael-seo/Versatile-OCR-Program) · 个人维护

**面向 ML 训练数据制作的多模态 OCR 流水线**

从试卷等复杂教育材料中提取结构化数据的 OCR 系统：两阶段流程（ocr_stage1.py 做版面检测与元素抽取，ocr_stage2.py 做语义解释与结构化输出），支持日/韩/英多语言文本、数学公式、表格、图表与插图，为图表等视觉元素自动生成自然语言描述，输出 JSON/Markdown 格式的 AI 训练就绪数据。技术栈使用 DocLayout-YOLO、Google Vision API、MathPix OCR、OpenAI API 等，需配置相应 API 密钥并通过 Docker 运行。v3.0 重构为模块化配置驱动架构，旧版本保留于 legacy/ 但不再维护。README 声称在 EJU 生物与东大数学等数据集上达到 90–95% 以上准确率。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段流水线：DocLayout-YOLO 版面检测 + 语义解释输出
- 为图表/插图自动生成自然语言描述与教育价值标注
- 支持日/韩/英多语言及数学公式、表格、图表解析
- 输出 AI-ready 的 JSON/Markdown 结构化格式

## 适用场景

- 把试卷等教育材料转成带语义标注的 ML 训练数据集
- 批量解析含公式、表格、插图的密集科学 PDF
- 为多语言教育语料生成图像描述与上下文元数据

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L42: This OCR system is specifically designed to extract structured data from complex educational materials—such as exam
> L47: – Optimized for ML Training: Extracted elements such as diagrams, tables, and figures are semantically annotated wi
> L58: – Built With: DocLayout-YOLO, Google Vision API, Gemini Pro Vision, MathPix OCR, OpenAI API, OpenCV, and more.

## 星数曲线

```mermaid
xychart-beta
    title "raphael-seo/Versatile-OCR-Program 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 673 --> 676
    line [675, 674]
```

2026-10-18 675 → 2026-10-27 674（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0b4f0a7beeb6` · [字段定义](../../DATASET.md)*
