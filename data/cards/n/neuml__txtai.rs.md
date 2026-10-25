# neuml/txtai.rs

⭐ 114 · Rust · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/neuml/txtai.rs) · 个人维护

**txtai API 的 Rust 客户端绑定**

txtai 是用于语义搜索、LLM 编排与语言模型工作流的一体化 AI 框架，本仓库提供其 API 的 Rust 绑定，使 Rust 项目能够连接并调用运行中的 txtai API 实例。以 crate 形式集成（需搭配 tokio 异步运行时），仓库内含介绍、抽取式问答、零样本分类、pipeline 与工作流等示例程序。限制：不内嵌模型运行，需先启动 txtai API 实例方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 语言访问 txtai API 的绑定库
- 基于 tokio 的异步 IO 调用
- 附带功能演示示例（问答/零样本分类/pipeline）

## 适用场景

- 在 Rust 项目中接入已部署的 txtai API 服务
- 以 Rust 调用语义搜索与 LLM 工作流能力
- 参考示例了解 txtai 功能覆盖范围

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L18: This repository contains Rust bindings for the txtai API.
> L42: txtai.rs connects to a txtai api instance. See this link for details on how to start a new api instance.

## 星数曲线

```mermaid
xychart-beta
    title "neuml/txtai.rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-25 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2ddb16049c31` · [字段定义](../../DATASET.md)*
