# batish52/codecontext

⭐ 15 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/batish52/codecontext) · [官网](https://pypi.org/project/promptrouter/) · 个人维护

**给开发者的 LLM 网关：本地路由与上下文压缩以降低 API 成本**

CodeContext 是部署在应用与 LLM API 之间的网关：对代码项目建 BM25 + 可选语义嵌入索引，对每个请求先分类——简单提示路由到本地模型或直接跳过外部调用；需外呼的请求只打包最相关的代码块进 token 预算，并设每请求美元花费上限。每次调用的真实 token 数与美元成本写入本地 SQLite 账本，CLI 可输出节省报告与内置基准测试。面向开发 AI 辅助工具的工程师，以 pip 包提供，支持 OpenAI/Anthropic/Ollama/OpenAI 兼容端点，需 Python 3.10+。HTTP API 服务端目前为本地演示性质，鉴权与限流由使用者自行负责。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 请求分类：简单提示路由本地或跳过外部调用
- BM25 + 语义嵌入检索，按 token 预算打包上下文（−40–80% 输入 token）
- 每请求成本上限（默认 $0.08）作为硬性花费护栏
- 真实 token 与美元成本写入 SQLite 账本，含节省基准测试工具

## 适用场景

- 降低代码类 LLM 工作负载的 API 开销并量化节省金额
- 在发送前自动裁剪不相关的文件上下文
- 按项目审计每次 LLM 调用的真实花费

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: CodeContext is a drop-in gateway that sits between your code and the LLM API. It routes trivial prompts to a local m
> L8: your app  ─────►  CodeContext gateway  ─────►  OpenAI / Anthropic / Ollama / any OpenAI-compatible endpoint
> L68: 4. **Call the model** — Speaks OpenAI, Anthropic, Ollama, or any OpenAI-compatible endpoint over HTTP. Caps per-req

## 星数曲线

```mermaid
xychart-beta
    title "batish52/codecontext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `42ad4b7119be` · [字段定义](../../DATASET.md)*
