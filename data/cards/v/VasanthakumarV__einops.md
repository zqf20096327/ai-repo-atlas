# VasanthakumarV/einops

⭐ 36 · Rust · 推送 2026-06-22 · [GitHub](https://github.com/VasanthakumarV/einops) · [官网](https://docs.rs/einops) · 个人维护

**Rust 版 einops：深度学习张量维度操作库**

受 Python einops 启发的 Rust 张量操作库，基于 tch 后端（目前唯一可用后端）。通过 einops! 宏用单一表达式完成 rearrange/reduce/repeat 操作，涵盖转置、维度组合、分解、sum/min/max/mean/prod 归约、重复与 squeeze；形状与归约操作可直接写在表达式内，支持从变量或结构体字段以花括号注入维度值。所有代码在编译期生成，无需缓存，区别于 Python 版的三套 API。面向使用 tch 的 Rust 深度学习开发者，以 crate 形式提供。

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

- einops! 宏单一表达式统一 rearrange/reduce/repeat
- 编译期生成代码，无需运行时缓存
- 支持从变量与结构体/枚举字段注入维度形状
- 支持 sum/min/max/mean/prod 归约与 squeeze

## 适用场景

- 在 Rust + tch 项目中做张量维度重排与归约
- 用单一表达式组合转置、分解、重复等操作

## 场景标签

 · 领域:深度学习/张量计算

## 证据(README 行号)

> L7: This library is heavily inspired by python's einops.
> L9: Currently tch is the only available backend.

## 星数曲线

```mermaid
xychart-beta
    title "VasanthakumarV/einops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `baa1b5ad3027` · [字段定义](../../DATASET.md)*
