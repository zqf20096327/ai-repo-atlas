# patterns-ai-core/milvus

⭐ 34 · Ruby · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/patterns-ai-core/milvus) · [官网](http://rubydoc.info/gems/milvus) · 组织维护

**Milvus 向量数据库的 Ruby API 封装库**

为 Milvus 向量搜索数据库提供 Ruby 客户端封装，通过 RESTful API（data-plane-v2）访问 Milvus 服务。覆盖集合管理、数据插入/删除/更新、索引创建与查询、向量搜索与混合搜索、分区、用户/角色管理与别名等接口。属 Langchain.rb 技术栈的一部分，供 Ruby 开发者在应用中接入 Milvus。以 Ruby gem 形式分发，可经 bundler 或 gem install 安装，另提供带 Milvus 服务的 Docker 开发环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装集合、实体、索引、分区等 Milvus 数据面接口
- 支持向量搜索、查询与混合搜索
- 支持用户、角色与权限（grant/revoke）管理
- 提供 Docker Compose 开发环境（含 Milvus 服务）

## 适用场景

- Ruby 应用中接入 Milvus 向量数据库
- Langchain.rb 技术栈下构建向量检索/嵌入存储流程
- 通过 Ruby 脚本管理 Milvus 集合、索引与用户权限

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: Ruby wrapper for the Milvus vector search database API.
> L9: Part of the Langchain.rb stack.

## 星数曲线

```mermaid
xychart-beta
    title "patterns-ai-core/milvus 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-23 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `948c2346e4c1` · [字段定义](../../DATASET.md)*
