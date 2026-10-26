# microsoft/synthetic-rag-index

⭐ 38 · Python · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/microsoft/synthetic-rag-index) · 组织维护

**Azure 无服务器文档导入与合成索引服务，服务 RAG 场景**

微软开源的概念验证项目：从 PDF、图片、Office、HTML 等格式提取文本（基于 Azure Document Intelligence 的 prebuilt-layout 模型，部分格式经 MuPDF 转 PDF），经文档综合与事实（Q&A 对）生成后逐条索引到 Azure AI Search，实测 1500 万字符语料缩减 93%。采用 Azure Functions 无服务器架构，闲置不产生费用；索引成本约每千页 29.15 欧元。README 声明不用于生产环境。需 Azure Functions Core Tools 与 config.yaml 配置，通过 make 命令本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 PDF/图片/Office/HTML 等多种格式的 OCR 文本提取
- 合成数据生成替代分块，实测文档量缩减 93%
- 无服务器架构，闲置时无费用
- 垃圾数据检测与内容去重

## 适用场景

- 为 RAG 场景构建规模更小、相关性更高的检索索引
- 批量导入多格式文档到 Azure AI Search
- 实验性地验证 LLM 合成索引相对分块方案的缩减效果

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Service to import data from various sources (e.g. PDF, images, Microsoft Office, HTML) and index it in AI Search. In
> L32: > This project is a proof of concept. It is not intended to be used in production. This demonstrates how can be com

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/synthetic-rag-index 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2df8a10e3599` · [字段定义](../../DATASET.md)*
