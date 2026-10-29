# langfuse/claude-observability-plugin

⭐ 29 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/langfuse/claude-observability-plugin) · [官网](https://langfuse.com/integrations/developer-tools/claude-code) · 组织维护

**将 Claude Code 会话遥测发送到 Langfuse 的追踪插件**

Langfuse 官方维护的 Claude Code 插件：通过 hook 把用户提示、agent 轮次、模型生成（含 token 用量与成本）、思考块、工具调用、子 agent 与图像发送到 Langfuse 实现可观测性。面向使用 Claude Code 并希望追踪其会话的开发者。运行依赖 uv（回退到 Python 3.10+ 与 langfuse SDK），通过 Langfuse 公钥/密钥配置，默认指向 cloud.langfuse.com。仅追踪 CLI 与 Code 模式桌面应用，Chat 模式不被追踪；hook 失败不阻塞 Claude Code。

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

- 追踪提示、生成、token/成本、思考块、工具调用与子 agent
- hook 失败仅写日志，不阻塞或拖慢 Claude Code
- 凭据存于 OS keychain，支持 EU 区默认云地址

## 适用场景

- 追踪 Claude Code 编码会话的成本与 token 用量
- 审计 agent 工具调用与用户输入
- 把 Claude Code 遥测接入 Langfuse 可观测性平台

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Claude Code plugin that sends Claude Code
> L5: agent turns, model generations with their token usage and cost, thinking blocks,

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/claude-observability-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bb318d8ce467` · [字段定义](../../DATASET.md)*
