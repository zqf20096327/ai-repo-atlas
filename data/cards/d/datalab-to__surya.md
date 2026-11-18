# datalab-to/surya

⭐ 21,600 · Python · Apache-2.0 · 推送 2026-11-13 · [GitHub](https://github.com/datalab-to/surya) · [官网](https://www.datalab.to) · 组织维护

**面向开发者的多语言文档 OCR 与版面分析模型工具包**

Surya 是一个 689M 参数的文档 OCR 与版面视觉语言模型，用单一 VLM 同时完成 OCR、版面分析（含阅读顺序与 token 数估计）和表格识别（输出含合并单元格的 HTML），覆盖 91 种语言。以 pip 安装的 Python 包形式提供，自带 CLI 与 surya_gui 交互式网页查看器；本体是轻量客户端/编排器，首次使用时自动拉起 vllm（NVIDIA GPU，Docker/Podman）或 llama-server（CPU/Apple Silicon）推理后端，也可指向已有 OpenAI 兼容服务。另有 Datalab 托管平台与模型权重的商业许可条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 VLM 同时完成 OCR、版面分析与表格识别（HTML 输出）
- 91 种语言多语言支持
- 自动拉起 vllm / llama.cpp 推理后端，或接入已有 OpenAI 兼容服务器
- 提供 CLI、Python API 与零额外依赖的 surya_gui 网页查看器

## 适用场景

- 批量 OCR 处理 PDF/图像并输出结构化 JSON
- 提取文档版面、阅读顺序与表格结构
- 在浏览器中交互检查版面框、阅读顺序与公式渲染结果

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L19: Surya is a 689M param document OCR and layout VLM with these features:
> L24: - Layout analysis (`Table`, `Picture`, `SectionHeader`, `Equation`, `Form`, etc.) with reading order and token-coun


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `3f48529d12cf` · [字段定义](../../DATASET.md)*
