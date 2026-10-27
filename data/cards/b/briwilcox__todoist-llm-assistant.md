# briwilcox/todoist-llm-assistant

⭐ 22 · Python · MIT · 推送 2026-06-14 · [GitHub](https://github.com/briwilcox/todoist-llm-assistant) · 个人维护

**为 Todoist 任务生成 AI 完成建议的命令行工具**

连接 Todoist API 与 OpenAI API 的 Python 命令行工具：读取用户的 Todoist 任务，为每个任务调用 LLM 生成分步完成建议，并将建议写入任务描述。支持项目级模型配置、交互模式（审查建议、反馈精炼、按需切换模型）、批量处理与失败时回退到 gpt-4o-mini。当前仅支持 OpenAI 模型（o 系列、gpt-4o 系列等），使用产生 API 费用；工具会直接修改 Todoist 任务数据。通过 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为每个 Todoist 任务生成 AI 分步建议并写入任务描述
- 支持项目级模型选择与命令行 --model 覆盖
- 交互模式含反馈循环与模型升级切换
- o 系列模型出错时可 --fallback 回退到 gpt-4o-mini

## 适用场景

- 为积压的 Todoist 任务批量生成可执行的完成步骤
- 在交互模式中反馈并精炼 AI 建议
- 按项目配置不同模型以平衡成本与输出质量

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: An AI assistant for your Todoist tasks.
> L198: 3. For each task, it asks the AI to generate a suggestion on how to accomplish it

## 星数曲线

```mermaid
xychart-beta
    title "briwilcox/todoist-llm-assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `358a893bec4d` · [字段定义](../../DATASET.md)*
