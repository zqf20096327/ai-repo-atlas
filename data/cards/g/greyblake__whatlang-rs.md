# greyblake/whatlang-rs

⭐ 1,087 · Rust · MIT · 推送 2025-12-24 · [GitHub](https://github.com/greyblake/whatlang-rs) · [官网](https://whatlang.org/) · 个人维护

**Rust 自然语言检测库：识别文本的语言与书写系统**

以纯 Rust 实现的自然语言检测库，支持 70 种语言，可同时识别书写系统（拉丁、西里尔等）并输出可靠性信息（is_reliable）。算法基于三元组（trigram）语言模型，源自 Cavnar and Trenkle '94 论文，是 Franc (JavaScript) 的衍生作品。提供黑名单语言等配置，附 serde、enum-map、arbitrary 等特性开关；另有 C/Go/Python/Ruby/Elixir 的移植与绑定版本。以 Rust 库形式集成使用，附在线演示站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 70 种语言与书写系统识别
- 基于 trigram 语言模型，纯 Rust 实现
- 输出 is_reliable 可靠性判定（基于唯一 trigram 数与首位得分差）
- 提供 C/Go/Python/Ruby/Elixir 绑定与移植版本

## 适用场景

- 在 Rust 应用中检测用户输入文本的语言
- 多语言内容处理流程中的语言路由或过滤
- 通过 FFI 绑定在 Python/Ruby/Elixir 等环境复用检测能力

## 场景标签

 · 领域:NLP/文本分析

## 证据(README 行号)

> L1: Whatlang - rust library for natural language detection
> L57: The algorithm is based on the trigram language models, which is a particular case of n-grams.

## 星数曲线

```mermaid
xychart-beta
    title "greyblake/whatlang-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 1086 --> 1088
    line [1087, 1087]
```

2026-10-18 1,087 → 2026-10-24 1,087（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `104a89894a39` · [字段定义](../../DATASET.md)*
