# kekePower/museweb

⭐ 32 · Go · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/kekePower/museweb) · 个人维护

**用 LLM 把纯文本 prompt 流式生成为可路由网页的自托管服务器**

Go 编写的实验性 prompt 驱动 Web 服务器：将目录下每个 .txt prompt 作为一个可路由页面，请求时调用 LLM（流式输出 HTML 并做代码围栏/Markdown 产物清洗），prompt 文件修改后实时生效。兼容任意 OpenAI 兼容 API 端点，默认后端为本地 Ollama，也可切换 OpenAI、Groq、OpenRouter、vLLM、LM Studio 等。支持推理模型（DeepSeek、Qwen 等）自动检测、config.yaml 与 CLI 参数配置、prompt 级静态资源目录。编译为约 7MB 单一静态二进制，无外部运行时；作者自述为概念验证，处于早期状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每个 .txt prompt 映射为一个可路由页面，编辑即生效无需重启
- HTML 逐 token 流式输出并带实时净化（代码围栏/Markdown 产物清理）
- 兼容任意 OpenAI 兼容端点，默认本地 Ollama，支持 vLLM/LM Studio 等
- Go 单一静态二进制（约 7MB），无外部运行时依赖

## 适用场景

- 用自然语言 prompt 搭建完全自托管的极简网站
- 本地 Ollama 模型离线生成并发布网页内容
- 实验 prompt 驱动网站的可行性与形态

## 场景标签

 · 领域:Web 服务器/AI 生成内容

## 证据(README 行号)

> L3: MuseWeb is an **experimental, prompt-driven web server** that streams HTML straight from plain-text prompts using a 
> L9: * **Prompt → Page** – Point MuseWeb to a folder of `.txt` prompts; each prompt becomes a routable page.
> L11: * **Streaming Responses** – HTML is streamed token-by-token for instant first paint with real-time sanitization.

## 星数曲线

```mermaid
xychart-beta
    title "kekePower/museweb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f2fda891eb7a` · [字段定义](../../DATASET.md)*
