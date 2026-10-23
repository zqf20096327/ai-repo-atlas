# rajudandigam/agent-inspect

⭐ 165 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/rajudandigam/agent-inspect) · [官网](https://agentinspect.vercel.app) · 个人维护

**TypeScript AI agent 的本地轨迹调试与 CI 轨迹断言工具包**

面向 TypeScript AI agent 开发者的本地优先调试与测试工具集：将 agent 运行记录为本地 JSONL 轨迹，提供执行树查看、确定性轨迹检查（可接入 CI，规则失败即退出非零码）、以及离线 Evidence v2 打包与哈希校验。默认仅采集元数据、写入时脱敏、无需账号或上传。通过官方适配器支持 LangChain/LangGraph、AI SDK、OpenAI Agents JS，另有 Vitest/Jest 报告器与可选 MCP server（Preview）。18 个包组成的 npm 包家族，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 JSONL 轨迹的执行树查看（嵌套步骤/工具调用/LLM 调用/错误）
- 确定性、provider 无关的轨迹检查，可作为 CI 门禁
- Evidence v2 离线打包、脱敏与文件哈希校验
- 提供 LangChain/AI SDK/OpenAI Agents/Vitest/Jest 等官方适配包

## 适用场景

- 在 CI 中捕获 agent 走错工具路径的回归
- 本地调试一次 agent 运行并定位首个因果失败
- 生成脱敏、可校验的离线证据附件用于 PR 或事故复盘

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L35: Agent code rarely fails as one function call. It plans, retrieves, calls tools, invokes a model, retries, and produ
> L57: Checks are deterministic and provider-free: the same trace and rules produce the same result. Start with a preset, 
> L104: |Stack|Install / command|Start|

## 星数曲线

```mermaid
xychart-beta
    title "rajudandigam/agent-inspect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 164 --> 166
    line [165, 165]
```

2026-10-18 165 → 2026-10-23 165（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f6b18948030e` · [字段定义](../../DATASET.md)*
