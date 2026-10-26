# MiniMax-AI/MiniMax-M2.5

⭐ 587 · NOASSERTION · 推送 2026-03-09 · [GitHub](https://github.com/MiniMax-AI/MiniMax-M2.5) · 组织维护 · 中文 README

**面向编码与 agent 任务的 MiniMax M2.5 前沿模型发布仓库**

MiniMax 公司发布的 M2.5 系列基础模型仓库，含 M2.5 与 M2.5-Lightning 两个速度版本，主打编码（SWE-Bench Verified 80.2%）、搜索与工具调用、办公文档（Word/PowerPoint/Excel）等 agentic 任务场景。模型经数十万真实环境强化学习训练，推理速度为 100/50 tokens 每秒，API 定价按百万 token 计费并支持缓存。模型权重托管于 Hugging Face 与 ModelScope，已部署于 MiniMax Agent 产品。许可证为 Modified-MIT。README 未给出本地部署命令，需经 API 或下载权重使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个版本 M2.5 / M2.5-Lightning，能力相同、吞吐 50/100 tokens 每秒不同
- 在 SWE-Bench Verified 得分 80.2%，BrowseComp 76.3%（含上下文管理）
- 在真实环境强化学习训练，覆盖编码、搜索、工具调用、办公文档任务
- 已部署于 MiniMax Agent，含按文件类型加载的 Office Skills

## 适用场景

- 构建代码生成与软件工程 agent
- 执行搜索、工具调用等自主任务
- 办公场景产出 Word/PowerPoint/Excel 交付物

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L40: Today we're introducing our latest model, **MiniMax-M2.5**.
> L42: Extensively trained with reinforcement learning in hundreds of thousands of complex real-world environments, M2.5 i

## 星数曲线

```mermaid
xychart-beta
    title "MiniMax-AI/MiniMax-M2.5 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 586 --> 588
    line [587, 587]
```

2026-10-18 587 → 2026-10-26 587（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `a875e8e2eb99` · [字段定义](../../DATASET.md)*
