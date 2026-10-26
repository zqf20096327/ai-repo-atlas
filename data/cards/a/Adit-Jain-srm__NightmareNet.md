# Adit-Jain-srm/NightmareNet

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Adit-Jain-srm/NightmareNet) · [官网](https://frontend-aj5.vercel.app) · 个人维护

**对抗鲁棒性训练平台：Wake/Dream/Nightmare/Compress 循环强化模型**

面向 NLP 与视觉分类模型的对抗鲁棒性训练平台：以受睡眠记忆巩固启发的四阶段循环（Wake 监督微调、Dream 数据增强、Nightmare 课程式对抗训练、Compress 鲁棒蒸馏+剪枝）迭代产出更鲁棒的模型，学生模型进入下一轮循环。提供 pip 包与 CLI（distort/train/evaluate）、FastAPI 后端与 Next.js 前端的 Docker 部署、GitHub Action 鲁棒性门禁，以及签名的 EU AI Act 合规报告生成。自称非运行时护栏（Lakera）或评测库（TextAttack），而是训练范式加编排平台。开发目标硬件为 4GB VRAM 笔记本 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四阶段循环训练（监督微调→生成增强→对抗训练→鲁棒蒸馏+剪枝）
- 文本与视觉双管线（TextFooler 类攻击 / FGSM、PGD 像素扰动）
- CLI 提供 distort/train/evaluate 命令，SST-2 单 GPU 十分钟内跑通全循环
- 生成签名的 EU AI Act 合规报告与 robustness-check GitHub Action

## 适用场景

- 在发布前对 NLP/视觉分类模型做对抗鲁棒性强化训练
- 在 CI 中用鲁棒性阈值门禁 PR
- 为高风险 AI 系统生成 EU AI Act Article 15 合规报告
- 在不遗忘旧防御的前提下迭代积累模型鲁棒性

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L38: > NightmareNet is not a runtime guardrail (Lakera) or evaluation library (TextAttack). It is a **training paradigm*
> L63: pip install nightmarenet                              # core (CLI + library)
> L152: ## Running the API + Dashboard Locally (Docker)

## 星数曲线

```mermaid
xychart-beta
    title "Adit-Jain-srm/NightmareNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `63a73228be33` · [字段定义](../../DATASET.md)*
