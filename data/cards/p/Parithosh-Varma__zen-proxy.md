# Parithosh-Varma/zen-proxy

⭐ 24 · JavaScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/Parithosh-Varma/zen-proxy) · 个人维护

**本地代理：让 Claude Code 接 OpenCode Zen 免费模型**

零依赖的 Node.js 本地翻译代理：前端接收 Anthropic Messages API 请求，改写为 OpenAI Chat Completions 格式转发至 OpenCode Zen 端点，再将响应翻译回 Anthropic 格式，覆盖流式增量、工具调用与 thinking/reasoning 块的双向转换。面向想在 Claude Code 中使用 Zen 免费模型（hy3-free、deepseek-v4-flash-free、nemotron-3-ultra-free）的开发者。核心是单个约 400 行的 proxy.js，仅用 Node 内置 http 与 fetch，无安装/构建步骤；默认绑定 127.0.0.1:8083，附 zen-claude 启动器与配置文件两种接入方式。

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

- Anthropic Messages ⇄ OpenAI Chat Completions 双向翻译，含流式/tool_use/thinking 块
- 零依赖：单文件 proxy.js，仅需 Node 18+，无 npm install 与构建步骤
- 每个上游请求带独立 session id，与其它 OpenCode 会话的免费配额互不挤占
- 仅绑定 127.0.0.1，Claude Code 仍在本地执行

## 适用场景

- 在 Claude Code 中使用 OpenCode Zen 的免费模型而无需 Anthropic 付费 token
- 不修改 ~/.claude/settings.json 通过启动器切换模型运行 Claude Code
- 本地完成 Claude Code 与 OpenAI 兼容端点的协议桥接

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Run Claude Code on OpenCode Zen's free models.** A zero-dependency local proxy that speaks Anthropic's Messages AP
> L22: zen-proxy removes the choice. It terminates Anthropic-format requests locally, rewrites them to OpenAI format, forw

## 星数曲线

```mermaid
xychart-beta
    title "Parithosh-Varma/zen-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `060d1b85ffbf` · [字段定义](../../DATASET.md)*
