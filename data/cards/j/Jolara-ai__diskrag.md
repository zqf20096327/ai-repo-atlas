# Jolara-ai/diskrag

⭐ 21 · Python · MIT · 推送 2025-11-21 · [GitHub](https://github.com/Jolara-ai/diskrag) · 组织维护 · 中文 README

**基于 DiskANN 的向量搜索系统，用于构建和检索知识库**

在 DiskANN 之上构建的向量搜索系统：读取 CSV（FAQ 问答对）与 Markdown 文件，使用 OpenAI embedding 模型（默认 text-embedding-3-small）生成向量，建立索引并提供 FAQ 搜索与一般搜索的 HTTP API（8000 端口），另有 diskrag 命令行工具处理文件、合并 collection、重建与修复索引。配置支持 fast/balanced/high 三档索引质量与分块大小设置。运行需 Python 3.11 与 OpenAI API 金钥，通过 Makefile、脚本或手动命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DiskANN 建立向量索引，支持 fast/balanced/high 三档索引质量
- 读取 CSV（FAQ）与 Markdown 文件，可整目录递归处理与合并 collections
- 提供 HTTP API（/faq-search、/search 等）与 diskrag 命令行工具
- 索引诊断与强制重建（doctor / index --force-rebuild）

## 适用场景

- 把 FAQ 问答对或 Markdown 文档建成可搜索的知识库
- 通过 HTTP API 为应用提供向量检索服务
- 维护与修复已有的向量索引 collection

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: 基於 DiskANN 的向量搜尋系統，用於建立知識庫並進行搜尋。
> L164: - `POST /faq-search` - FAQ 搜尋
> L238: - **Embedding 模型**: `text-embedding-3-small` (預設), `text-embedding-3-large`

## 星数曲线

```mermaid
xychart-beta
    title "Jolara-ai/diskrag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `35b06f191d03` · [字段定义](../../DATASET.md)*
