# ServiceNow/eva

⭐ 243 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/ServiceNow/eva) · [官网](https://servicenow.github.io/eva/) · 组织维护

**语音智能体端到端自动评测框架：同时评任务准确与对话体验**

ServiceNow 开源的会话语音智能体评测框架，以 bot-to-bot 架构全自动运行多轮语音对话并打分，无需人工听审。评测覆盖两个维度：EVA-A（任务是否正确完成）与 EVA-X（对话是否自然、简洁、适合语音场景）。内置 213 个企业场景（3 个领域）、12 个级联与音频原生系统的结果、可施加背景噪声/口音/连接退化的扰动套件，并提供 Streamlit 配置编辑器与结果分析应用。需配置多个 LLM/STT/TTS 提供商的 API key 方可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EVA-A/EVA-X 双维度评分，覆盖级联与 speech-to-speech 两类系统
- 213 个企业场景，针对语音特有失败模式
- 扰动套件：背景噪声、口音变体、连接退化模拟
- Streamlit 配置编辑器与结果可视化分析应用

## 适用场景

- 上线前对语音智能体做多轮对话自动化回归评测
- 用扰动套件测试嘈杂环境与口音下的表现
- 跨多个模型配置批量运行基准并对比结果
- 扩展支持新语言的文化适配评测数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **EVA** is an open-source evaluation framework for conversational voice agents that scores complete, multi-turn spo
> L16: Using a realistic **bot-to-bot architecture**, EVA runs fully automated evaluations without human listeners — end t
> L258: Existing benchmarks evaluate voice agent components in isolation — speech understanding, TTS quality, or conversat

## 星数曲线

```mermaid
xychart-beta
    title "ServiceNow/eva 星数(近 13 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-20", "2026-11-21", "2026-11-27"]
    y-axis "stars" 229 --> 244
    line [230, 231, 232, 233, 234, 230, 236, 239, 240, 241, 242, 243, 243]
```

2026-10-25 230 → 2026-11-27 243（+13）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `dc28e0eae35d` · [字段定义](../../DATASET.md)*
