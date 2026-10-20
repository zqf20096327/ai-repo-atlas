# VectifyAI/PageIndex

⭐ 39,256 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/VectifyAI/PageIndex) · [官网](https://pageindex.ai) · 组织维护

**面向长专业文档 RAG 的树状索引检索引擎，无需向量库**

PageIndex 用层次化树索引替代向量索引：索引阶段从文档版式提取树结构并由基础模型摘要精炼，检索阶段由 LLM 在树上推理式搜索定位相关章节，不需要向量数据库与分块。以 pip 包提供 SDK，支持本地模式（本地索引/检索/对话，用自有 LLM key）与 PageIndex Cloud（托管解析、OCR、存储）两种形态；提供 OpenAI Agents SDK、Claude Agent SDK 集成路径。开源版仅处理文本型 PDF；扫描件与图像文档需走云服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 22,16 位贡献者
- 涨星:近 1 天 **+84**(自 20261016 起算)
- 安装:pypi 包 `pageindex` 月下载 117,984
- 平台:— · 协议:MCP

## 能力要点

- 树状索引 + LLM 推理检索，无向量库、无分块
- SDK 本地模式：本机索引/检索/对话，用自有 LLM key
- 可接入 OpenAI Agents SDK / Claude Agent SDK 等 agent 框架
- 本地索引成本与耗时的基准数据（约 $0.001/页，9–1,098 页文档 13 秒–4.5 分钟）

## 适用场景

- 对财报、法律文件、技术手册等长 PDF 做问答检索
- 把文档检索工具接入自己的 agent 框架
- 本地用自有模型 key 建立可溯源的文档索引

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L7: # PageIndex: Vectorless, Reasoning-based RAG
> L30: 1. **Index**: generate a **tree-structure index** for each document
> L76: Drop PageIndex tools into the OpenAI Agents SDK, the Claude Agent SDK, or any other framework.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `93086187c45a` · [字段定义](../../DATASET.md)*
