# evinism/mistql

⭐ 393 · Rust · MIT · 推送 2026-02-23 · [GitHub](https://github.com/evinism/mistql) · [官网](https://mistql.com) · 个人维护

**面向 JSON 类数据的嵌入式查询/表达式语言，供应用集成**

MistQL 是一种针对 JSON 类结构的查询与表达式语言，定位为嵌入到应用程序中的通用表达式语言。同一查询语句在 Python、JavaScript、Rust 实现下具有一致的行为语义，并提供语言无关的共享测试套件。代码仓库为 monorepo，包含文档站、npm 与 PyPI 实现、尚未发布的 Rust 实现及共享测试资产；浏览器版本目标保持约 5kb 体积。语言规范计划在 0.5.0 版本后独立制定，当前以 Lark 语法定义语法。

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

- 同一查询在 Python/JavaScript/Rust 实现下行为一致
- 语言无关的共享测试套件位于 /shared 目录
- 浏览器实现目标体积约 5kb（gzipped）
- monorepo 包含文档站、JS/Python/Rust 三种实现

## 适用场景

- 在应用中嵌入统一的 JSON 数据查询与计算能力
- 跨语言项目共享同一套数据变换表达式
- 对事件流等 JSON 数据做分组、过滤等管道操作

## 场景标签

 · 领域:数据处理/开发者工具

## 证据(README 行号)

> L9: MistQL is a query language for JSON-like structures, built for embedding across multiple domains. It supports
> L36: The primary power of MistQL comes from its strong cross-platform behavior semantics. For example, the following hav

## 星数曲线

```mermaid
xychart-beta
    title "evinism/mistql 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 392 --> 394
    line [393, 393]
```

2026-10-18 393 → 2026-10-28 393（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `e1dcc7308b9e` · [字段定义](../../DATASET.md)*
