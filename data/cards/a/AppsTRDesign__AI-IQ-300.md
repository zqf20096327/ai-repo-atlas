# AppsTRDesign/AI-IQ-300

⭐ 4 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/AppsTRDesign/AI-IQ-300) · [官网](https://wplugins.shop) · 个人维护

**本地与云端 LLM 的自主开发与自动化命令中心**

运行在本地计算机上的软件开发与自动化平台，提供类 ChatGPT 的聊天界面，背后由多角色 Agent（Planner/Coder/Debugger/Tester）驱动：按目标创建文件与文件夹、运行 PowerShell/CMD/Python/Node/PHP 命令、调试错误、在真实浏览器中测试并截图验证。支持 31 个模型提供商、原生 function calling 与 Qwen-XML/Hermes/Mistral 工具格式的通用解析、上下文压缩、MCP 客户端、多模型并行 Agent 团队，以及 Word/Excel/PDF/PPTX 文档生成。数据默认不离开本机，除非用户选择云提供商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 31 个提供商：Ollama、LM Studio、OpenAI、Anthropic、Gemini 等
- 通用工具解析器识别 Qwen-XML、Hermes-JSON、Mistral 工具格式
- MCP 客户端接入 stdio/HTTP 服务器（GitHub、PostgreSQL、文件系统、浏览器）
- 多 Agent 团队并行/分阶段分工，成员间消息与共享任务板

## 适用场景

- 用一句话让 Agent 分步生成并测试完整的 Web 项目
- 本地模型离线环境下执行自动化开发与运维任务
- 生成 Word/Excel/PDF/PPT 文档并即时预览
- 多模型池配额耗尽时自动切换继续长任务

## 场景标签

`多智能体` `编码 Agent` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L98: - **Real tool use:** Native function calling for Ollama, OpenAI-compatible APIs and Anthropic. A universal parser a
> L116: - **31 providers:** Ollama, LM Studio, OpenAI, Anthropic, Gemini, OpenRouter, Groq, NVIDIA NIM, Cloudflare Workers

## 星数曲线

```mermaid
xychart-beta
    title "AppsTRDesign/AI-IQ-300 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-20", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 low · 依据 README sha `64cb5d58016e` · [字段定义](../../DATASET.md)*
