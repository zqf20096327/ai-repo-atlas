# beihzb/dsh-opencode-session-header

⭐ 16 · JavaScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/beihzb/dsh-opencode-session-header) · 个人维护 · 中文 README

**DSH 插件：为 OpenCode Go 请求注入会话头，修复 400 错误**

面向 DeepSeek Harness (DSH) 的插件：在 Fetch 传输中间件中，仅当请求主机命中 opencode.ai 白名单时注入 x-opencode-session 头，取值为当前 DSH 会话 id，以此修复 OpenCode Go 自 2026-09-05 起返回的 400 MissingSessionID 拒绝，同时保留按会话路由与 prompt-cache 优化。通过 JSON 状态文件可在不重启的情况下开关注入；零依赖，其他主机请求逐字节透传。随 DSH 插件命令安装，上游原生修复发布后建议卸载。

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

- 仅对 opencode.ai 白名单主机注入 x-opencode-session 头
- 通过 AsyncLocalStorage 从 llm/stream 取得每会话稳定 id
- JSON 状态文件运行时开关，无需重启
- 自有 fetch pipeline 键，与其他 fetch 补丁插件共存

## 适用场景

- DSH 用户修复调用 OpenCode Go 模型时的 400 MissingSessionID 错误
- 保留 OpenCode 按会话的 prompt-cache 与路由优化
- 需要临时关闭注入时不重启切换

## 场景标签

 · 领域:LLM 工具链/编码代理基础设施

## 证据(README 行号)

> L7: Per-conversation `x-opencode-session` header injection for **DeepSeek Harness (DSH)** → **OpenCode Go**.
> L9: It fixes the `400 MissingSessionID` rejection **and** keeps OpenCode's per-conversation routing / prompt-cache optim
> L68: 1. **`llm/stream` waterfall observer** — wraps every adapter stream iteration in an `AsyncLocalStorage` carrying `G

## 星数曲线

```mermaid
xychart-beta
    title "beihzb/dsh-opencode-session-header 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2d867a7a83cf` · [字段定义](../../DATASET.md)*
