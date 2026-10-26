# QuickButlerPace65/AnythingLLM-Desktop

⭐ 37 · 推送 2026-10-23 · [GitHub](https://github.com/QuickButlerPace65/AnythingLLM-Desktop) · 个人维护

**便携版一体化 AI 桌面应用：连接任意 LLM 与文档对话**

AnythingLLM Desktop 的便携 Windows 分支：打包为免安装的绿色版应用，解压后运行 Main.exe 即可使用，可放置于任意文件夹或 U 盘，不写入系统注册表。功能包括连接本地（Ollama、LM Studio、Llama.cpp 等）或云端（OpenAI、Anthropic、Groq 等）模型，通过内置向量库对 PDF/Word/TXT/网页进行 RAG 式文档对话，并支持按工作区隔离上下文。要求 Windows 系统，构建需 Node.js v18+ 与 Yarn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零安装便携运行：解压 zip 双击 Main.exe 启动，不写注册表
- 支持本地（Ollama/LM Studio/LocalAI/Llama.cpp）与云端（OpenAI/Anthropic/Groq 等）模型接入
- 内置 LanceDB 默认向量库，对 PDF/Word/TXT/网页自动向量化实现文档对话
- 多工作区隔离上下文，各配独立文档与系统提示词

## 适用场景

- 在 U 盘或任意文件夹免安装地使用本地 AI 文档问答工作区
- 切换本地与云端多种 LLM 进行私密对话
- 按项目划分工作区，分别挂载文档与提示词

## 场景标签

`文档问答` `聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L17: This is a customized, enhanced fork of the original AnythingLLM Desktop application, specifically optimized and pac
> L34: * 🔒 **100% Privacy by Default:** Run local models (via Ollama, LM Studio, etc.) and keep all your documents and cha
> L36: * 📚 **Enterprise-Grade RAG:** Drop in PDFs, Word docs, TXT files, or web links. The app automatically vectorizes th

## 星数曲线

```mermaid
xychart-beta
    title "QuickButlerPace65/AnythingLLM-Desktop 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-25 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `55e2afc68c6b` · [字段定义](../../DATASET.md)*
