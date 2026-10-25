# langchain-ai/langchain-ibm

⭐ 37 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/langchain-ai/langchain-ibm) · [官网](https://python.langchain.com/docs/integrations/providers/ibm) · 组织维护

**LangChain 的 IBM watsonx 与 Db2 向量库集成包**

langchain-ai 维护的 monorepo，含两个 Python 包：langchain-ibm 将 IBM watsonx 接入 LangChain，langchain-db2 提供 IBM Db2 数据库的向量存储与向量检索集成。README 主要面向贡献者，说明仓库结构、uv 安装开发依赖、ruff/mypy 格式化与 lint、单元/集成测试流程，集成测试需设置 WATSONX_APIKEY、WATSONX_PROJECT_ID 等环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- langchain-ibm 包接入 IBM watsonx
- langchain-db2 提供 Db2 向量存储与向量搜索
- monorepo 结构，各包含单元测试与集成测试

## 适用场景

- 在 LangChain 应用中使用 IBM watsonx 模型
- 用 IBM Db2 作为 LangChain 的向量存储后端
- 参与贡献这两个集成包的开发

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5: This repository contains 2 package with IBM integrations with LangChain:
> L7: - langchain-ibm integrates IBM watsonx.
> L8: - langchain-db2 integrates IBM Db2 database vector store and vector search.

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langchain-ibm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e186a66d80e` · [字段定义](../../DATASET.md)*
