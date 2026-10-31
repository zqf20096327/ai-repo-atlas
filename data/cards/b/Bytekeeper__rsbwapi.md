# Bytekeeper/rsbwapi

⭐ 14 · Rust · 推送 2026-10-19 · [GitHub](https://github.com/Bytekeeper/rsbwapi) · 个人维护

**Rust 编写的 Brood War AI bot 客户端库**

面向星际争霸：母巢之战 AI bot 开发者的 Rust 库，封装 BWAPI（社区的 C++ 接口），用于创建和操控游戏 bot。提供 docs.rs 文档、ExampleBot 示例与作者自己的 bot Styx2 供参考。构建支持 Windows（x64 可执行文件可直接用于现有赛事/天梯）与 Linux（可产出 32/64 位可执行文件），Windows-GNU 与 MSVC 目标需通过 rustup/cargo-xwin 配置交叉编译目标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Rust 封装 BWAPI 接口用于编写星际争霸 bot
- 提供 ExampleBot 示例与 docs.rs 文档
- 支持 Windows（GNU/MSVC）与 Linux 目标构建

## 适用场景

- 用 Rust 编写星际争霸：母巢之战的 AI bot
- 参加 SSCAIT 等 bot 赛事或天梯对战
- 学习星际争霸 AI 开发入门

## 场景标签

 · 领域:游戏/游戏AI

## 证据(README 行号)

> L5: `rsbwapi` is a Rust library for building artificial intelligence (AI) for the popular real-time strategy game Starcr
> L7: If you're not familiar with BWAPI, it is a community-developed project that provides a C++ interface to interact wit

## 星数曲线

```mermaid
xychart-beta
    title "Bytekeeper/rsbwapi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b7902b70e6be` · [字段定义](../../DATASET.md)*
