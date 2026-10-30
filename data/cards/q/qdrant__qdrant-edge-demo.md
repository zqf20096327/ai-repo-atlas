# qdrant/qdrant-edge-demo

⭐ 63 · Python · 推送 2026-10-24 · [GitHub](https://github.com/qdrant/qdrant-edge-demo) · [官网](https://qdrant.tech/edge/ ) · 组织维护

**智能眼镜离线视觉记忆 POC：CLIP 向量化本地检索找物品**

qdrant 维护的概念验证项目，演示智能眼镜在无网络连接时记住所见内容并帮助找回物品。设备端用 CLIP 模型将视频帧转为向量，跳过冗余帧后存入本地可变分片供即时检索，同时经 SQLite 队列在后台同步到 Qdrant 服务器；CPU 密集的 HNSW 索引构建在服务端完成，眼镜再以不可变分片同步回来，支持部分快照增量下载。运行需要 uv 与 Docker，通过 make 命令启动服务端与演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端 CLIP 模型将视频帧向量化并做帧去重
- 本地可变分片支持无网络时的即时检索
- SQLite 队列后台同步，网络中断时暂存数据
- 可变/不可变双分片设计支持部分快照增量同步

## 适用场景

- 在智能眼镜上离线检索见过的物品（如钥匙）
- 体验 Qdrant Edge 端云协同向量检索架构
- 参考端侧向量存储与后台增量同步的实现

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: This is a proof-of-concept for smart glasses that remember what they see and help you find your keys even without an
> L22: The glasses use a CLIP model to turn video frames into vectors. We compare frame similarity to skip redundant frame

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-edge-demo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-30 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c88b447d6032` · [字段定义](../../DATASET.md)*
