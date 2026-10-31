# neohaskell/NeoHaskell

⭐ 348 · Haskell · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/neohaskell/NeoHaskell) · [官网](https://neohaskell.org) · 组织维护

**面向新手的 Haskell 方言：易学且面向生产发布的编程语言**

NeoHaskell 是聚焦 newcomer 友好与生产效率的 Haskell 方言，本仓库为其 mono-repo，含核心库 nhcore（事件溯源 + CQRS，位于 core/service/）、参考应用与验收测试 nhtestbed、出站集成 nhintegrations、Rust 安装器与 Rust CLI（含捆绑 IDE）。贡献流程通过 Nix flakes 环境与 cabal 构建，提供 ./dev 统一脚本（typecheck watcher、测试、lint）。核心测试套件 nhcore-test-service 需要 PostgreSQL 实例，可用 Docker 启动。另有面向 AI agent 的 AGENTS.md 契约与规范门控变更流水线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心库内置事件溯源 + CQRS（core/service/）
- mono-repo 含 Rust 安装器与 Rust CLI（捆绑 IDE）
- Nix flakes 开发环境 + Cachix 二进制缓存 + ./dev 统一脚本
- AGENTS.md 定义 AI agent 贡献契约与规范门控流水线

## 适用场景

- 用 Haskell 方言快速开发并发布应用
- 构建基于事件溯源与 CQRS 的服务
- 以 AI agent 辅助方式参与语言工具链贡献

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L3:  NeoHaskell is a dialect of Haskell that is focused on newcomer-friendliness and productivity.
> L35: - **`AGENTS.md`** — the agent contract: hard rules, dialect style, and the

## 星数曲线

```mermaid
xychart-beta
    title "neohaskell/NeoHaskell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 347 --> 349
    line [348, 348]
```

2026-10-18 348 → 2026-10-31 348（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `107afc7b398a` · [字段定义](../../DATASET.md)*
