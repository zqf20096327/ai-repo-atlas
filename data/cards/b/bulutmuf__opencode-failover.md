# bulutmuf/opencode-failover

⭐ 51 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/bulutmuf/opencode-failover) · [官网](https://www.npmjs.com/package/opencode-failover) · 个人维护

**OpenCode 插件：跨多把 API key 自动故障转移与轮换**

面向 OpenCode（TypeScript 编码 agent TUI）的插件，通过全局 fetch 补丁拦截请求，为同一 provider 的多把 API key 做加权轮询分发。命中 429/5xx 时按指数退避（60s–300s 封顶，尊重 retry-after）隔离 key，401/403/402 鉴权与计费错误时永久禁用，隔离到期自动恢复。支持 NVIDIA NIM、OpenRouter、Anthropic、OpenAI、Cloudflare Workers AI 及任何 OpenCode 兼容 provider，提供 keychain-setup/remove/status/reset 四个 LLM 自然语言工具与 /keychain TUI 只读面板，key 保存于 .env。限制：仅做 key 层轮换，provider ID 须与模型配置一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加权轮询多 key 分发，429/5xx 指数退避隔离（60–300s 封顶）
- 401/403/402 永久禁用并要求手动恢复，尊重 retry-after 头
- keychain 系列自然语言工具与 /keychain TUI 实时状态面板
- 支持 NVIDIA NIM/OpenRouter/Anthropic/OpenAI/Cloudflare 及自定义 provider

## 适用场景

- 多把 key 池化使用，避开单 key 速率限制
- 在 OpenCode TUI 里用自然语言增删查 API key
- 实时查看各 key 的激活/隔离/禁用状态

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L19: **opencode-failover** is a OpenCode plugin that automatically rotates API keys across multiple provider credentials
> L185: Request    -->  Plugin intercepts via global fetch patch
> L186:              -->  Identifies provider by existing Authorization header

## 星数曲线

```mermaid
xychart-beta
    title "bulutmuf/opencode-failover 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-31 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dadde4268666` · [字段定义](../../DATASET.md)*
