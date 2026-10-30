# aadityansha06/vecdb

⭐ 18 · C · NOASSERTION · 推送 2026-09-19 · [GitHub](https://github.com/aadityansha06/vecdb) · 个人维护

**C 从零实现的磁盘级 ANN 向量数据库，含延迟删除安全架构**

用 C 语言从零编写的磁盘持久化近似最近邻（ANN）向量数据库，自称学习性质项目、未达到生产可用。存储层采用零填充磁盘持久化与内存映射文件，支持 K-Means IVF 索引（索引可序列化重启复用）、cosine/euclidean 距离、基于 epoll 的 TCP JSON API（/search、/insert、/train、/delete-request）及逐表 API Key 认证。核心特性为延迟删除架构：删除请求可经网络提交，但实际删除仅能在服务器本地经人工确认执行，以应对 API Key 泄露场景。负载测试在 1000 并发连接下通过。另提供交互式 TUI 与单命令 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 延迟删除架构：删除仅可本地人工执行，泄露的 API Key 无法删除数据
- K-Means IVF 索引可序列化持久化，重启无需重训
- epoll 事件循环 TCP JSON API，负载测试通过 1000 并发连接
- 逐表 API Key 认证与可插拔距离度量（cosine/euclidean）

## 适用场景

- 学习可扩展 C 系统编程与底层内存管理的实现参考
- 需要删除操作与网络面隔离的向量存储场景实验
- 研究磁盘级 ANN 索引与存储架构的设计写法

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L8: A custom, high-performance, disk-backed Approximate Nearest Neighbor (ANN) vector database
> L48: - **TCP Server with JSON API:** POST /search, /insert, /train, /delete-request routes over an epoll-based event loo

## 星数曲线

```mermaid
xychart-beta
    title "aadityansha06/vecdb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f8b1732bee3c` · [字段定义](../../DATASET.md)*
