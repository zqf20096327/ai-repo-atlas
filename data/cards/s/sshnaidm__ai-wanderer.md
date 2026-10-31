# sshnaidm/ai-wanderer

⭐ 14 · Python · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/sshnaidm/ai-wanderer) · 个人维护

**免费 AI 代理网关：聚合多家免费层模型并自动降级路由**

OpenAI 与 Anthropic 兼容的本地代理服务器：应用统一请求单一端点，代理按优先级将请求路由到多个免费层 AI 提供商（Gemini、Qwen、OpenRouter、xAI、DeepSeek 等），失败或限流时自动尝试下一个，客户端无需改代码。支持每后端 RPM/RPD/TPM 等限额保护免费配额、keep_cycles 多轮重试、单别名模型暴露、环境变量注入密钥、可选 Redis 共享计数状态，并提供 /dashboard 运维面板展示后端健康、延迟与令牌用量。需 Python 3.11+，可 pip、Docker 或源码安装，支持 Render/Railway 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按优先级分组路由，同组随机分摊负载，失败自动降级
- 每后端请求/令牌限额（rpm/rpd/tpm 等），本地 JSON 或可选 Redis 持久化计数
- 同时兼容 OpenAI SDK 与 Anthropic SDK 两种请求格式
- /dashboard 运维面板展示后端状态、成功率、延迟与令牌用量

## 适用场景

- 把多个免费层 API key 聚合成一个本地端点供应用调用
- 某家免费提供商限流或宕机时自动切换，保持应用可用
- 在免费配额内给不同 key 分别设限额分摊用量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: An OpenAI- and Anthropic-compatible proxy server that routes your requests
> L47: 2. The proxy tries providers in priority order (lowest number = highest priority).

## 星数曲线

```mermaid
xychart-beta
    title "sshnaidm/ai-wanderer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `762ddbb7b74f` · [字段定义](../../DATASET.md)*
