# benttega/ovo-local-llm

⭐ 106 · TypeScript · MIT · 推送 2026-04-22 · [GitHub](https://github.com/benttega/ovo-local-llm) · [官网](https://ovoment.com) · 个人维护 · 中文 README

**Apple Silicon 本地 LLM 桌面应用：聊天/编码 Agent/图像生成**

面向 macOS（Apple Silicon，M1–M4）的本地 LLM 桌面应用：内置 MLX 原生运行时与 Ollama/OpenAI 兼容 API 端口，零 API key。功能包括 Chat（流式、语音、文件附件）、带 Monaco 编辑器与 Agent Chat 的 Code IDE（文件读写/搜索/执行工具、MCP 集成）、diffusers 本地文生图、BM25+语义搜索的 Wiki 知识库、LoRA 微调与模型混合。自动识别 HuggingFace/LM Studio 已有缓存模型，按 RAM/GPU 评分模型适配度。限制：不支持 Intel Mac，16GB 内存仅能跑 7B Q4 模型。以 DMG 安装包分发，构建未签名需运行清除 quarantine 的脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MLX 原生本地推理 + Ollama(11435)/OpenAI(11436)/原生(11437) 三种 API 兼容端口
- Code IDE：文件读写/搜索/执行工具 + MCP 服务器集成的 Agent Chat
- PPTX/HWP 文档解析、OCR、RAG 知识库自动注入
- LoRA 微调全流程与 SLERP/TIES/DARE 模型混合
- 按 RAM/GPU/上下文余量为模型评分的 Hardware Fit

## 适用场景

- 在 Mac 上离线运行开源 LLM 进行聊天和编码，不把数据发送到云端
- 用本地模型替代云端服务做代码 Agent 交互
- 管理 HuggingFace 本地缓存模型并挑选适配内存的模型
- 作为本机 Ollama/OpenAI 兼容端点供 Open WebUI 等客户端接入

## 场景标签

`聊天机器人` `编码 Agent` `图像生成` `RAG` · 领域:编码与开发

## 证据(README 行号)

> L12:  🦉 A private Claude-Code-style coding agent for Apple Silicon
> L15:  MLX-native. Ollama/OpenAI API compatible. Zero API keys.
> L41: Monaco editor + file explorer + Git panel + PTY terminal + AI inline completion. The Agent Chat on the right gets f

## 星数曲线

```mermaid
xychart-beta
    title "benttega/ovo-local-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-28 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `62a6ee2262f4` · [字段定义](../../DATASET.md)*
