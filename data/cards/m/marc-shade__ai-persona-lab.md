# marc-shade/ai-persona-lab

⭐ 14 · TypeScript · MIT · 推送 2026-02-22 · [GitHub](https://github.com/marc-shade/ai-persona-lab) · 个人维护

**基于 Ollama 的多 AI 人格创建与群聊应用**

Streamlit 构建的 Web 应用：通过本地 Ollama 服务创建具有不同背景、性格与技能的 AI 人格，为每个人格配置不同模型（mistral、llama2 等）、温度与 token 参数，并支持多个人格同时参与的群聊。内含 ICL 系统：基于 sentence-transformers 的持久记忆、NetworkX 知识图谱、置信度评分与提示模板优化，可通过 config/icl_config.json 调整。需要 Python 3.8+ 与本地运行的 Ollama 服务，数据存于 data/personas.json。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 AI 人格创建与管理，每人格可配置不同 Ollama 模型与参数
- 多人格同时参与的交互式群聊
- ICL 系统：持久嵌入记忆、知识图谱、置信度回退
- 人格数据自动持久化到 personas.json

## 适用场景

- 创建多个不同性格的 AI 角色进行群聊互动
- 在本地 Ollama 上试验多 agent 对话与记忆机制
- 为不同人格配置不同模型对比对话表现

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3:  A powerful AI-driven application for creating and managing dynamic personas, enabling interactive group chats with 
> L10: - **Interactive Group Chat**: Engage in conversations with multiple AI personas simultaneously
> L51:    streamlit run app.py

## 星数曲线

```mermaid
xychart-beta
    title "marc-shade/ai-persona-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `452da7e89a30` · [字段定义](../../DATASET.md)*
