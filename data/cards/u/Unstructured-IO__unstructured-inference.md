# Unstructured-IO/unstructured-inference

⭐ 210 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Unstructured-IO/unstructured-inference) · 组织维护

**文档版面解析模型推理库：检测+OCR 提取文档文本元素**

unstructured 生态的托管模型推理库，为 unstructured 包的 partitioning 模块提供版面解析模型调用。推理流程：用检测模型（Detectron2、YOLOX 等）定位文档页面的文本元素，再通过直接抽取、OCR 及可选的表格推理模型提取内容。支持通过 get_model 按关键字切换模型，或包装自定义检测模型（需实现 predict 与 initialize 方法）。Detectron2 需单独源码安装，Windows 非官方支持。要求 Python>=3.11,<3.14。

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

- 检测模型+OCR 的文档版面推理流程
- 内置多个检测模型（Detectron2、YOLOX）
- 自定义检测模型可经 UnstructuredObjectDetectionModel 包装接入

## 适用场景

- PDF 等文档的版面分析与文本元素提取
- 为 unstructured 分区流程提供模型推理后端
- 替换或接入自定义文档检测模型

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L8: The `unstructured-inference` repo contains hosted model inference code for layout parsing models.
> L67: The inference pipeline operates by finding text elements in a document page using a detection model, then extractin

## 星数曲线

```mermaid
xychart-beta
    title "Unstructured-IO/unstructured-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 209 --> 211
    line [210, 210]
```

2026-10-18 210 → 2026-10-28 210（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f0ecfa241551` · [字段定义](../../DATASET.md)*
