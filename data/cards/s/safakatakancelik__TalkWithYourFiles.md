# safakatakancelik/TalkWithYourFiles

⭐ 94 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/safakatakancelik/TalkWithYourFiles) · 个人维护

**上传文档并提问的开源 RAG 问答应用**

基于 LangChain 与 Streamlit 的图形界面应用：加载 PDF、DOCX、TXT、CSV 文件后提问，可把问答结果并入聊天对话，并支持调整 QA 链参数与查看上下文窗口用量。模型通过 Anthropic（Claude）或 OpenRouter 接入；有 OpenRouter key 时用 embeddings 检索相关片段，仅有 Anthropic key 时退回 BM25 关键词检索。提供 git clone + pip 与 Docker 两种安装方式，GUI 框架可替换（FlowCoordinator 不依赖 Streamlit）。此版本为向 2023 年原版（v1.0.0）致敬的重制，作者称后续方向在考虑中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 PDF/DOCX/TXT/CSV 问答并可并入聊天对话
- Anthropic 与 OpenRouter 双通道，模型名可在侧边栏任意填写
- 有 embeddings API 时用向量检索，仅有 Anthropic key 时用 BM25
- FlowCoordinator 与 Streamlit 解耦，可换 GUI 框架

## 适用场景

- 上传本地文档直接提问获取答案
- 在聊天对话中引用文件内容持续问答
- 调整 QA 链参数并观察上下文窗口消耗

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: Talk-With-Your-Files is an open source GUI (Graphical User Interface) application powered by LLMs (Large Language Mo
> L28: - **Anthropic** (Claude) or **OpenRouter** (GPT, Gemini, Llama, Claude and many more). Pick one in the sidebar and 

## 星数曲线

```mermaid
xychart-beta
    title "safakatakancelik/TalkWithYourFiles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-28 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6127dc26d40b` · [字段定义](../../DATASET.md)*
