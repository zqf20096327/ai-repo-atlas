# theagentplane/chronicle

⭐ 26 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/theagentplane/chronicle) · [官网](https://theagentplane.github.io) · 组织维护

**Agent 决策图录制回放 SDK：无 LLM 调用复现线上失败**

AgentPlane 套件的边缘 SDK，运行在 agent 自身进程内：在决策点（LLM 调用或工具调用边界）录制调用、经 HTTP 保存到控制平面，并可回放已录制的请求以在不调用 LLM 的情况下验证修复。提供 @boundary 装饰器、wrap 客户端封装（OpenAI/Azure/Anthropic/LiteLLM）、LangGraph/ASGI/httpx instrumenter、hooks、脱敏与重试声明。本地存储、CLI 与可视化在 1.0 已移除，归属控制平面；回放仅支持 JSON 可序列化数据，且按边界名加调用次数匹配，不支持流式。

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

- 在 LLM/工具边界录制并保存到控制平面，跨服务经 W3C traceparent 串联
- 回放可指定 cut-point 单点真实执行，其余边界返回录制原始输出
- wrap 自动识别 OpenAI、Azure OpenAI、Anthropic 与 LiteLLM 客户端
- hooks（AbortCall）、默认脱敏（API key/JWT/私钥）与 host 白名单注入

## 适用场景

- 把线上 agent 故障录制成可复现的回归测试
- 验证修复时不发起真实 LLM 调用
- 跨服务多 agent 链路的 trace 记录与成本用量归集

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L27: 1. **Record** what the agent did at each decision point (a *boundary*: an LLM call or a tool call).
> L29: 3. **Replay** one recorded request so a fix can be tested without live LLM calls.
> L101: **5. Replay a recorded request.** A span is the unit of replay. Fetch it by id, stub everything, or

## 星数曲线

```mermaid
xychart-beta
    title "theagentplane/chronicle 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5cc504725b5e` · [字段定义](../../DATASET.md)*
