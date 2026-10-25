# glaforge/embedding-gemma-semantic-search

⭐ 38 · TypeScript · Apache-2.0 · 推送 2026-06-13 · [GitHub](https://github.com/glaforge/embedding-gemma-semantic-search) · 个人维护

**浏览器内语义搜索演示：EmbeddingGemma+Transformers.js 无服务器**

演示型 Web 应用：用 Transformers.js 在浏览器中加载 EmbeddingGemma（308M 参数、多语言 embedding 模型），对用户添加的文档集合与查询计算嵌入并按语义相似度排序，全程无服务器、数据不出本地。嵌入向量以红蓝方格可视化（取前 128 维，利用 Matryoshka 截断特性）。模型文件不在仓库内，默认从 Hugging Face Hub 拉取 ONNX 模型并缓存到浏览器 IndexedDB，也可下载模型文件到 public/model 离线使用。Apache-2.0 许可，声明非官方 Google 产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯浏览器内运行，无服务器、数据不远程发送
- EmbeddingGemma 308M 多语言模型，模型缓存于 IndexedDB
- 文档与查询按语义相似度排序并可视化嵌入向量
- 支持远程 Hub 或本地离线模型两种配置

## 适用场景

- 在本地对一组文档做语义搜索实验
- 学习 Transformers.js 加载 embedding 模型的配置方式
- 体验 Matryoshka 截断嵌入的可视化效果

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L1: # In-browser Semantic Search with EmbeddingGemma
> L3: This project demonstrates how to use a Gemma model variant for semantic search directly in the browser using Transfo
> L15: 3. **Find Similar Documents:** Click the "Find similar documents" button. The application will then compute the emb

## 星数曲线

```mermaid
xychart-beta
    title "glaforge/embedding-gemma-semantic-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `27ef642cae4e` · [字段定义](../../DATASET.md)*
