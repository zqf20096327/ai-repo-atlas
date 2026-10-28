# shotit/shotit

⭐ — · [GitHub]() · 组织维护

**面向影视的截图搜视频引擎：上传截图定位来源视频**

面向 TV & Film 场景的截图到视频搜索引擎，以 Docker Compose 集群部署，由 watcher/hasher/loader/searcher 等 worker 与 api、media 服务组成，底层使用 Milvus 向量数据库、liresolr、MinIO 对象存储与 MariaDB/Redis 等组件。视频放入 incoming 目录后自动上传、计算哈希并载入向量库，之后通过 HTTP API 以截图 URL 检索，结果 5 秒内返回（含 5,300 万向量规模数据集）。最低配置 2v4G+，首次 API 调用需将哈希全量载入内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截图 URL 输入、HTTP API 返回命中视频帧
- Docker Compose 一键部署多服务集群（含 Milvus、MinIO 等 14 个镜像）
- incoming 目录自动入库流水线：上传→哈希→向量加载
- 5,300 万向量规模数据集检索时间在 5 秒内

## 适用场景

- 影视从业者凭截图定位出处视频
- 批量建立剧集/影片的可截图检索索引
- 私有部署的帧级视频溯源服务

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: Shotit is a screenshot-to-video search engine tailored for TV & Film, blazing-fast and compute-efficient.
> L87: GET http://127.0.0.1:3311/search?url=https://i.ibb.co/KGwVkqy/big-buck-bunny-10.png

## 星数曲线

```mermaid
xychart-beta
    title "shotit/shotit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `504c36e96b79` · [字段定义](../../DATASET.md)*
