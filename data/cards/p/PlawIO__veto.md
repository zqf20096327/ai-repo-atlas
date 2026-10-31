# PlawIO/veto

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/PlawIO/veto) · [官网](https://veto.so) · 组织维护

**AI agent 工具调用授权策略运行时：用 YAML 规则拦截/放行/审批**

介于 agent 与其可执行工具之间的策略层：读取工具名与参数，按确定性策略输出 allow/block/warn/log/require_approval 决定。规则以 YAML 定义，可用自然语言提示生成；本地路径无需 provider SDK 或 API key，prose 生成支持云端/自托管端点并带本地确定性模板回退。面向使用 LangChain、Vercel AI SDK、OpenAI Agents、MCP 等框架的开发者，提供 TypeScript SDK、Python SDK、CLI、Docker 自托管与 BYOC 部署物，决策可写入离线可验证的 receipt 链。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- block/allow/warn/log/require_approval 五种动作的确定性策略评估
- 自然语言提示生成 YAML 规则，LLM 不可用时回退本地模板
- 适配 Vercel AI SDK / OpenAI Agents / LangChain / MCP 等十余种运行时
- 决策写入离线可验证的 veto.receipt/1 receipt 链

## 适用场景

- 在 agent 执行 shell/文件/资金操作前加拦截与审批关卡
- 为不同 agent 框架统一接入工具调用策略与审计日志
- 在自有基础设施上自托管策略服务并离线验证决策记录

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: Veto sits between an agent and the tools it can execute. It evaluates tool name + arguments against deterministic po

## 星数曲线

```mermaid
xychart-beta
    title "PlawIO/veto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e68f2eee0815` · [字段定义](../../DATASET.md)*
