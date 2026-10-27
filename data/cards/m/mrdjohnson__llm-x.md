# mrdjohnson/llm-x

⭐ 297 · TypeScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/mrdjohnson/llm-x) · [官网](https://mrdjohnson.github.io/llm-x/) · 个人维护

**本地 LLM 的网页/浏览器扩展聊天 UI，可离线运行**

面向本地运行大模型的用户的 ChatGPT 风格聊天界面，以 PWA 网页应用与 Chrome 扩展两种形式提供。支持连接 Ollama、llmman、LM Studio、OpenAI 服务器、Gemini Nano 及 AUTOMATIC1111 等多个后端，可同时连接多服务器、多模型对话，并支持文本生成图像与多模态图像理解。所有数据存于本地 IndexedDB，不发起外部 API 调用，可完全离线使用。可通过 GitHub Pages 直接访问、源码构建或 Docker 运行。限制：连接非 localhost 服务器需 HTTPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Ollama/llmman/LM Studio/OpenAI 服务器/Gemini Nano/AUTOMATIC1111 多后端连接
- 多模型同时对话与文本生成图像（Ollama/A1111）
- 数据存 IndexedDB，无外部 API 调用，PWA 支持完全离线
- 提供 Web 应用与 Chrome 扩展两种形式

## 适用场景

- 给本地 Ollama/LM Studio 模型一个可离线使用的聊天界面
- 同时连接多个本地服务器对比模型回答
- 本地进行文本生成图像与图像理解对话

## 场景标签

`聊天机器人` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L178: ChatGPT style UI for the niche group of folks who run Ollama (think of this like an offline chat gpt server) local
> L111: - [x] **Ollama integration!**

## 星数曲线

```mermaid
xychart-beta
    title "mrdjohnson/llm-x 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 296 --> 298
    line [297, 297]
```

2026-10-18 297 → 2026-10-27 297（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `66b9a28ef3d0` · [字段定义](../../DATASET.md)*
