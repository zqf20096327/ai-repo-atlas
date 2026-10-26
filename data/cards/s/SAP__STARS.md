# SAP/STARS

⭐ 46 · Python · Apache-2.0 · 推送 2026-08-23 · [GitHub](https://github.com/SAP/STARS) · 组织维护

**对 LLM 执行漏洞测试的 AI agent（SAP AI Core/HF/本地部署）**

SAP 维护的安全测试 agent：对来自 SAP AI Core、本地部署或 HuggingFace 的 LLM 执行漏洞测试，目标是识别并修正潜在安全漏洞。攻击手段覆盖 NLP 类（TextAttack）与 LLM 类（Promptmap、GPTFuzz、PyRIT、CodeAttack、ArtPrompt、Garak）。可通过聊天前端使用 Agent，或仅运行 backend 以 CLI 方式使用；架构为 backend-agent 加 Angular 前端两部分。具体安装步骤位于子目录文档中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 SAP AI Core、本地部署及 HuggingFace 模型执行漏洞测试
- 支持 7 种 LLM 攻击（Promptmap/GPTFuzz/PyRIT/CodeAttack/ArtPrompt/Garak）及 TextAttack
- 聊天前端与 CLI 两种使用方式

## 适用场景

- 上线前对 LLM 应用做安全漏洞扫描
- 用多种已知攻击方法测试模型的提示注入鲁棒性
- 对 SAP AI Core 或本地部署的模型做合规安全评估

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: STARS is a AI agent whose purpose is to conduct vulnerability tests on LLMs from SAP AI Core or from local deployme
> L14: Hereafter, a list with all the attacks the Agent is able to run, grouped by attack type.

## 星数曲线

```mermaid
xychart-beta
    title "SAP/STARS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3f74c20abc66` · [字段定义](../../DATASET.md)*
