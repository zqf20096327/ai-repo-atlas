# FAI-Solutions/open-webui-extensions

⭐ 18 · MIT · 推送 2026-10-17 · [GitHub](https://github.com/FAI-Solutions/open-webui-extensions) · 组织维护

**Open WebUI 的过滤器/管道扩展集合：LLM 流程可视化与用量监控**

面向 Open WebUI 的扩展仓库，当前包含两个过滤器扩展：LLMTrace 逐步可视化 LLM 收到用户查询后的工作流程（提供紧凑时间线与详细仪表盘两种输出）；Ollama Usage Monitor 在每条 LLM 回复顶部显示 Ollama Cloud 的会话与每周用量统计，包括距重置的剩余时间与已用模型。两者均可从 Open WebUI Marketplace 或 GitHub 安装。仓库自述为早期阶段，计划随关注度增加发布更多扩展。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLMTrace 以时间线/仪表盘两种形式展示 LLM 工作流各步骤
- Ollama Usage Monitor 在回复顶部显示 Ollama Cloud 会话与每周用量、重置倒计时
- 支持从 Open WebUI Marketplace 或 GitHub 直接安装

## 适用场景

- 排查 Open WebUI 中 LLM 处理流程各环节
- 跟踪 Ollama Cloud 订阅的会话/每周用量与重置时间
- 为自托管 Open WebUI 补充实用过滤器功能

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **Practical filter, function, pipeline, and tool extensions for Open WebUI**, solving everyday usability and functio
> L18: LLMTrace is an Open WebUI filter extension that gives insights into the LLMs workflow. It show each step that happe

## 星数曲线

```mermaid
xychart-beta
    title "FAI-Solutions/open-webui-extensions 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `56c943f8b75c` · [字段定义](../../DATASET.md)*
