# dsukh-agent/supermemory-native

⭐ 10 · Go · MIT · 推送 2026-07-07 · [GitHub](https://github.com/dsukh-agent/supermemory-native) · [官网](https://github.com/dsukh-agent/supermemory-native) · 个人维护

**自托管 Supermemory 服务器的 Go 静态编译轻量替代实现**

用纯 Go 重写的自托管 Supermemory 服务器替代品：以 API 兼容官方 Supermemory SDK 的方式提供记忆与语义检索服务，存储层用纯 Go SQLite 做向量索引，记忆本体以 OKF v0.1 格式的 Markdown 文件存于本地 vault，支持 Git/Obsidian 挂载与双向同步 API。默认通过云端嵌入 API（如 Gemini text-embedding-004）生成向量，本地 CPU/RAM 占用低。安装方式为源码编译（Go 1.25+），面向在低配 VPS/家用服务器上自托管的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 与官方 Supermemory SDK 100% API 兼容，现有客户端无需改代码
- File-First Hybrid RAG：文件系统为源，SQLite 仅作向量索引，查询时从磁盘实时读取文本
- 纯 Go 实现向量运算（余弦相似度/L2 范数/点积），无 CGO，单二进制部署
- 启动时自动将数据库遗留记录迁移为物理 OKF 文件

## 适用场景

- 在低配 VPS 或家用服务器上自托管记忆服务
- 为多个 AI 编码客户端提供共享的跨项目记忆库
- 将记忆 vault 挂载到 Git 或 Obsidian 做双向同步

## 场景标签

`语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: `supermemory-native` is a drop-in, zero-dependency, ultra-high-performance replacement for self-hosted Supermemory s
> L8: It is 100% API-compatible with official Supermemory SDKs, meaning all your existing clients (OpenClaw, Paperclip, Cl

## 星数曲线

```mermaid
xychart-beta
    title "dsukh-agent/supermemory-native 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-22 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `784edce61c75` · [字段定义](../../DATASET.md)*
