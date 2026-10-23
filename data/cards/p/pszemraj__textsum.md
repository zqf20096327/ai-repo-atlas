# pszemraj/textsum

⭐ 134 · Python · Apache-2.0 · 推送 2025-11-07 · [GitHub](https://github.com/pszemraj/textsum) · 个人维护

**用 transformers 摘要模型处理任意长度文本文档的工具**

基于 transformers 的文本摘要工具包，对任意长度的文本文档生成摘要，提供 Python API、CLI（textsum-dir）和 Gradio UI 演示三种接口。CLI 支持批量处理目录内文件、断点续跑、指定 HuggingFace 模型。支持 8-bit 量化、TF32、Optimum ONNX Runtime、模型编译等推理优化。默认模型较小以控制内存占用，可加载模型库中任意 text-to-text 摘要模型。ONNX 与 force_cache 特性标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Python API / CLI / Gradio UI 三种使用接口
- CLI 支持目录批量摘要与跳过已完成文件
- 支持 8-bit 量化、TF32、ONNX Runtime、模型编译等推理优化
- 可使用 HuggingFace 模型库中任意摘要模型

## 适用场景

- 批量摘要目录下的文本文件
- 在 Python 程序中调用摘要能力
- 通过浏览器 UI 快速试用摘要功能

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: > a utility for using transformers summarization models on text docs 🖇
> L10: This package provides easy-to-use interfaces for using summarization models on text documents of arbitrary length. 

## 星数曲线

```mermaid
xychart-beta
    title "pszemraj/textsum 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-23 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `82af8b6c6a33` · [字段定义](../../DATASET.md)*
