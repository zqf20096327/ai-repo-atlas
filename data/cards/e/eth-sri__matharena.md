# eth-sri/matharena

⭐ 293 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/eth-sri/matharena) · [官网](https://matharena.ai) · 组织维护 · 中文 README

**在最新数学竞赛上评测 LLM 的平台（NeurIPS D&B '25）**

苏黎世联邦理工学院 SRI 维护的 LLM 数学能力评测平台（matharena.ai 后端代码）：以最新数学竞赛与奥赛题为评测集，通过 YAML 配置文件指定模型与竞赛，运行评测脚本产出答案并可用本地 Web 服务器查看完整推理轨迹；支持 xAI/OpenAI/Anthropic/DeepSeek/OpenRouter/GLM 等 API 提供商及 vllm 本地运行，部分证明类赛题需 judge 脚本或人工评分，ArXivLean 等竞赛支持 codex/claude 等 harness 在 Docker/Podman 中运行。依赖 UV 或 conda 安装，评测日志发布于 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以最新数学竞赛/奥赛（AIME、IMO、Putnam 等）为评测集
- YAML 配置添加模型，支持十余家 API 提供商与 vllm 本地运行
- 本地 Web 界面查看最终答案与完整模型交互/Agent 步骤
- 支持 Docker/Podman 容器化 harness 运行与 LLM judge 评分

## 适用场景

- 把我的模型在最新数学竞赛上跑分并与榜单对比
- 复现 MathArena 网站上的评测结果
- 为新数学竞赛构建可复现的 LLM 评测流程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: MathArena (NeurIPS D&B '25) is a platform for evaluation of LLMs on latest math competitions and olympiads. It is h
> L146:  - `api`: API provider. The API key should be defined as an environment variable when using the specified API. The

## 星数曲线

```mermaid
xychart-beta
    title "eth-sri/matharena 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 291 --> 294
    line [292, 293, 293]
```

2026-10-18 292 → 2026-10-26 293（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `821c970ebfee` · [字段定义](../../DATASET.md)*
