# Keyvanhardani/german-ocr

⭐ 114 · Python · Apache-2.0 · 推送 2026-05-06 · [GitHub](https://github.com/Keyvanhardani/german-ocr) · [官网](https://german-ocr.de) · 个人维护

**德语文档 OCR 模型与服务：从发票、收据、表单提取文本**

基于 Qwen 微调（LoRA/GGUF）的德语文档 OCR 模型，含 Vision-OCR（图像→严格 JSON）与 Text-Assistant（翻译、摘要、改写、对话）两个专用模型。本地通过 Ollama 拉取或 llama.cpp 加载 GGUF 运行，支持 CUDA/Metal/Vulkan/OpenVINO/CPU；云侧提供法兰克福托管 API（DSGVO 合规，v1 异步、v2 同步结构化提取，€0.10/页）及发票/送货单等模板。提供 Python/Node.js/PHP SDK 与 CLI，集成 Zapier、n8n、各 CMS 与后端框架。

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

- Vision-OCR 图像→严格 JSON，面向发票/收据/表单等德语商业文档
- 本地运行支持 Ollama 拉取与 llama.cpp GGUF（CUDA/Metal/Vulkan/OpenVINO/CPU）
- 云 API 提供模板化结构化提取（invoice/delivery-notes 等，DSGVO 合规）
- Python/Node.js/PHP SDK、CLI 及 n8n/Zapier/CMS 集成

## 适用场景

- 从德语发票中提取字段并输出结构化 JSON
- 本地离线运行 OCR 保护文档隐私
- 通过 n8n/Zapier 把德语文档提取接入自动化流程

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L19: > Engineered + optimized German document AI on Qwen 3.5. **Zero hallucination on real German invoices**, 100 % vali
> L24: > ollama pull Keyvan/german-ocr-3.1
> L64: |**Backends**|Ollama, llama.cpp, HuggingFace|Cloud API|Cloud API|

## 星数曲线

```mermaid
xychart-beta
    title "Keyvanhardani/german-ocr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-25 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1c52548369a2` · [字段定义](../../DATASET.md)*
