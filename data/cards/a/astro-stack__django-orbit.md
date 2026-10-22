# astro-stack/django-orbit

⭐ 180 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/astro-stack/django-orbit) · [官网](https://labs.wearehik.com/django-orbit) · 组织维护

**面向 AI agent 的 Django 运行时证据记录与调试工具**

Django 中间件/应用，捕获 HTTP 请求、SQL、慢查询与 N+1 候选、日志异常、缓存、后台任务及 LLM 调用元数据，按 family_hash 关联成有界上下文。人类通过 /orbit/ 仪表盘查看，编码 agent 通过本地 stdio 只读 MCP 服务器查询脱敏证据，配合 build_debug_brief、propose_fix_hypotheses 等 8 个工具完成排查；agent 不自动改代码。受 Django Debug Toolbar、Laravel Telescope 启发但不注入宿主 UI。MIT 许可，另有规划中的 Orbit Pro 自托管层（尚未发布）。

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

- 捕获请求/SQL/异常/任务/LLM 元数据并按 family_hash 关联
- 本地只读 MCP 服务器，敏感键脱敏、结果有界、默认不捕获提示词与补全内容
- 8 个调查工具：匹配工单证据、排序修复假设、生成回归测试计划
- 自带 /orbit/ 仪表盘与含预设场景的 demo 项目

## 适用场景

- Django 应用出现线上问题后，让编码 agent 基于运行时证据定位根因
- 在仪表盘中按请求族查看关联的 SQL、日志与异常
- 调试前生成脱敏的事件包供团队或 agent 使用

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **AI agent-native runtime evidence and debugging for Django.**
> L10: Orbit has its own dashboard at <code>/orbit/</code> and a read-only MCP server. It does not
> L104: Orbit's MCP server runs locally over stdio. It reads Orbit evidence and does
> L197: - AI/LLM metadata such as provider, model, tokens, latency, errors and tool

## 星数曲线

```mermaid
xychart-beta
    title "astro-stack/django-orbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-22 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2cd8983e0170` · [字段定义](../../DATASET.md)*
