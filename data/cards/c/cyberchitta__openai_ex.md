# cyberchitta/openai_ex

⭐ 217 · Elixir · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/cyberchitta/openai_ex) · [官网](https://hexdocs.pm/openai_ex) · 组织维护

**Elixir 语言的 OpenAI API 客户端库**

社区维护的 OpenAI API Elixir 客户端：模块与方法名镜像官方 Python SDK，OpenAI 文档可直接对应使用；不依赖应用配置，以 client struct 传入每次调用，适配 Livebook 与多租户应用。基于 Finch 实现可取消的流式传输，支持 Azure OpenAI 与 OpenAI 兼容代理（本地 LLM、网关）。文档以 Livebook 形式提供并兼作测试套件，每次发布前完整运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模块与方法名镜像官方 Python SDK
- 基于 Finch 的流式传输且支持取消
- 支持 Azure OpenAI 与 OpenAI 兼容代理（本地 LLM、网关）
- Livebook 用户指南兼作发布前运行的测试套件

## 适用场景

- 在 Elixir/Phoenix 应用中接入 OpenAI API
- 通过 Azure OpenAI 或兼容代理（本地 LLM、网关）调用模型
- 在 Livebook 中交互式调用与学习 OpenAI API

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A community-maintained Elixir client for the OpenAI API.
> L12: - **Azure OpenAI and OpenAI-compatible proxies** (local LLMs, gateways) are supported.

## 星数曲线

```mermaid
xychart-beta
    title "cyberchitta/openai_ex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 216 --> 218
    line [217, 217]
```

2026-10-18 217 → 2026-10-25 217（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f80e106876b5` · [字段定义](../../DATASET.md)*
