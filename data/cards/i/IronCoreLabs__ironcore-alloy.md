# IronCoreLabs/ironcore-alloy

⭐ 31 · Rust · AGPL-3.0 · 推送 2026-10-02 · [GitHub](https://github.com/IronCoreLabs/ironcore-alloy) · [官网](https://ironcorelabs.com/) · 组织维护

**应用层加密 SDK，含面向 AI 数据的向量加密**

IronCore Labs 的统一加密 SDK，将原 SaaS Shield TSC SDK 与 Cloaked AI 工具合并为一个库，提供标准、确定性与向量三类加密算法。向量加密用于保护存于向量数据库中的 embeddings，配合多种向量数据库集成示例。SDK 以 Rust 编写，通过 uniffi 生成 Java、Kotlin、Python 与 Rust 四种语言绑定。运行需 glibc 2.29+；集成测试需本地 TSP（docker compose 启动）。采用 AGPL 许可并提供商业许可选项。仓库含加密软件出口管制（ECCN 5D002）合规声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标准/确定性/向量三种加密算法
- Rust 编写，uniffi 生成 Java/Kotlin/Python 绑定
- 面向向量数据库的 Cloaked AI embeddings 保护集成示例
- AGPL 许可并另提供商业许可

## 适用场景

- 加密存入关系数据库或键值存储的敏感字段
- 加密向量数据库中的 embeddings 且保持可检索性
- 在 Java/Kotlin/Python/Rust 应用中统一接入应用层加密

## 场景标签

 · 领域:数据安全/加密基础设施

## 证据(README 行号)

> L16: in a single library that you can include in your application. This library provides tools to encrypt data using
> L20: store, vectors that are stored in a vector database, or some combination of these, the Alloy SDK provides the tools
> L35: You can see the examples on our main docs site here. We also have specific vector database integration examples for

## 星数曲线

```mermaid
xychart-beta
    title "IronCoreLabs/ironcore-alloy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `dc0aea26b363` · [字段定义](../../DATASET.md)*
