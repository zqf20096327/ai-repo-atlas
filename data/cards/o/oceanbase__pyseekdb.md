# oceanbase/pyseekdb

⭐ 62 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/oceanbase/pyseekdb) · [官网](https://seekdb.ai) · 组织维护 · 中文 README

**面向 OceanBase/seekdb 的 Python SDK，提供向量与全文检索接口**

OceanBase 官方维护的 Python SDK，统一封装 seekdb 与 OceanBase AI search 的访问：支持嵌入式与远程服务器两种部署模式，提供向量相似度检索、全文与混合检索、内置 embedding 函数接入、collection 管理与数据库管理操作，采用 collection-first API 面向应用工作流。高级数据库操作可通过 MySQL 兼容驱动执行 SQL。以 pip/uv 安装，文档含 RAG 中英文示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一接口覆盖嵌入式与远程服务器两种模式
- 向量、全文与混合检索，内置多种 embedding 模型支持
- collection（表）创建与管理及数据库管理操作
- 可通过 MySQL 兼容驱动执行 SQL 进行高级数据库操作

## 适用场景

- 在 Python 应用中接入 seekdb/OceanBase 的向量与全文检索
- 构建嵌入式或服务器模式的 AI search 数据层
- 管理检索 collection 与数据库，配合 RAG 工作流

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: pyseekdb is a Python SDK for seekdb and OceanBase AI search. It supports embedded and server deployments with vector
> L7: - **Unified API**: Single interface for embedded and remote server modes
> L16: - Docs home: https://docs.seekdb.ai

## 星数曲线

```mermaid
xychart-beta
    title "oceanbase/pyseekdb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-30 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `837515589a22` · [字段定义](../../DATASET.md)*
