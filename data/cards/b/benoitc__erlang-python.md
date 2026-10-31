# benoitc/erlang-python

⭐ 110 · Erlang · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/benoitc/erlang-python) · 个人维护

**在 BEAM 中嵌入 Python 的互操作库：Erlang/Elixir 调用 Python 并行执行**

通过 dirty NIF 将 Python 解释器嵌入 BEAM VM 的互操作库，供 Erlang/Elixir 开发者调用 Python 函数、求值表达式、流式读取生成器，并支持 Python 回调 Erlang 函数与双向消息传递。提供 worker/owngil/isolated 三种执行模式应对 GIL 与并行问题（free-threading 3.13t+ 或 3.14+ 子解释器可获真并行），每个 Erlang 进程可绑定隔离的 Python 环境。附带 embeddings、语义搜索、RAG、AI 聊天等示例，需自行编译（rebar3），依赖 Erlang/OTP 27+、Python 3.12+ 与 C 编译器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dirty NIF 执行，Python 运行不阻塞 BEAM 调度器
- worker/owngil/isolated 三种上下文模式，free-threading 与子解释器支持真并行
- 进程级隔离的 Python 环境与可重入的 Python→Erlang→Python 回调
- 带语义搜索、RAG、AI 聊天等 AI/ML 示例

## 适用场景

- 在 Erlang/Elixir 服务中调用 Python 的 ML/AI 库（如 sentence-transformers）
- 构建 OTP 监督的有状态 Python actor
- 利用 BEAM 轻量进程对 Python 任务做并行分发

## 场景标签

 · 领域:编程语言互操作/开发库

## 证据(README 行号)

> L14: erlang_python embeds Python into the BEAM VM, letting you call Python functions,
> L33: - **AI/ML ready** - Examples for embeddings, semantic search, RAG, and LLMs

## 星数曲线

```mermaid
xychart-beta
    title "benoitc/erlang-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-31 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `bbd0c3433190` · [字段定义](../../DATASET.md)*
