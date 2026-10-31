# dipjyotimetia/JARVIS

⭐ 14 · Go · 推送 2026-08-17 · [GitHub](https://github.com/dipjyotimetia/JARVIS) · 个人维护

**面向开发测试者的 AI 驱动 API 测试与流量检查 CLI**

用 Go 编写的命令行工具，结合 OpenAI、Anthropic、Google Gemini 或本地 Ollama 模型，从 OpenAPI 规格生成测试数据、测试场景、Pact 契约，并对 API 失败做 AI 根因诊断。同时内置 HTTP/HTTPS 代理流量检查器（记录/回放/透传、TLS 与 mTLS、路径路由、实时 OpenAPI 校验、9090 端口 Web UI）、自签名证书生成、gRPC curl 命令生成与 Jira/Confluence 集成。通过 GitHub Releases 下载二进制安装，配置支持 flag/环境变量/配置文件三级优先。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 OpenAPI 规格生成测试数据/场景/Pact 契约，含边界值与多 locale
- AI 失败分析：根因识别、错误分类、修复建议
- HTTP/HTTPS 代理流量检查：记录/回放/透传、mTLS、路径路由、Web UI
- 四家 AI 提供商可选，支持 LLM_PROVIDER 切换与自动探测

## 适用场景

- 从 OpenAPI 规格批量生成测试数据与测试代码
- 在开发或 CI/CD 流水线中代理并校验 API 流量
- API 失败后用 AI 生成根因分析报告
- 本地用 Ollama 免费模型跑测试生成，云端模型做关键分析

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: An AI-powered CLI tool for intelligent API testing and traffic inspection
> L9: Jarvis is a comprehensive CLI tool that leverages **multiple AI providers** (OpenAI, Anthropic, Google, Ollama) to r
> L32: - **HTTP/HTTPS Proxy**: Record, replay, and analyze API traffic with TLS and mTLS support

## 星数曲线

```mermaid
xychart-beta
    title "dipjyotimetia/JARVIS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4b980fb9ff80` · [字段定义](../../DATASET.md)*
