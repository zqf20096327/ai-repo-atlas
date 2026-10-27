# softwarewrighter/rlm-project

⭐ 26 · Rust · 推送 2026-01-24 · [GitHub](https://github.com/softwarewrighter/rlm-project) · 个人维护

**Rust 实现递归语言模型：让 LLM 处理超长上下文**

基于 MIT CSAIL 论文《Recursive Language Models》的 Rust 实现：LLM 输出结构化 JSON 命令（slice/find/regex/llm_query 等）由执行器运行，迭代检查上下文直到给出最终答案，可处理超出模型上下文窗口约两个数量级的输入。当前版本通过 wasmtime 支持沙箱化 WASM 动态代码执行，提供 Rust/Axum 服务器、REST API 与交互式 HTML 可视化。支持 DeepSeek 与 Ollama（本地/远程）多提供方，可经 LiteLLM 网关统一访问。保留的 Python PoC 被标注为遗留参考、不建议生产使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 输出结构化 JSON 命令（slice/find/regex/llm_query 等）由执行器迭代执行
- wasmtime 沙箱化 WASM 动态代码执行
- Rust/Axum 服务器提供 REST API 与 /visualize 交互式可视化
- 多提供方支持：DeepSeek、Ollama（本地/远程）、LiteLLM 网关

## 适用场景

- 处理超出模型上下文窗口的超长文本（如整本书）并提问
- 在长日志中定位错误、排序统计
- 通过可视化界面观察 RLM 的迭代推理过程

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L18: RLM is an inference strategy that allows LLMs to process **arbitrarily long contexts** by:
> L22: 3. Iterating until the LLM reaches a final answer
> L33: |**Rust Orchestrator**|✅ Production|Pure Rust, structured JSON commands, WASM support|

## 星数曲线

```mermaid
xychart-beta
    title "softwarewrighter/rlm-project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5ab409f81aa4` · [字段定义](../../DATASET.md)*
