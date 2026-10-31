# aqiu817/dsh-llm-agentrouter

⭐ 36 · JavaScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/aqiu817/dsh-llm-agentrouter) · 个人维护 · 中文 README

**把 AgentRouter 中转站接入 DeepSeek Harness 的 profile 插件**

DeepSeek Harness 的 profile bundle：在 llm-pi-ai 上声明单条 agentrouter 路由，收录三个模型（gpt-5.6-sol / gpt-6-astra / gpt-6.1-sol）及推理档位，通过「插件」页卡片切换国内/国际端点。围栏在出站路径上改写哨兵主机、替换 User-Agent、为国内端点绕过进程代理直连、补齐工具 schema 的 required 数组，并提供静默重试（应对中转站多渠道方言不一致）、路由自愈（对抗 profile 补丁覆盖）与 402 配额提示。密钥存于凭据文件或环境变量，附 69 项行为测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条路由 + 端点开关（cn/intl），避免模型选择器重复条目
- 国内端点自动绕过代理直连，规避中转站 WAF 对代理出口 IP 的质询
- 静默重试重发渠道方言导致的瞬时 400/5xx，200ms 递增退避
- 桌面端 profile 覆盖路由时在配置解析期自动合并回（claimRoute）

## 适用场景

- 在 DeepSeek Harness 中使用 AgentRouter 中转站的模型
- 国内/国际网络环境间一键切换端点而不重复声明路由
- 应对中转站多上游渠道的请求方言差异与瞬时拒绝

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6: 把 AgentRouter 中转站接入 DeepSeek Harness 的 profile bundle：一条 provider 路由、三个模型及其推理档位，一个在「设置 → 插件」里切换国内 / 国际端点的开关，以及一层让出站请
> L22: |路由声明|`cordis.patch.yml`|覆盖 `llm-pi-ai` 行，声明单条 `agentrouter` 路由，`baseURL` 指向一个哨兵主机|

## 星数曲线

```mermaid
xychart-beta
    title "aqiu817/dsh-llm-agentrouter 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-31"]
    y-axis "stars" 31 --> 37
    line [32, 34, 35, 36]
```

2026-10-18 32 → 2026-10-31 36（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b1d35f74024e` · [字段定义](../../DATASET.md)*
