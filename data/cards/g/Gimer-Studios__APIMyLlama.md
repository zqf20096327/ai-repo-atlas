# Gimer-Studios/APIMyLlama

⭐ 204 · JavaScript · MIT · 推送 2026-03-30 · [GitHub](https://github.com/Gimer-Studios/APIMyLlama) · 组织维护

**为 Ollama 服务器提供 API 密钥分发的网关服务器**

Node.js 服务器应用，运行在 Ollama 之前作为接口层：通过 generatekey/addkey/removekey 等命令生成和管理 API 密钥（存入本地 SQLite 数据库），支持按密钥设置每分钟速率限制（默认 10 次/分钟）、启用/停用密钥、密钥描述、实时更换端口与 Ollama 地址、以及请求触发 Webhook 通知（如 Discord）。提供 npm/pip/Jitpack(Gradle/Maven)/Cargo 四种语言的客户端包，含 generate 与健康检查 API。面向希望向外部分发受控 Ollama API 访问的开发者。

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

- API 密钥生成/添加/停用/批量操作，存入本地数据库
- 按密钥的每分钟速率限制（默认 10 次/分钟）
- 请求触发 Webhook 通知（如 Discord）
- npm/pip/Jitpack(Java)/Cargo(Rust) 四语言客户端包与健康检查

## 适用场景

- 为自己的 Ollama 服务器发放和管理 API 密钥供他人调用
- 对分发出去的密钥做速率限制与启用/停用控制
- 通过 Discord Webhook 接收 API 请求告警

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: APIMyLlama is a server application that provides an interface to interact with the Ollama API, a powerful AI tool to
> L177: ## Working with the API

## 星数曲线

```mermaid
xychart-beta
    title "Gimer-Studios/APIMyLlama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 203 --> 205
    line [204, 204]
```

2026-10-18 204 → 2026-10-27 204（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3b4706727cbd` · [字段定义](../../DATASET.md)*
