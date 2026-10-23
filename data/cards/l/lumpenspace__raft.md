# lumpenspace/raft

⭐ 176 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/lumpenspace/raft) · [官网](https://raft.hyperplex.org) · 个人维护

**从某人网络足迹微调对话人格模型的流水线工具**

RAFT（Retrieval-Augmented Fine-Tuning）提供从公开写作构建对话人格的完整流水线：`raft fetch` 从 LessWrong、X/Bluesky、Substack、RSS、PDF 等来源抓取对话与背景文档，prep 阶段分块嵌入并按日期过滤生成检索增强微调样本（含 thinking 模型推理链），train 阶段可送 OpenAI 微调 API 或本地 MPS/CUDA 训 LoRA/QLoRA，`raft comment` 用 MLX 或 OpenAI 兼容端点运行训练出的人格。作者声明该仓库曾一度放弃维护且不保证可用，README 主要以变更日志形式组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多来源抓取（LessWrong/X/Bluesky/Substack/RSS/URL/PDF）并区分对话与背景文档
- 检索只召回目标更早的写作，召回内容须逐句引用锚定
- 支持 thinking 模型推理链生成（`raft ft:gen --thinking`）
- 本地训练支持 Apple Silicon MPS 与 CUDA（QLoRA 仅 CUDA）

## 适用场景

- 用某人的公开帖子与文章训练其对话人格模型
- 构建基于个人语料的检索增强微调数据集
- 在本地 Mac 或 CUDA 机器上训练人格 LoRA 并通过 `raft comment` 对话

## 场景标签

`微调` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L48: The first release on PyPI since 2.6 (`pip install -U raft-ft`), so it also
> L135: **Training on your own Mac (or CUDA box).** `raft ft:run --model <org/name>
> L191: 2. **prep** — chunk + embed, then generate the finetune examples. Retrieval

## 星数曲线

```mermaid
xychart-beta
    title "lumpenspace/raft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 175 --> 177
    line [176, 176]
```

2026-10-18 176 → 2026-10-23 176（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `025826bffab5` · [字段定义](../../DATASET.md)*
