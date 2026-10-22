# ServiceNow/eva

⭐ 231 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/ServiceNow/eva) · [官网](https://servicenow.github.io/eva/) · 组织维护

**给语音 Agent 开发者与研究者：端到端评测多轮语音对话的开源框架**

EVA 是 ServiceNow 开源的对话式语音 Agent 评测框架：用 bot-to-bot 架构全自动运行多轮语音对话，从语音输入到评判输出，无需人类听者。评分覆盖两个维度——EVA-A（任务完成、语音保真度、忠实度）与 EVA-X（简洁度、轮次切换、延迟、进展）。内置 213 个企业场景（3 个领域）、12 个级联与音频原生系统的结果，以及背景噪声、口音、连接劣化等扰动套件。依赖外部 API key（OpenAI、ElevenLabs、Cartesia、Vertex AI、Bedrock）驱动评判与用户模拟器；OpenAI Realtime 通话器为 beta。提供 CLI、Streamlit 配置编辑器与分析应用、Docker 支持、多语言扩展脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- bot-to-bot 架构全自动评测完整多轮语音对话，无需人类听者
- EVA-A/EVA-X 双维度指标：任务完成、忠实度、简洁度、轮次切换、延迟等
- 213 个企业场景（3 领域）+ 噪声/口音/连接劣化扰动套件
- Streamlit 配置编辑器与分析应用，Docker 与多语言（WER 归一化）扩展

## 适用场景

- 对级联或音频原生语音 Agent 做端到端质量评测
- 在噪声、口音、连接劣化等真实音频条件下压测语音 Agent
- 横向对比多个语音 Agent 系统并可视化结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **EVA** is an open-source evaluation framework for conversational voice agents that scores complete, multi-turn spo
> L16: Using a realistic **bot-to-bot architecture**, EVA runs fully automated evaluations without human listeners — end t

## 星数曲线

```mermaid
xychart-beta
    title "ServiceNow/eva 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 228 --> 232
    line [229, 230, 231]
```

2026-10-18 229 → 2026-10-22 231（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `db910cf2a081` · [字段定义](../../DATASET.md)*
