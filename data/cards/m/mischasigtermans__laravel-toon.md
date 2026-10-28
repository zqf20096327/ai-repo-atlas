# mischasigtermans/laravel-toon

⭐ 147 · PHP · MIT · 推送 2026-03-23 · [GitHub](https://github.com/mischasigtermans/laravel-toon) · [官网](https://toonformat.dev) · 个人维护

**Laravel 的 TOON 编码包：给 LLM 传数据时省约 50% token**

面向 Laravel 开发者的 PHP 包，实现 TOON（Token-Optimized Object Notation）v3.0 规范：将数组、Collection、Eloquent 模型编码为类 YAML 紧凑格式，README 给出基准显示相对 JSON 节省约 50% token，并保持编码/解码往返一致性与标量类型保留。提供全局辅助函数 toon_encode/toon_decode、toToon 宏、字段白名单 Toon::only、省 token 配置（omit 选项、日期格式化）等。适用于 MCP 服务器返回数据、压缩 LLM 上下文与 API 响应。要求 PHP 8.2+ 与 Laravel 10/11/12，通过 composer 安装，测试套件含 470 个测试。

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

- 实现 TOON v3.0 规范并通过官方规范测试套件（470 个测试）
- 相对 JSON 约 50% token 节省，保持往返一致性与标量类型保留
- 提供 Collection 宏 toToon、Eloquent 模型 toToon、Toon::only 字段白名单
- 可选省 token 配置（omit 空值/null）与日期格式化

## 适用场景

- MCP 服务器工具调用返回数据时降低 token 消耗
- 把更多业务数据装进 LLM 上下文窗口
- 为关注 token 成本的客户端提供 TOON 格式 API 响应

## 场景标签

 · 领域:LLM 数据编码/PHP 生态

## 证据(README 行号)

> L8: TOON (Token-Optimized Object Notation) is a compact, YAML-like format designed to reduce token usage when sending da
> L74: When building MCP servers or LLM-powered applications, every token counts. JSON's verbosity wastes context window s

## 星数曲线

```mermaid
xychart-beta
    title "mischasigtermans/laravel-toon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-28 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `04196d360242` · [字段定义](../../DATASET.md)*
