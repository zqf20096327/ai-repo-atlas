# knows-cloud/paperless-iq

⭐ 16 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/knows-cloud/paperless-iq) · 组织维护

**Paperless-NGX 的自托管 AI 附加组件：元数据建议与文档对话**

连接既有 Paperless-NGX 实例的 LLM 附加组件：读取文档 OCR 文本（或视觉模型转录扫描件），生成标题、标签、往来方、文档类型、存储路径与自定义字段的结构化建议，经审批队列写入；提供基于 RAG 的多轮对话式文档检索，带长期记忆与多语言重排。支持 Ollama、Amazon Bedrock、Anthropic、OpenAI 四类提供方，向量存储用 ChromaDB 或 Qdrant，可完全离线运行。面向自托管 Paperless-NGX 用户，尤其是非英语档案场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成结构化元数据建议，经审批队列（可编辑、批量、堆叠）后写入
- 视觉两阶段流水线处理 OCR 效果差的图像型 PDF
- RAG 对话式文档检索：内联引用、长期记忆、多语言重排（bge-reranker-v2-m3）
- 四类 LLM 提供方可切换，索引嵌入自动迁移，可完全离线（Ollama+本地向量库）

## 适用场景

- 给 Paperless-NGX 档案自动生成标签、标题等元数据并人工审核
- 用自然语言对话检索整个文档档案并获得带引用的回答
- 处理扫描质量差、OCR 无文本的图像型 PDF
- 非英语（德/法/西/意等）文档档案的元数据与检索

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: Paperless IQ connects to your existing Paperless-NGX instance and gives it a brain: an LLM reads every document, sug
> L33: Every document is sent to the LLM with its OCR text. The LLM returns structured JSON: title, tags, correspondent, d
> L94: |**Ollama** (local)|✓|✓|

## 星数曲线

```mermaid
xychart-beta
    title "knows-cloud/paperless-iq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cf9ee816cc67` · [字段定义](../../DATASET.md)*
