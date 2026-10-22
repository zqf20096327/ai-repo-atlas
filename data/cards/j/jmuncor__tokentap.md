# jmuncor/tokentap

⭐ 811 · Python · MIT · 推送 2026-06-21 · [GitHub](https://github.com/jmuncor/tokentap) · [官网](https://github.com/jmuncor/tokentap) · 个人维护

**LLM CLI 工具的 token 用量拦截监控代理与终端仪表盘**

通过本地代理拦截 LLM CLI 工具的 API 流量，在实时终端仪表盘中展示 token 用量，提供颜色分级的上下文窗口油量表、prompt 自动存档（Markdown/JSON）与会话汇总。以 Python 包提供，支持 Claude Code、OpenAI Codex、Gemini CLI 与 MiniMax（Gemini 因上游 OAuth 问题暂不可用），零配置安装即用，可经 path-prefix 转发 OpenAI 兼容请求。

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

- 本地代理拦截并实时统计每次请求的 token 消耗
- 上下文窗口油量表（绿<50%/黄50-80%/红>80%）
- 每个 prompt 自动存档为 Markdown 与 JSON
- 支持 Anthropic/OpenAI/Gemini/MiniMax，含通用 run 命令

## 适用场景

- 开发会话中实时查看 LLM CLI 工具的 token 消耗
- 逼近上下文上限前获得可视化预警
- 保存并回查每次请求的 prompt 用于调试

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L19: tokentap tracks token usage for LLM CLI tools with a live terminal dashboard. See exactly how many tokens you're us
> L101: |`tokentap start`|Start the proxy and dashboard|
> L107: Supported providers for `--provider`: `anthropic`, `openai`, `gemini`, `minimax`

## 星数曲线

```mermaid
xychart-beta
    title "jmuncor/tokentap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 810 --> 812
    line [811, 811]
```

2026-10-18 811 → 2026-10-21 811（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a4016652864d` · [字段定义](../../DATASET.md)*
