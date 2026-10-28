# cortesi/ruskel

⭐ 30 · Rust · MIT · 推送 2026-10-17 · [GitHub](https://github.com/cortesi/ruskel) · 个人维护

**生成 Rust crate 公共 API 骨架的命令行工具，可供 LLM 使用**

Ruskel 从 Rust crate 的 rustdoc JSON 生成保留文档注释、剥离实现体的语法有效骨架代码，未在本地的 crate 会从 crates.io 获取；支持 std/core/alloc 标准库。提供按名称/文档/签名多域搜索、条目列表、私有项与 feature flag 控制、专用 rustdoc 构建缓存（含上限与淘汰策略），以及 workspace API 快照目录生成。可作为 MCP 服务器（stdio/TCP）供编码 agent 调用，底层 libruskel 库可分离捕获与持久化。运行需 Rust nightly 工具链及 rust-docs-json 组件，通过 cargo install 安装。

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

- 生成保留 docs、剥离实现的语法有效 crate 骨架，导出单文件供 LLM 使用
- 可作 MCP 服务器（stdio/TCP）供编码 agent 调用单一 ruskel 工具
- 多域搜索（name/doc/signature）与 --list 条目目录
- 带容量上限与淘汰策略的专用 rustdoc 构建缓存

## 适用场景

- 从命令行快速查阅 Rust crate 公共 API
- 把 crate API 导出为单文件喂给 LLM 或编码 agent
- 用 Git 审阅 workspace 公共 API 的变更快照

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L15: - Exporting a crate's public API as a single file for LLMs and other tools.

## 星数曲线

```mermaid
xychart-beta
    title "cortesi/ruskel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1bce88350299` · [字段定义](../../DATASET.md)*
