# cohere-ai/cohere-compass-sdk

⭐ 13 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/cohere-ai/cohere-compass-sdk) · 组织维护

**对接 Compass 文档解析与索引的 Python SDK**

Cohere 官方维护的 Python SDK，包含 CompassParserClient 与 CompassClient 两类客户端：前者调用 Compass Parser REST API 解析单文件、多文件及整个文件夹，支持 pdf/docx/json/csv 等多种格式与本地、S3、GCS 等文件系统；后者对接 Compass API 服务器，对索引中的文档执行创建、删除与检索操作。需自备托管 Compass 服务器。v2.0 引入破坏性变更与异步客户端，运行依赖通过 pip/poetry/uv 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CompassParserClient 解析单/多文件与整个文件夹
- 支持 pdf/docx/json/csv 等格式及本地/S3/GCS 等文件系统
- CompassClient 支持索引文档的创建、删除与搜索
- v2.0 新增异步客户端（CompassAsyncClient）

## 适用场景

- 在 Python 代码中批量解析文档并写入 Compass 索引
- 构建基于 Compass 的检索应用
- 需要异步接入 Compass API 的服务端开发

## 场景标签

`文档解析` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: The Compass SDK is a Python library that allows you to parse documents and insert them
> L18: To insert parsed documents into a `Compass` index, the Compass SDK provides a

## 星数曲线

```mermaid
xychart-beta
    title "cohere-ai/cohere-compass-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `db206461d7a9` · [字段定义](../../DATASET.md)*
