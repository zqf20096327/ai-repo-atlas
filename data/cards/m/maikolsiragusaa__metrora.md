# maikolsiragusaa/metrora

⭐ 14 · TypeScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/maikolsiragusaa/metrora) · [官网](https://metrora.eu) · 个人维护

**本地优先的 AI 辅助开发控制中心：观测用量成本、对比模型、内嵌 OpenCode**

面向使用 AI 编程工具的开发者的桌面控制中心：通过 40 个本地采集器统一读取 Claude、Codex、Gemini、Cursor 等客户端与网关的用量、成本、会话与模型数据，不要求 AI 流量经过自有网关、不强制账户。证据分层标注 observed/metered/derived/estimated 等状态。内嵌上游 OpenCode 运行时与 Web UI 提供编码界面，并提供 CLI、本地 Web、Android 伴侣端与只读 MCP 服务器。Windows 经 Microsoft Store 分发，Android 上架 Google Play，也可用 Node.js 22.15+ 从源码构建。

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

- 40 个本地采集器覆盖主流 AI 编码客户端/CLI/编辑器/网关
- 证据分层（observed/metered/derived/estimated/partial 等）与可导出的用户数据
- 内嵌上游 OpenCode 运行时与 Web UI 作为 Code 界面
- CLI 覆盖 overview/sessions/models/compare/audit/export/bench/mcp 等命令

## 适用场景

- 统一查看分散在各编辑器和 CLI 中的 AI 用量与成本
- 并排对比不同模型的 token 与成本证据
- 在同一控制中心里配置预算、容量与项目范围
- 在桌面端内嵌的 OpenCode 环境中编码

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L42: - **Multi-tool, not single-provider.** Metrora currently registers **40 local collectors** across major AI coding c
> L45: - **One factual layer, many surfaces.** Desktop, CLI, local web, Android, MCP, Bench and Code integrations build on
> L104: |**Desktop**|Primary local control center for observation, comparison, Capacity and configuration|**Live on Micros

## 星数曲线

```mermaid
xychart-beta
    title "maikolsiragusaa/metrora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b458911cec2a` · [字段定义](../../DATASET.md)*
