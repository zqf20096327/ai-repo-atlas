# evisdrenova/helix

⭐ 24 · Rust · 推送 2026-01-09 · [GitHub](https://github.com/evisdrenova/helix) · 个人维护

**Rust 编写的新版本控制系统，面向 AI 原生开发工作流**

从零构建的版本控制系统（非 Git 封装），采用内存映射索引、并行树构建、BLAKE3 哈希与 Zstd 压缩对象存储，README 称基准测试中多项操作相对 Git 有 20–100× 加速。支持自定义 RPC 推拉协议（Axum 实现服务端）、Git 仓库导入、分支与 HEAD 管理、TUI。定位面向 AI 生成代码工作流与大型 monorepo。当前为实验性项目，合并、diff、冲突解决、认证等功能尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内存映射索引、并行树构建、BLAKE3 哈希、Zstd 压缩 blobs
- 自定义二进制流式 RPC 推拉协议，零往返协商
- Git → Helix 仓库导入器
- 本地 VCS 操作与 TUI 已可用，服务端以 Axum 实现

## 适用场景

- 在大型 monorepo 中执行状态、暂存、提交、日志等本地版本控制操作
- 导入现有 Git 仓库并迁移到 Helix 自有存储格式
- 通过自建 Helix 服务端进行推拉同步

## 场景标签

 · 领域:开发工具/版本控制

## 证据(README 行号)

> L1: # **Helix — A Next-Generation Version Control System**
> L5: Helix is a high-performance version control system designed for the AI-native developer workflow. Helix optimizes fo

## 星数曲线

```mermaid
xychart-beta
    title "evisdrenova/helix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `84ddf5d2864b` · [字段定义](../../DATASET.md)*
