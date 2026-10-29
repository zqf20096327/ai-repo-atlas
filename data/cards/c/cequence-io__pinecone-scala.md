# cequence-io/pinecone-scala

⭐ 19 · Scala · MIT · 推送 2026-10-18 · [GitHub](https://github.com/cequence-io/pinecone-scala) · 组织维护

**面向 Scala 开发者的 Pinecone 向量数据库异步客户端库**

由 Cequence 维护的社区库（与 Pinecone 公司无关联），以异步 Scala API 封装 Pinecone 的全部端点：向量操作（upsert/query/fetch/update/delete）、索引与集合管理、推理操作（embedData/rerank/evaluate）以及 Assistant 操作（含文件上传与 chatWithAssistant）。通过 PineconeVectorService、PineconeIndexService、PineconeInferenceService 及两个 Assistant 服务提供，调用均返回 Future。依赖仅 play-ws 两个库，支持 Scala 2.12/2.13/3，经 sbt 或 Maven 引入，凭 API key（环境变量或配置文件）访问 pod 或 serverless 服务。

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

- 覆盖 Pinecone 向量/索引/集合/推理/Assistant 五类操作端点
- 全异步 API，调用返回 Future
- 顶层依赖仅 play-ahc-ws-standalone 与 play-ws-standalone-json 两个库
- 支持 Scala 2.12、2.13 与 3

## 适用场景

- 在 Scala 项目中读写 Pinecone 向量索引并执行相似度查询
- 通过代码管理 Pinecone 索引、集合与 Assistant 及其文件
- 在 Scala 中调用 Pinecone 的嵌入生成、rerank 与问答评估推理端点

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L4: This is an intuitive async full-fledged Scala client for Pinecone API supporting all the available index, vector, co
> L16: **✔️ Important**: this is a "community-maintained" library and, as such, has no relation to Pinecone company.

## 星数曲线

```mermaid
xychart-beta
    title "cequence-io/pinecone-scala 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f7e2c7c0f4c6` · [字段定义](../../DATASET.md)*
