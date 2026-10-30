# henomis/lingoose

⭐ 833 · Go · MIT · 推送 2026-03-15 · [GitHub](https://github.com/henomis/lingoose) · [官网](https://simonevellei.com/lingoose) · 个人维护

**构建 AI/LLM 应用的 Go 框架（模块化抽象层）**

LinGoose 是用于构建 AI/LLM 应用的 Go 框架，定位为功能抽象层与完整方案：按需导入所需模块，可为每个特性选择或自建实现，覆盖 LLM 接入、embeddings、向量索引、prompt、pipeline 等主题。以 Go module 形式安装（go mod init + go mod tidy），快速开始示例需设置 OPENAI_API_KEY 后 go run 运行。README 顶部声明项目不再积极开发，作者转向新的多 agent 框架 Phero，本仓库保持稳定可用。

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

- 模块化设计：仅导入构建应用所需的模块
- 功能抽象层：可自选实现或创建自己的实现
- 以 Go module 形式提供，快速开始含可运行示例

## 适用场景

- 用 Go 从零构建 LLM 应用
- 在同一抽象层下切换不同 AI 特性实现
- 参考其 Q&A pipeline 与 RAG 相关文章实践

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18: LinGoose is a Go framework for building awesome AI/LLM applications.
> L20: - **LinGoose is modular** — You can import only the modules you need to build your application.
> L21: - **LinGoose is an abstraction of features** — You can choose your preferred implementation of a feature and/or cre

## 星数曲线

```mermaid
xychart-beta
    title "henomis/lingoose 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 831 --> 834
    line [832, 833, 833]
```

2026-10-18 832 → 2026-10-30 833（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `310357712ece` · [字段定义](../../DATASET.md)*
