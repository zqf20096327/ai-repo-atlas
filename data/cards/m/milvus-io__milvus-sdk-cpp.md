# milvus-io/milvus-sdk-cpp

⭐ 53 · C++ · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/milvus-io/milvus-sdk-cpp) · 组织维护

**面向 C++ 开发者的 Milvus 向量数据库官方 SDK**

Milvus 向量数据库的 C++ 客户端 SDK，由 milvus-io 组织维护。提供 MilvusClientV2 请求/响应式 API（旧 MilvusClient 处于维护模式），覆盖连接、集合创建、插入、加载、搜索、DML/DQL、RBAC 等操作。支持从源码构建（需 C++14 编译器、CMake 3.16+、Conan 2），可安装到系统或作为 Conan 包消费；附 8 个从入门到进阶的独立教程工程与可运行示例。README 给出与 Milvus 2.3–3.0 各版本对应的推荐 SDK 版本表。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 MilvusClientV2 请求/响应式客户端 API
- 8 个从入门到进阶的独立教程工程（Quickstart 到 RBAC）
- 源码构建 / make install / Conan 包三种消费方式
- 附与 Milvus 2.3.x–3.0.x 各版本的兼容版本表

## 适用场景

- 在 C++ 应用中连接 Milvus 并执行插入、加载与向量搜索
- 学习 Milvus 的 DML/DQL、索引、RBAC 等完整操作流程
- 通过 CMake 或 Conan 将 SDK 集成到自己的工程

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L6: The C++ SDK for Milvus.
> L82: New applications should use `MilvusClientV2`, which provides the current request/response-style

## 星数曲线

```mermaid
xychart-beta
    title "milvus-io/milvus-sdk-cpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9a0f5b6bdc5d` · [字段定义](../../DATASET.md)*
