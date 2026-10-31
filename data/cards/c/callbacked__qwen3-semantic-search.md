# callbacked/qwen3-semantic-search

⭐ 60 · TypeScript · 推送 2026-02-25 · [GitHub](https://github.com/callbacked/qwen3-semantic-search) · [官网](https://huggingface.co/spaces/callbacked/qwen3-semantic-search) · 个人维护

**浏览器内本地运行的 Qwen3 嵌入模型语义搜索演示**

基于 Qwen3-Embedding-0.6B 的交互式语义搜索演示应用，通过 transformers.js 在浏览器本地运行：首次访问从 Hugging Face Hub 下载 ONNX 模型并缓存，对记忆库中每条文本生成嵌入向量，查询时计算余弦相似度排序结果，并以交互式图谱可视化语义关系。用户可使用预置的三个记忆库或自建记忆库（IndexedDB 持久化）。配套 reranker 模型因暂无 ONNX 转换未纳入，改用余弦相似度排序。面向普通用户/演示用途，git clone 后 npm install、npm run dev 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- transformers.js 驱动的浏览器本地语义搜索，无需服务器
- 嵌入向量余弦相似度排序与交互式图谱可视化
- 自建记忆库并以 IndexedDB 持久化
- 预置 General/Programming/Science 三个示例记忆库

## 适用场景

- 在浏览器中体验嵌入模型的语义检索效果
- 构建个人笔记/记忆库并按语义查找相关内容
- 直观查看文本之间的语义关联图谱

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: This is a demo of using semantic search with the Qwen3-Embedding-0.6B model that came out recently. All running loca
> L15: 3. **Semantic Search**: When you type a query, it is also converted into an embedding vector. The application then 

## 星数曲线

```mermaid
xychart-beta
    title "callbacked/qwen3-semantic-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-31 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4978901333ac` · [字段定义](../../DATASET.md)*
