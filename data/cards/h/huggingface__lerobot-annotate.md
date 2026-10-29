# huggingface/lerobot-annotate

⭐ 45 · Python · 推送 2026-01-29 · [GitHub](https://github.com/huggingface/lerobot-annotate) · 组织维护

**为 LeRobot 数据集添加子任务与对话标注的 Web 界面**

Hugging Face 维护的轻量级 Web 标注工具：连接本地或 Hub 上的任意 LeRobot 数据集，在视频回放中为 episode 添加子任务片段（起止时间戳与标签）和高层对话片段（用户提示+机器人响应及技能/场景标签），保存后导出更新后的 parquet 文件（subtasks.parquet、tasks_high_level.parquet 及 chunk 数据中的标注列），可直接用于训练。标注状态存于 JSON 以便续作。可本地以 uvicorn 运行，也可通过 Dockerfile 部署到 HF Spaces。

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

- 子任务片段标注（起止时间戳+标签）与高层对话片段标注
- 导出更新后的 parquet 文件与数据集元数据，可直接用于训练
- 标注状态保存至 JSON 支持续作
- 支持本地与 Hugging Face Hub 数据集，Hub 数据按需加载视频

## 适用场景

- 为机器人学习数据集标注子任务划分
- 为 LeRobot 数据集添加 prompt/response 形式的对话标注
- 在 HF Spaces 上部署团队共享的标注环境

## 场景标签

 · 领域:机器人学习/数据标注

## 证据(README 行号)

> L3: A lightweight web UI for annotating LeRobot datasets with subtask segments and high-level dialogue. It works with an
> L35: 6. **Export** to write parquet updates and dataset metadata.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/lerobot-annotate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `beffbd87ea71` · [字段定义](../../DATASET.md)*
