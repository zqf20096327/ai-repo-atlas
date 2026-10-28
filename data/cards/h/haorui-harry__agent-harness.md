# haorui-harry/agent-harness

⭐ 29 · Python · 推送 2026-04-13 · [GitHub](https://github.com/haorui-harry/agent-harness) · 个人维护 · 中文 README

**通用 agent 运行时：把开放任务转为交付物+证据与可审计产物**

基于持久线程的通用 agent 运行时：以能力规划器按任务选择技能、工具与工作区动作，在真实工作区内执行任务图，输出主交付物（研究报告/架构设计/对比矩阵等）及证据包、执行轨迹等可审阅产物。证据管道按 Tavily→公共搜索(DuckDuckGo/SearXNG)→live_search→静态目录的优先级取材；配置 live 模型后启用分析-综合-批评-修订四阶段推理链。以 Python 库与 CLI 形式提供，支持无 API Key 模式，含 183 个测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 持久线程 + 工作区 + 可恢复执行与事件流导出
- 多后端证据管道（Tavily/DuckDuckGo/SearXNG/live_search/静态目录）
- 四阶段推理链：分析→综合→批评→修订
- 技能互操作目录导出，兼容 OpenAI/Anthropic 风格生态

## 适用场景

- 把开放式请求自动产出研究报告或架构设计等可交付成果
- 需要每条结论带证据包与执行轨迹以便审阅的任务
- 无 API Key 环境下用公共搜索回退做证据优先综合

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6:  A high-performance, general-purpose agent runtime: plans with capabilities, uses skills and tools on demand, runs i
> L48: Request -> Thread -> Capability Planner -> Skills/Tools/Workspace Actions -> Main Deliverable -> Evidence + Artifac
> L162: from app.harness.engine import HarnessEngine

## 星数曲线

```mermaid
xychart-beta
    title "haorui-harry/agent-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c2e2e092f753` · [字段定义](../../DATASET.md)*
