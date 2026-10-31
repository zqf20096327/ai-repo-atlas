# taskvanguard/taskvanguard

⭐ 45 · Go · AGPL-3.0 · 推送 2026-02-07 · [GitHub](https://github.com/taskvanguard/taskvanguard) · 个人维护

**TaskWarrior 的 LLM 增强命令行包装器**

用 Go 编写的 CLI 工具，包裹 TaskWarrior 命令并通过任意 OpenAI 兼容 LLM API（OpenAI、DeepSeek、OpenRouter 等）增强任务管理：添加任务时建议改进标题/标签/注释，识别下一步最该做的任务（结合心情与情境），生成目标路线图，批量重构任务积压并建议拆分子任务。目标以普通 TaskWarrior 任务形式存于专用项目并通过 UDA 关联。面向 TaskWarrior 用户，尤其 ADHD 相关拖延场景。需预装 TaskWarrior 与 Go 1.21+，配置 API key，支持 AUR、go install 或源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- vanguard add 在创建任务时用 LLM 建议改进标题、标签、注释与子任务拆分
- vanguard spot 基于紧急度、情境与心情推荐下一个任务
- 目标管理：任务与长期目标通过 UDA 关联并自动追踪关系
- 支持任意 OpenAI 兼容 API，可按标签/项目黑名单阻止任务发送到 API

## 适用场景

- 在 TaskWarrior 工作流中获得 AI 建议的标签、注释与子任务拆分
- 不知道先做什么时让工具推荐下一个最有影响的任务
- 把模糊的大任务拆成可执行步骤并关联长期目标

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: **TaskVanguard** is a lightweight, fast, highly configurable CLI wrapper for TaskWarrior, written in Go. It brings A
> L24: Use `vanguard add <task>` just like `taskwarrior add <task>`. TaskVanguard creates the task, then suggests improvem

## 星数曲线

```mermaid
xychart-beta
    title "taskvanguard/taskvanguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c986cf9b114f` · [字段定义](../../DATASET.md)*
