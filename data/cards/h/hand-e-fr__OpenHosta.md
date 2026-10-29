# hand-e-fr/OpenHosta

⭐ 33 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/hand-e-fr/OpenHosta) · [官网](http://www.openhosta.com/) · 组织维护

**Python 语义层库：用类型注解+文档串让 LLM 实现函数**

OpenHosta 是一个 Python 库，将 LLM 集成为 Python 原生函数：开发者定义带类型注解和 docstring 的函数签名，库调用 AI 模型生成实现，无需 DSL 或包装器。提供 emulate/emulate_async/emulate_variants、语义 lambda（closure）、语义测试（test）、Pydantic 与 Callable 等类型守卫、不确定性跟踪、成本跟踪、审计模式与图像输入。模型无关，支持 OpenAI、Ollama、Azure、vLLM 等 OpenAI 兼容端点，可配合 Ollama 完全本地运行。通过 pip 安装。

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

- emulate：由 docstring 与类型注解驱动 AI 实现函数
- 类型守卫校验 LLM 输出（int/dict/Enum/Pydantic/Callable 等）
- 语义测试（test）：模糊逻辑与文化知识型条件判定
- 不确定性跟踪、成本跟踪、审计模式、async 与图像输入

## 适用场景

- 用函数签名+docstring 快速获得 LLM 实现的功能
- 编写需要模糊逻辑或文化知识判断的语义测试
- 配合本地 Ollama 在离线环境运行，数据不出本机

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L13: OpenHosta integrates Large Language Models directly into Python as native functions. Define a function with type hi
> L35: - **Model-agnostic** — Works with OpenAI, Ollama, Azure, vLLM — any OpenAI-compatible endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "hand-e-fr/OpenHosta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f0940c20ed9f` · [字段定义](../../DATASET.md)*
