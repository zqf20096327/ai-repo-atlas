# ProvablyAI/sourcerykit

⭐ 21 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/ProvablyAI/sourcerykit) · [官网](http://provably.ai/) · 组织维护

**Python SDK：为 agent 的 API/MCP 调用生成可验证证明与错误检测**

面向 AI agent 开发者的 Python SDK（3.12+），通过自动拦截 HTTP/API/MCP 请求与响应，将证据提交到 QEDB 可验证数据库，生成约 1KB 的便携式证明；agent 的声明可与加密锚定记录比对，得出 PASS/CAUGHT/ERROR 确定性裁决，供下游 agent 触发重试与修复流程。支持端点白名单拦截未信任请求，可嵌入 OpenAI Agents SDK、LangChain、CrewAI、LangGraph 等框架。初始化需通过 OAuth 账号向 Provably 后端注册，代码以 Business Source License 1.1 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动拦截 HTTP/API/MCP 调用并提交至 QEDB 可验证数据库，无需改动 agent 代码
- 声明核验产生 PASS/CAUGHT/ERROR 确定性裁决，供下游 agent 触发重试
- 端点白名单在源头阻断未信任请求
- 框架无关，支持 OpenAI Agents SDK、LangChain、Claude Agent SDK、CrewAI、LangGraph

## 适用场景

- 为 agent 的工具调用与数据引用建立可审计的证据链
- 在多 agent 流程中检测上游回答错误并自动重试修复
- 限制 agent 只能访问白名单内的受信任端点

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L8: SourceryKit is the Python SDK for Provably. Agents self verify API and MCP calls against recorded source evidence an
> L17: - **Automatic HTTP interception** — records supported API and MCP requests and responses, then commits the evidence
> L20: - **Framework-agnostic** — drops into OpenAI Agents SDK, LangChain, Claude Agent SDK, CrewAI, and LangGraph.

## 星数曲线

```mermaid
xychart-beta
    title "ProvablyAI/sourcerykit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e40a9ab25c69` · [字段定义](../../DATASET.md)*
