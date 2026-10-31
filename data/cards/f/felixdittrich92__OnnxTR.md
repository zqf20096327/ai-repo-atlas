# felixdittrich92/OnnxTR

⭐ 198 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/felixdittrich92/OnnxTR) · [官网](https://github.com/mindee/doctr) · 个人维护

**docTR 的 ONNX 推理封装库：无 PyTorch/TF 依赖的文档 OCR**

OnnxTR 是对 docTR 库的封装，将其文本检测、文本识别、版面分析与表格结构识别模型转换为 ONNX 流水线，运行于 ONNX Runtime，不依赖 PyTorch 或 TensorFlow。支持 CPU、CUDA、OpenVINO、CoreML 执行提供者，提供 8-bit 量化模型以加速 CPU 推理。可读取 PDF/图片/网页，输出 JSON/文本/XML/hocr/Markdown 等格式，附带 onnxtr-cli 命令行工具，支持加载自定义 ONNX 模型及 HuggingFace Hub 模型。需 Python 3.11+，通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 docTR 模型的 ONNX 流水线，无 PyTorch/TensorFlow 依赖
- 支持 CPU / CUDA / OpenVINO / CoreML 执行提供者与 8-bit 量化模型
- 覆盖文本检测、识别、版面检测（LW-DETR）与表格结构识别（TableCenterNet）多种架构
- 提供 onnxtr-cli 命令行与 JSON/XML/hocr/Markdown 等多种导出格式

## 适用场景

- 在没有深度学习框架依赖的环境中对 PDF/图片做文档文字识别
- 对文档做版面分析与表格结构识别并导出 Markdown/JSON
- 通过命令行批量运行 OCR 而不写 Python 代码

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L14: **Optical Character Recognition made seamless & accessible to anyone, powered by Onnx**
> L18: - efficient ways to parse textual information (localize and identify each word) from your documents
> L19: - a Onnx pipeline for docTR, a wrapper around the doctr library - no PyTorch or TensorFlow dependencies

## 星数曲线

```mermaid
xychart-beta
    title "felixdittrich92/OnnxTR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 197 --> 199
    line [198, 198]
```

2026-10-18 198 → 2026-10-31 198（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2289b0f871ca` · [字段定义](../../DATASET.md)*
