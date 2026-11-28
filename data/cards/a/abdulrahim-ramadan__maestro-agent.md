# abdulrahim-ramadan/maestro-agent

⭐ 3 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/abdulrahim-ramadan/maestro-agent) · 个人维护

**工厂故障日志转班次交接报告的个人学习型 AI agent**

面向工业 4.0 场景的 CLI/Web 应用：读取生产班次故障日志 CSV，计算每台机器的停机时间与可用率；错误码从 JSON 字典精确查找，维修手册按标题分块后在 ChromaDB 做语义检索（RAG），引用手册条目生成德/英双语 Markdown 报告。数字均由 Python 工具计算、模型仅复制，Prompt 禁止自行算术并有测试校验；每次运行输出 JSON trace，带步数上限。数据全部为脚本生成的合成数据，作者声明为个人学习项目、非商业用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 错误码精确字典查询 + 手册标题分块的 RAG 混合检索
- 所有数字由 Python 工具计算，模型禁止自行算术并有测试校验
- 每次运行输出含每步工具调用的 JSON trace，失败工具不中断运行
- 德/英双语 CLI 与 Streamlit 界面，流式展示 agent 步骤

## 适用场景

- 把班次故障日志整理成可交接的维保报告
- 查询机器错误码对应的维修手册步骤
- 学习 agent 工具调用与 RAG 的工程实践

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5:  An AI agent that reads machine fault logs, searches maintenance manuals and writes a verified shift report in Engli
> L40: |ChromaDB|Embedded, persistent vector store with local default embeddings; no server to run.|
> L38: |OpenAI Python SDK|One client for any OpenAI-compatible API; the provider is a `.env` setting.|

## 星数曲线

```mermaid
xychart-beta
    title "abdulrahim-ramadan/maestro-agent 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a3cdc4b0f968` · [字段定义](../../DATASET.md)*
