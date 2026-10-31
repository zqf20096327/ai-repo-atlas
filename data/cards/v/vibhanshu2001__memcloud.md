# vibhanshu2001/memcloud

⭐ 14 · TypeScript · MIT · 推送 2025-12-25 · [GitHub](https://github.com/vibhanshu2001/memcloud) · [官网](https://memcloud.vercel.app/) · 个人维护

**局域网内多机内存池化的分布式内存数据存储（Rust）**

用 Rust 编写的 P2P 分布式内存存储：局域网内各设备（macOS/Linux/Windows）通过 mDNS 自动发现组成节点，把闲置 RAM 汇成共享易失存储池。提供 memcli 命令行、memnode 守护进程、Rust SDK 与 npm 的 TypeScript SDK，支持键值存取、数据流式传输、C/C++ 大堆分配拦截转移。数据仅存于内存、不落盘，重启即丢失；提供 Pinned/Cache 两种淘汰模式与基于 Noise 风格握手、ChaCha20-Poly1305 加密的节点认证。LLM KV-cache 卸载列为路线图未实现项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mDNS 零配置发现的多机 RAM 池化存储
- Pinned/Cache 两种持久性模式（Random Sampling LRU 淘汰）
- Ed25519 身份 + Noise 风格握手 + ChaCha20-Poly1305 加密的局域网安全
- CLI、Rust SDK、TypeScript SDK 及 memcli run 大内存分配拦截器

## 适用场景

- 把局域网内闲置台式机的内存当作本机内存扩展，处理超大数据文件
- 团队在局域网内共享构建产物或 ML 模型权重缓存
- 流式转存 GB 级日志/数据流，保持本地进程低内存占用

## 场景标签

 · 领域:分布式基础设施/存储

## 证据(README 行号)

> L11: **MemCloud** is a distributed in-memory data store written in Rust. It allows nodes (such as macOS and Linux machin
> L81: - [ ] LLM KV-cache offloading integration

## 星数曲线

```mermaid
xychart-beta
    title "vibhanshu2001/memcloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `029cbe3050cb` · [字段定义](../../DATASET.md)*
