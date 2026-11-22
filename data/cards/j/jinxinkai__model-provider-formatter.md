# jinxinkai/model-provider-formatter

⭐ — · [GitHub]() · 个人维护 · 中文 README

**把 /v1/models 列表转成 OpenCode/Cherry Studio 等客户端配置的工具**

读取 OpenAI 兼容的 /v1/models 列表或 OpenAPI 文档，从模型 ID 推断上下文窗口、输出上限、视觉、工具调用与推理模式，生成 OpenCode、Cherry Studio（导入包+deep link）和 VS Code Copilot 的配置文件。内置按厂商官方文档优先的规则表，并为不同厂商生成对应参数方言的推理变体。提供 Web UI（Vue 3 + Koa）、CLI 与 API，界面支持中英文，可经 npm/Docker 部署，也提供 GitHub Pages 静态版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从模型 ID 自动推断上下文、输出上限、视觉与推理能力
- 生成 OpenCode / Cherry Studio / VS Code Copilot 三种客户端配置
- 厂商文档规则优先级：manual > official-doc > upstream > inferred > default
- 提供 Web UI、CLI 与 API 三种使用方式，中英文双语

## 适用场景

- 为 OpenCode 批量生成接入多个模型的配置文件
- 通过 deep link 一键导入模型到 Cherry Studio
- 配置 VS Code Copilot 自定义模型端点

## 场景标签

 · 领域:LLM 基础设施/开发工具

## 证据(README 行号)

> L5: Turns an OpenAI-compatible `/v1/models` list (or an OpenAPI document) into ready-to-use configs for **OpenCode** (`o
> L56: input → ingest → enrich + knowledge → NormalizedModel → adapters → Web / CLI
> L64: |`src/core/adapters/`|OpenCode / Cherry Studio / VS Code Copilot output|

## 星数曲线

```mermaid
xychart-beta
    title "jinxinkai/model-provider-formatter 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-19 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f8c07dceeb2a` · [字段定义](../../DATASET.md)*
