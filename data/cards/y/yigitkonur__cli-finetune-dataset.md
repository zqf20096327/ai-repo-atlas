# yigitkonur/cli-finetune-dataset

⭐ 17 · Python · 推送 2026-02-21 · [GitHub](https://github.com/yigitkonur/cli-finetune-dataset) · 个人维护

**构建类别加权平衡的 LLM 微调数据集的 Python CLI**

面向 LLM 微调数据准备的 Python 脚本工具：读取目录下的 OpenAI chat 格式 JSONL 对话文件，以首条 assistant 消息内容作为类别标签，按 config.ini 中可配置的权重对各类别采样（不足时可放回过采样），输出单个打乱后的 JSONL 数据集。附带评估脚本统计输出中类别分布并以终端表格展示。由两个脚本构成，依赖仅 pandas（评估需 rich）。

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

- 线程池并发读取 JSONL 文件
- 按权重采样，源数据不足时放回过采样
- 以首条 assistant 消息内容作为类别标签
- 评估脚本统计类别分布并渲染终端表格

## 适用场景

- 把多类别对话数据合并为可控比例的微调数据集
- 检查微调数据集的类别分布是否符合预期权重

## 场景标签

 · 领域:机器学习/数据准备

## 证据(README 行号)

> L1: weighted, category-balanced dataset builder for LLM fine-tuning. takes a directory of JSONL conversation files, samp
> L14: you have a pile of JSONL files with OpenAI chat-format conversations, split across categories. you want a single fi

## 星数曲线

```mermaid
xychart-beta
    title "yigitkonur/cli-finetune-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `1a41ed82ede0` · [字段定义](../../DATASET.md)*
