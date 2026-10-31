# pinecone-io/pinecone-rust-client

⭐ 23 · Rust · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/pinecone-io/pinecone-rust-client) · [官网](https://www.pinecone.io/) · 组织维护

**Pinecone 向量数据库的官方 Rust 客户端 SDK**

Pinecone 官方维护的 Rust SDK，供 Rust 开发者以代码方式访问 Pinecone 托管向量数据库。入口为 PineconeClient，可通过参数或 PINECONE_API_KEY 等环境变量配置；支持创建/列出/描述/配置/删除 serverless 与 pod 两类索引，覆盖向量的 upsert、按 ID/值查询、按 ID/过滤条件/全量删除、fetch、update、list，以及 collection 的增删查。需先注册 Pinecone 账号获取 API key，用 cargo add 安装。README 声明 SDK 处于 alpha 状态，更新可能引入破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 serverless 与 pod 两类索引的创建与配置
- 向量 upsert/查询/删除/更新/fetch/list 全操作覆盖
- API key 与控制面主机可经环境变量配置

## 适用场景

- 在 Rust 项目中接入 Pinecone 向量数据库
- 以代码管理索引、向量与 collection 的生命周期
- 构建语义检索或相似度搜索应用的数据访问层

## 场景标签

 · 领域:向量数据库/SDK

## 证据(README 行号)

> L1: # Pinecone Rust SDK
> L3: > ⚠️ **Warning:** This SDK is still in an alpha state. While it is mostly built out and functional, it may undergo c

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pinecone-rust-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `927700050073` · [字段定义](../../DATASET.md)*
