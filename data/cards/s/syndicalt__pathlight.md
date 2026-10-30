# syndicalt/pathlight

⭐ 25 · TypeScript · 推送 2026-05-01 · [GitHub](https://github.com/syndicalt/pathlight) · 组织维护

**给 AI agent 开发者的可视化调试与执行追踪观测平台**

自托管的 AI agent 可观测性工具：通过 SDK/Python 包/OpenTelemetry 采集 agent 执行 trace，在 Next.js 仪表盘以瀑布时间线展示每个 span 的输入输出、耗时与源码位置。支持 trace 双列对比、按 commit SHA 聚合标记成本/延迟回归、LLM span 在线编辑消息后真实重放、运行中断点暂停与状态编辑、eval 断言接入 CI，以及 BYOK LLM 读取失败 trace 生成修复 diff。Docker Compose 一条命令部署，数据存 SQLite named volume。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 瀑布时间线 + span 检查器展示输入/输出/源码位置/token 数
- LLM span 编辑消息后针对真实 provider 重放
- SDK 自动捕获 commit SHA，/commits 页标记 ≥25% 成本/延迟回归
- 断点暂停 agent、在线编辑 JSON 状态后继续执行

## 适用场景

- 定位多步 agent 工作流中某一步的决策与耗时问题
- 对比 prompt 修改前后两次运行的差异
- 在 CI 中用 trace 断言拦截成本/延迟回归
- 让 LLM 读取失败 trace 与源码生成修复补丁

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Visual debugging, execution traces, and observability for AI agents.
> L31: |**OpenTelemetry interop**|Collector accepts OTLP/HTTP; any OTel-instrumented app can ship to Pathlight|docs/opente
> L33: |**One-command deploy**|`docker compose up -d` pulls prebuilt images from GHCR; SQLite persists in a named volume|d

## 星数曲线

```mermaid
xychart-beta
    title "syndicalt/pathlight 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [26, 25, 25]
```

2026-10-18 26 → 2026-10-30 25（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `56779222fa8a` · [字段定义](../../DATASET.md)*
