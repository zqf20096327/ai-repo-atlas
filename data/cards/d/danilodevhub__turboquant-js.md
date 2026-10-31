# danilodevhub/turboquant-js

⭐ 19 · TypeScript · MIT · 推送 2026-07-11 · [GitHub](https://github.com/danilodevhub/turboquant-js) · [官网](https://www.npmjs.com/package/turboquant-js) · 个人维护

**给 JS 开发者的向量量化库：向量索引与 LLM KV 缓存压缩**

Google TurboQuant 论文（ICLR 2026）算法的 TypeScript 实现，提供三个层次 API：VectorIndex 最近邻检索索引、KVCacheCompressor 用于浏览器内 LLM 推理的 KV 缓存压缩，以及 TurboQuantMSE/TurboQuantProd 底层量化器。采用随机 Hadamard 旋转 + Lloyd-Max 标量量化 + QJL 符号校正的两级方案，无需训练，产出无偏内积估计，零运行时依赖，包体积约 15 KB。限制：QJL 投影矩阵 O(d²) 存储，大维度时代价高；低比特下 Recall@10 约 36%-50%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VectorIndex / KVCacheCompressor / 底层量化器三层 API
- 零训练、零依赖，Node.js 与浏览器通用，包约 15 KB
- 两阶段量化（MSE + QJL）保证无偏内积估计
- 索引支持 toBuffer/fromBuffer 二进制序列化

## 适用场景

- 在浏览器扩展里本地索引并语义搜索书签、笔记、历史
- 压缩浏览器内 LLM 推理的 KV 缓存以降低内存占用
- 在 Cloudflare Workers 等边缘环境跑纯 JS 向量检索
- 测试与 CI 中用确定性（可设种子）向量搜索替代向量数据库

## 场景标签

`语义搜索` `模型量化` · 领域:知识与检索

## 证据(README 行号)

> L17: - **Two application APIs** — `VectorIndex` for nearest-neighbor search, `KVCacheCompressor` for LLM KV cache compre
> L35: - **KV cache compression** — The `KVCacheCompressor` API compresses attention keys and values for in-browser LLM in

## 星数曲线

```mermaid
xychart-beta
    title "danilodevhub/turboquant-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `25f096877f3d` · [字段定义](../../DATASET.md)*
