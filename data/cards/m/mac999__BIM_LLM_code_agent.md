# mac999/BIM_LLM_code_agent

⭐ 37 · Python · 推送 2026-05-19 · [GitHub](https://github.com/mac999/BIM_LLM_code_agent) · 个人维护 · 中文 README

**BIM/IFC 数据分析与代码生成的 LLM Agent，面向论文研究**

结合 BIM 与 LLM 的代码 Agent：接收自然语言查询，生成 Python 脚本对 IFC 等 BIM 文件进行提取、分析与可视化，支持 IFC/PDF/JSON/TXT/CSV 输入，基于 LangChain 构建多 Agent 管道，使用 Ollama 本地模型（codegemma/qwen2.5-coder/llama3/gemma3）与 OpenAI API key，提供 Streamlit 交互界面。README 自述存在幻觉与不完整代码生成等限制，且用于检验 LLM Agent 性能并发表论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言查询 BIM 数据并自动生成 Python 脚本
- 支持 IFC/PDF/JSON/TXT/CSV 多格式文件处理
- LangChain 多 Agent 管道结合向量检索（FAISS）
- Ollama 本地模型（codegemma/qwen2.5-coder/llama3/gemma3）与 Streamlit 界面

## 适用场景

- 用自然语言查询 IFC 模型中的房间、面积等数据
- 让 Agent 生成脚本完成 BIM 数据分析与图表输出
- 作为 LLM Agent 在复杂模型任务上的性能研究载体

## 场景标签

`代码生成` `数据分析` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: This is BIM (Building Information Modeling) LLM Code Agent for the purpose of checking LLM Agent Performance as the 
> L18: - **BIM Query Handling**: Processes natural language queries to extract or analyze BIM data.
> L19: - **Code Generation**: Automatically generates Python scripts to fulfill user commands.

## 星数曲线

```mermaid
xychart-beta
    title "mac999/BIM_LLM_code_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `900e4316ee4f` · [字段定义](../../DATASET.md)*
