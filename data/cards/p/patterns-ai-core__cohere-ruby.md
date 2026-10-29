# patterns-ai-core/cohere-ruby

⭐ 18 · Ruby · MIT · 推送 2026-04-28 · [GitHub](https://github.com/patterns-ai-core/cohere-ruby) · [官网](http://rubydoc.info/gems/cohere-ruby) · 组织维护

**Cohere API 的 Ruby 客户端库**

以 Ruby gem 形式封装 Cohere API 的客户端库，属于 Langchain.rb 技术栈的一部分。通过 Cohere::Client 初始化后，可调用 generate、chat（支持流式输出与 Tool use/function calling）、embed、rerank、classify、tokenize/detokenize、detect_language、summarize 等接口。默认使用 Faraday 的 Net::HTTP 适配器，可为高吞吐场景传入 net_http_persistent 等持久连接适配器并配置连接池参数。安装方式为 bundle add 或 gem install，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 chat/generate/embed/rerank/classify/summarize 等 Cohere 接口
- chat 支持流式输出与 Tool use（function calling）
- 可自定义 HTTP 适配器，支持持久连接与连接池配置

## 适用场景

- 在 Ruby/Rails 应用中接入 Cohere 的对话与生成接口
- 调用 Cohere 的嵌入与重排接口构建检索流程
- 在 Langchain.rb 技术栈内作为 Cohere 通道

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L7: Cohere API client for Ruby.
> L9: Part of the Langchain.rb stack.

## 星数曲线

```mermaid
xychart-beta
    title "patterns-ai-core/cohere-ruby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1d2e46f5a5c5` · [字段定义](../../DATASET.md)*
