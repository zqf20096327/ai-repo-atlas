# huggingface/rlhf-interface

⭐ 35 · Python · 推送 2026-09-24 · [GitHub](https://github.com/huggingface/rlhf-interface) · 组织维护

**面向 Amazon Mechanical Turk 的 RLHF 数据收集界面**

基于 Gradio 的 Hugging Face Space 应用，用于通过 Amazon Mechanical Turk 众包收集人类反馈（RLHF）标注数据。部署到自有 Space 后配置 HF_TOKEN、DATASET_REPO_URL 等密钥，新的 HIT 结果会自动推送到指定的 Hugging Face 数据集仓库；本地通过 python app.py 运行，配合 AWS 密钥与 mturk requestor 账户执行 python collect.py 发起收集。README 提示 Spaces 计算与内存资源有限，并发过多 HIT 或数据集过大会遇到问题。

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

- Gradio Space 形式部署，标注结果自动 force push 到 Hugging Face 数据集
- 集成 Amazon Mechanical Turk 发起众包 HIT
- 提供本地运行方式与 .env 本地开发配置建议

## 适用场景

- 通过 mturk 众包收集人类偏好反馈数据用于 RLHF 训练
- 构建自动归档到 Hub 的标注数据集流水线

## 场景标签

 · 领域:LLM 数据/标注工具

## 证据(README 行号)

> L10: An RLHF interface for data collection with Amazon Mechanical Turk and Gradio.
> L30:  When you run this space on mturk and when people visit your space on

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/rlhf-interface 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `448d90229025` · [字段定义](../../DATASET.md)*
