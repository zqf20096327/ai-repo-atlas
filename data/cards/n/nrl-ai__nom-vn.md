# nrl-ai/nom-vn

⭐ 14 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/nrl-ai/nom-vn) · [官网](https://nom-vn.nrl.ai/) · 组织维护

**越南语 AI 工具包：本地优先的越南语 RAG、OCR、声调恢复管线**

面向越南语场景的 Python 工具包与 playground 网页应用：将任意 LLM（默认 Ollama，支持 llama.cpp/HF Transformers/OpenAI/Anthropic）与嵌入器、解析器接入越南语感知的 RAG 管线，可作库使用或以 FastAPI+React 网页应用部署（pip 安装后 nom serve 启动）。另提供声调恢复、拼写纠错、分词、OCR、NFC 规范化、摘要、STT 等模块，各任务默认模型均在真实越南语数据上基准测试并给出推荐表。本地优先，数据不出机器；另设企业版（OIDC/RBAC/审计转发等，开源核心协议可插拔）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 越南语感知的 RAG 管线：文档解析、VN 分块、混合检索与重排
- 内置 playground 网页应用（chat 带引文 + 声调恢复/分词/规范化等无状态工具页）
- 各任务默认模型在真实越南语数据上基准测试并附推荐表（spell/diacritic/OCR/STT 等）
- 本地优先，多后端：Ollama（默认）/llama.cpp/HF Transformers/OpenAI/Anthropic

## 适用场景

- 对越南语文档（PDF/DOCX/XLSX/图片等）搭建本地 RAG 问答
- 恢复越南语声调、纠错拼写与 OCR 错误
- 为越南语应用做分词、规范化与语域分类

## 场景标签

`RAG` `文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L12: A local-first toolkit. **No data leaves your machine.** Use any LLM (Ollama by default), any embedder, any document
> L98: |`nom.llm`|`LLM` Protocol + `Ollama` adapter (default `think=False`) + `OpenAI` + `Anthropic`|✅|

## 星数曲线

```mermaid
xychart-beta
    title "nrl-ai/nom-vn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `80e5120c0a75` · [字段定义](../../DATASET.md)*
