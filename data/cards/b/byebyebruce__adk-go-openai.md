# byebyebruce/adk-go-openai

⭐ 29 · Go · 推送 2025-12-08 · [GitHub](https://github.com/byebyebruce/adk-go-openai) · 个人维护

**为 ADK-Go 框架提供 OpenAI 模型接入的 Go 库**

一个 Go 语言包，为 ADK-Go（Agent Development Kit）框架实现 OpenAI 模型支持，通过 go get 安装后以代码方式引入使用。可通过设置 OPENAI_BASE_URL 环境变量指向本地 Ollama 的 OpenAI 兼容端点（http://localhost:11434/v1/），从而在 ADK-Go 中使用本地模型。README 附带 deepwiki-cli 与 quickstart 两个示例。面向使用 ADK-Go 构建 agent 的 Go 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 ADK-Go 提供 OpenAI 模型实现
- 通过 OPENAI_BASE_URL 支持 Ollama 本地模型
- 提供 deepwiki-cli 与 quickstart 示例

## 适用场景

- 在 ADK-Go 框架中接入 OpenAI 模型
- 配合本地 Ollama 运行模型构建 agent

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This package provides an OpenAI model implementation for the ADK-Go framework.
> L15: ## For Ollama

## 星数曲线

```mermaid
xychart-beta
    title "byebyebruce/adk-go-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ac92f1dab70e` · [字段定义](../../DATASET.md)*
