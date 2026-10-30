# hit1001/multiagent-visibility-tool

⭐ 15 · JavaScript · NOASSERTION · 推送 2026-05-27 · [GitHub](https://github.com/hit1001/multiagent-visibility-tool) · 个人维护

**多智能体系统的实时追踪、可视化与调试工具**

面向多智能体 AI 系统的可观测性开发工具：以 npm 全局安装后启动本地服务，浏览器访问 localhost:4242 查看面板。提供 LangChain、AutoGen、CrewAI 的 Python 适配器，两行代码接入即可采集 agent 间消息、LLM 轮次（含 token 与延迟）、工具调用、内存读写等数据；支持实时拓扑图、运行历史回放，以及 token 预算/agent 卡住/critic 失败率的 Webhook 告警。给构建和运维多智能体工作流的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 间消息按序追踪与 LLM 轮次检查（prompt/响应/token/延迟）
- 实时拓扑执行图与运行历史逐步回放
- LangChain/AutoGen/CrewAI 的两行接入适配器
- token 预算、agent 卡住、critic 失败率 Webhook 告警

## 适用场景

- 多智能体工作流出错时定位是哪个 agent、哪一步失败
- 查看 agent 之间实际传递的消息与工具调用细节
- 监控生产环境 agent 的 token 预算与卡住状态

## 场景标签

`多智能体` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L34: |🔁 **Agent-to-agent traces**|See every message passed between agents, in order|
> L35: |🧠 **LLM turn inspector**|Full prompt/response history with token counts and latency|
> L57: ### LangChain

## 星数曲线

```mermaid
xychart-beta
    title "hit1001/multiagent-visibility-tool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5a337e53ac5a` · [字段定义](../../DATASET.md)*
