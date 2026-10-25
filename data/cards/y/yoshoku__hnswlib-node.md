# yoshoku/hnswlib-node

⭐ 139 · C++ · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/yoshoku/hnswlib-node) · [官网](https://www.npmjs.com/package/hnswlib-node) · 个人维护

**为 Node.js/TypeScript 提供 Hnswlib 近似最近邻搜索绑定**

 hnswlib-node 是 C++ 库 Hnswlib 的 Node.js 绑定，基于分层可导航小世界图实现近似最近邻（ANN）搜索。以 npm 包形式提供，通过 TypeScript/JavaScript 导入 HierarchicalNSW 类即可生成向量索引、插入数据点并执行最近邻查询；支持索引的保存与加载（示例含 loading index），文档中另提供在 AWS Lambda 上运行的指南。Apache-2.0 许可。

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

- Node.js/TypeScript 绑定 Hnswlib 的 ANN 搜索
- HierarchicalNSW 类支持构建索引与最近邻查询
- 提供 AWS Lambda 运行指南

## 适用场景

- 在 Node.js 服务中构建和查询向量搜索索引
- 为嵌入向量做近似最近邻检索
- 在 AWS Lambda 等无服务器环境运行 ANN 搜索

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L8: hnswlib-node provides Node.js bindings for Hnswlib
> L9: that implements approximate nearest-neighbor search based on

## 星数曲线

```mermaid
xychart-beta
    title "yoshoku/hnswlib-node 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 137 --> 139
    line [138, 138]
```

2026-10-18 138 → 2026-10-25 138（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9d3d4975c0fd` · [字段定义](../../DATASET.md)*
