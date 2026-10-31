# Lam810/visual-document-rag

⭐ 14 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/Lam810/visual-document-rag) · [官网](https://u273179-9099-b42eb921.nmb1.seetacloud.com:8443) · 个人维护 · 中文 README

**面向视觉富文档（PDF 版式/公式/表格）的 RAG 问答系统**

对版式、公式、表格承载主要信息的 PDF 做检索增强问答：先经多阶段视觉管线（DocLayout-YOLO 版式检测、YOLOv8 公式检测、UniMERNet 公式识别输出 LaTeX、PaddleOCR），重组为结构化 Markdown 后再切块、嵌入（Chroma 向量库）并检索回答。项目提供编排、设备抽象、检索层与 Flask 上传/查询前端，视觉模型来自 PDF-Extract-Kit。设计运行于华为昇腾 NPU、CUDA GPU 与 CPU，逐阶段解析设备；在 Ascend 910C 上已验证部分阶段，完整文档管线尚未验证。README 声明为研究原型，无认证层，不建议多租户部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 版式/公式/表格检测识别后重组为结构化 Markdown 再做检索
- 逐阶段设备解析，支持 Ascend NPU / CUDA / CPU（VDR_DEVICE）
- 基于 torch_npu transfer_to_npu shim 处理硬编码 CUDA 路径
- Ascend 910C 上已验证部分阶段，check_ascend.py 提供逐阶段诊断

## 适用场景

- 对含大量公式与表格的学术 PDF 提问
- 在昇腾 NPU 环境运行文档解析与 RAG 管线
- 本地部署文档问答服务并上传 PDF 检索

## 场景标签

`文档解析` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L10: A retrieval-augmented question-answering system for **visually rich documents** — PDFs
> L16: recognition, OCR — reassembles the result as structured Markdown, and only then chunks
> L17: and embeds it for retrieval. Questions are answered against a representation that still

## 星数曲线

```mermaid
xychart-beta
    title "Lam810/visual-document-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2f7ebd4a0b75` · [字段定义](../../DATASET.md)*
