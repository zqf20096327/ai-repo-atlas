# germangb/ai-bindgen

⭐ 121 · Rust · MIT · 推送 2026-02-18 · [GitHub](https://github.com/germangb/ai-bindgen) · 个人维护

**Rust 编译期调用 LLM API 生成代码的过程宏**

Rust 过程宏 crate，在编译阶段调用 OpenAI（或兼容）API 生成 Rust 代码：通过 `#[ai]` 标注 extern block，宏读取 OPENAI_API_KEY / OPENAI_API_MODEL 环境变量连接 API，默认端点为 api.openai.com，可用 OPENAI_API_URL 覆盖；生成结果可用 cargo expand 查看。以 git 依赖方式引入 Cargo.toml。README 顶部声明该 crate 可能危险、需自担风险运行。

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

- 编译期通过 LLM API 生成 Rust 代码的过程宏
- 环境变量配置 API key、模型与自定义端点（兼容 OpenAI 协议）
- 通过 Cargo.toml git 依赖引入

## 适用场景

- 在构建流程中实验性地由 LLM 生成函数实现
- 探索编译期 AI 代码生成的可行性

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L6: This is a procedural macro that generates Rust code at compile-time using the OpenAI (or compatible) API. Simply add
> L15: You must have a valid API token and define the following two variables in your environment, so the macro can connec

## 星数曲线

```mermaid
xychart-beta
    title "germangb/ai-bindgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-28 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `a328b71c5e0f` · [字段定义](../../DATASET.md)*
