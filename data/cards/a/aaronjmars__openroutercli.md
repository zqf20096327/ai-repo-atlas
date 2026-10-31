# aaronjmars/openroutercli

⭐ 14 · JavaScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/aaronjmars/openroutercli) · [官网](https://www.npmjs.com/package/@aaronjmars/openroutercli) · 个人维护

**覆盖全部 OpenRouter 端点的非官方 CLI，面向人类与 LLM agent**

Node.js 20+ 编写的 OpenRouter API 命令行客户端，零 npm 依赖，将 OpenRouter 全部端点映射为 CLI 命令：浏览器 OAuth(PKCE) 登录、流式聊天、消息/补全/嵌入/重排/语音/视频/转录、批处理、模型发现与端点对比、账单与活动审计、密钥/护栏/工作区管理，以及 request 逃生通道访问任意未来端点。用户密钥与管理密钥分槽自动路由；TTY 流式输出、管道时切换 JSON，稳定退出码便于脚本分支。支持 npm/npx 安装或源码 npm link。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAPI spec 中每个 OpenRouter 端点均有对应命令，另有 request 原始请求逃生通道
- OAuth(PKCE) 浏览器登录，用户/管理密钥双槽分存并按命令自动选择
- 每条命令支持 --json 与稳定退出码，供脚本与 agent 管道消费
- 零 npm 依赖，纯 Node 20+ 内置 fetch/parseArgs/crypto

## 适用场景

- 在 shell 中直接向任意模型发一次性提示词或对比多个模型
- 脚本/agent 通过 --json | jq 稳定解析输出并按退出码分支
- 查询余额、逐密钥支出与逐请求元数据做成本监控和审计
- 在 onboarding 流程中批量创建/轮换/禁用 per-customer 密钥

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13:  Every OpenRouter endpoint, on the command line - for humans and LLM agents
> L20: - Streams chat completions in a TTY; emits clean JSON when piped or with `--json`. Built so an agent can `--json | 

## 星数曲线

```mermaid
xychart-beta
    title "aaronjmars/openroutercli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4896fdf107ab` · [字段定义](../../DATASET.md)*
