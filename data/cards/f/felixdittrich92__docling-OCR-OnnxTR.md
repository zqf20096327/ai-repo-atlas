# felixdittrich92/docling-OCR-OnnxTR

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/felixdittrich92/docling-OCR-OnnxTR) · [官网](https://github.com/felixdittrich92/OnnxTR) · 个人维护

**Docling 的 OnnxTR OCR 插件：文档转换中接入文本识别**

将 OnnxTR OCR 引擎集成为 Docling 框架插件的 Python 包，用于文档处理流程中的文本检测与识别。按硬件选择安装 extras：CPU、Nvidia GPU（需预装 CUDA 与 cuDNN）及 OpenVINO 等配置。通过 OnnxtrOcrOptions 类配置语言列表、置信度阈值、检测/识别模型架构、批大小、8-bit 加载等参数；模型可从 Hugging Face Hub 下载或本地加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OnnxTR OCR 引擎以插件形式集成进 Docling 流程
- 支持 CPU / GPU / OpenVINO 多种硬件部署
- OnnxtrOcrOptions 暴露检测/识别架构、置信度阈值等十余项配置
- 模型可从 Hugging Face Hub 或本地文件加载

## 适用场景

- 在 Docling 文档转换流程中获得 OCR 文本识别能力
- 按硬件（CPU/GPU/OpenVINO）选择推理配置
- 通过本地模型文件离线运行 OCR

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L9: The `docling-OCR-OnnxTR` repository provides a plugin that integrates the OnnxTR OCR engine into the Docling framewo
> L17: - **Flexible Deployment:** Supports various hardware configurations, including CPU, GPU, and OpenVINO, allowing you

## 星数曲线

```mermaid
xychart-beta
    title "felixdittrich92/docling-OCR-OnnxTR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `df63b09335be` · [字段定义](../../DATASET.md)*
