# gvkhosla/pi-tinker

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/gvkhosla/pi-tinker) · [官网](https://www.npmjs.com/package/pi-tinker) · 个人维护

**在 Pi 内用 Tinker 微调开源模型的工具包，含托管训练流程**

Pi 编辑器的扩展包（pi-package），封装 Tinker 与 Tinker Cookbook 的微调工作流：读取 CSV/JSON/JSONL/Markdown 等数据生成分割好的训练与留出评估集、可编辑的 train_sft.py/eval.py 脚本，按 demo/smoke/small/real 四档预算运行基线评估、短训练与 checkpoint 对比，并在 checkpoint 胜过基线时才扩大训练。支持 In kling 与 Qwen、gpt-oss、Kimi 等 Tinker 提供的模型；不能上传 Tinker 未提供的 Hugging Face 模型。微调需 Python 3.11+、Tinker SDK 与 PyTorch，并提供供其他编码 agent（Claude Code/Cursor 等）使用的 CLI 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 托管 improve 循环：数据准备→smoke 测试→小训练→checkpoint 对比，胜过基线才扩大规模
- 生成可检视编辑的普通文件（train.jsonl/eval.jsonl/train_sft.py/eval.py）
- 注册 4 个 Inkling 模型变体（64K/256K 上下文），支持 reasoning effort 扫描与自动选档
- demo 档不调用 API；API 命令需确认，deploy 仅使用已批准的 checkpoint

## 适用场景

- 用 CSV/JSONL 客服问答等数据微调模型并对比效果
- 在 Pi 内按预算阶梯（demo→smoke→small→real）推进微调实验
- 让 Claude Code、Cursor 等编码 agent 通过 agent-cli 脚本执行同一微调流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: pi-tinker prepares your data, writes editable Python, runs small training jobs, and compares the trained checkpoint 
> L44: /tinker improve data.csv --goal "better customer support answers" --budget demo

## 星数曲线

```mermaid
xychart-beta
    title "gvkhosla/pi-tinker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5e6cfc7ecab5` · [字段定义](../../DATASET.md)*
