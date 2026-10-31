# singhpratech/ferrovec

⭐ 18 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/singhpratech/ferrovec) · [官网](https://singhpratech.github.io/ferrovec/) · 个人维护

**浏览器内持久化向量库：Rust→WASM HNSW 引擎，OPFS 落盘、跨标签页一致**

面向本地优先 Web 应用的向量存储库：用 Rust 实现的 HNSW 图编译为 WASM（77 KB），索引持久化到浏览器 OPFS，通过 Web Locks 单写者选举保持多标签页读写同一存储。内置 transformers.js 自动嵌入（Xenova/all-MiniLM-L6-v2，首次约 23 MB 下载后离线），提供三行 API。崩溃安全机制包括 CRC-32 校验快照（双槽位交替写入）、写前日志（durability strict/relaxed 两档）、混沌测试套件。声明的限制：不保证断电持久性（OPFS flush 非 fsync）、不支持跨用户/设备共享、索引需在一页内存内。

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

- HNSW 索引持久化到 OPFS，重载后无需重建或重新嵌入
- Web Locks + BroadcastChannel 单写者选举实现跨标签页一致
- 内置 transformers.js 自动嵌入，首次下载后全程离线
- 双槽位校验和快照 + 写前日志，声明经 1,000 周期×2 浏览器崩溃测试

## 适用场景

- 本地优先笔记/PKM 应用做离线语义搜索
- 法律/HR/健康等隐私文档的设备内 RAG
- 离线作业类 PWA 在强制关闭后保住已写入数据
- 多标签页控制台共享一个一致的向量索引

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: **The in-browser vector store that _remembers_.** A Rust→WASM HNSW engine that persists to disk (OPFS) and stays con
> L15: Most in-browser vector libraries hand you an *in-memory* index: fast to query, but it evaporates on reload and dive
> L40: **First open downloads the embedding model** (`Xenova/all-MiniLM-L6-v2`, about 23 MB quantized) from the Hugging Fa

## 星数曲线

```mermaid
xychart-beta
    title "singhpratech/ferrovec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1f88f59215a1` · [字段定义](../../DATASET.md)*
