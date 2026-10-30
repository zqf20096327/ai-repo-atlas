# Ganesh-403/semantic-plagiarism-detector

⭐ 16 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/Ganesh-403/semantic-plagiarism-detector) · [官网](https://semantic-plagiarism-detector.streamlit.app/) · 个人维护

**面向教师作业审查的语义查重系统：识别改写式抄袭**

基于 Streamlit 的 NLP 应用，用于检测学生作业中的语义抄袭：用 SentenceTransformers（paraphrase-multilingual-MiniLM-L12-v2，384 维多语言模型）生成段落嵌入，FAISS 向量索引（Flat/IVF）做全量 N×N 相似度检索，按可调阈值（默认 0.59）标记抄袭并支持段落级下钻。提供 SQLite 认证与角色管理（admin/teacher）、Plotly 热图与网络图、自定义片段检索、OCR（本地 Tesseract）解析 PDF/DOCX/TXT，以及 FastAPI REST 扫描接口。支持 pip、源码与 Docker Compose 部署（可选 Redis 缓存）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transformer 嵌入 + FAISS 向量检索检测改写式语义抄袭
- 段落级分块比对与相似对下钻、热图/网络图可视化
- SQLite 认证与 admin/teacher 角色管理，REST API 支持Bearer 认证扫描
- 本地 OCR（Tesseract），文档不外发外部 OCR 服务

## 适用场景

- 教师批量上传学生作业，检测改写或跨文档抄袭
- 粘贴任意片段检索其与已上传作业的相似度
- 机构通过 REST API 集成自动查重流程

## 场景标签

`语义搜索` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L7: An NLP application that detects **semantic plagiarism** in student
> L8: assignments—even when text has been paraphrased—using Sentence Transformers, cosine
> L30: |**Transformer embeddings**|`paraphrase-multilingual-MiniLM-L12-v2` (384-dim, multilingual, accurate)|

## 星数曲线

```mermaid
xychart-beta
    title "Ganesh-403/semantic-plagiarism-detector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9b78e29ab532` · [字段定义](../../DATASET.md)*
