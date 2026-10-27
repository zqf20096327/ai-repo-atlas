# huggingface/pyo3-special-method-derive

⭐ 25 · Rust · MIT · 推送 2026-09-24 · [GitHub](https://github.com/huggingface/pyo3-special-method-derive) · [官网](https://docs.rs/pyo3_special_method_derive/) · 组织维护

**Rust 过程宏：为 PyO3 类型自动派生 Python 魔术方法**

面向使用 PyO3 编写 Python 扩展的 Rust 开发者的过程宏 crate：通过 derive 宏在结构体与枚举上自动生成 __str__、__repr__、__dir__、__getattr__、__dict__ 等 Python 魔术方法。支持结构体与枚举（受 PyO3 限制，仅 unit 与 complex 枚举），可用 #[skip(...)] 属性跳过指定字段或变体，非 pub 字段自动跳过。使用时需在 PyO3 依赖上启用 multiple-pymethods feature。

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

- 自动派生 __str__/__repr__/__dir__/__getattr__/__dict__ 五种魔术方法
- 支持 #[skip(...)] 属性按需跳过字段或变体
- 非 pub 字段自动跳过派生

## 适用场景

- 在 PyO3 扩展中为 Rust 类型自动实现 Python 魔术方法，减少手写样板代码
- 为暴露给 Python 的结构体定制 dir/getattr 行为

## 场景标签

 · 领域:开发工具/Rust-Python 互操作

## 证据(README 行号)

> L3: This crate enables you to automatically derive Python dunder methods for your Rust crate using PyO3.
> L25: To use `pyo3-special-method-derive`, you should enable the `multiple-pymethods` feature on PyO3:

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/pyo3-special-method-derive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5b657887e8f5` · [字段定义](../../DATASET.md)*
