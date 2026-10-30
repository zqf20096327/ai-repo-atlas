# nwtgck/naidan

⭐ 42 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/nwtgck/naidan) · [官网](https://naidan.pages.dev/) · 个人维护

**浏览器内本地优先 AI 应用：隐私对话与端上模型运行**

隐私优先、本地优先的 Web AI 应用：可直接在浏览器内运行文本、图像、语音生成模型（GGUF 等），也可连接 OpenAI 兼容 API 与 Ollama 使用自有推理服务。提供四种运行方式：file:// 打开的 standalone HTML 包、自托管静态文件、独立服务器二进制、在线版。数据存于浏览器（OPFS/LocalStorage），支持对话分支树、跨标签页同步、URL 参数自动化与浏览器沙箱内的 Agent Shell。声明大部分代码由 GPT/Gemini/Claude 生成、人工审查较少。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 浏览器内端上运行文本/图像/语音生成模型，无需推理服务器
- 支持连接 OpenAI 兼容 API（vLLM/LM Studio/llama-server）与 Ollama
- file:// 直接运行，数据存浏览器，提供 CSP 收紧的 local-only 与 curated 托管版
- 对话分支树、跨标签页同步（Web Locks + BroadcastChannel）、URL 参数自动化

## 适用场景

- 不装桌面应用、不跑后端服务就在浏览器里用本地模型聊天
- 连接自己的 Ollama 或 OpenAI 兼容推理服务作为前端界面
- 通过书签/快捷方式用 URL 参数快速发起指定模型和提示词的对话

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: A privacy-focused, local-first AI app. Run models on your device, directly in your browser, or connect to OpenAI-com
> L113: - **On-Device AI**: Generate text, images, and speech on your device, directly in your browser. No inference serve
> L114: - **Broad Compatibility**: Connect to **OpenAI-compatible APIs** (such as vLLM, LM Studio, or llama-server) and **

## 星数曲线

```mermaid
xychart-beta
    title "nwtgck/naidan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `567b0da8b28a` · [字段定义](../../DATASET.md)*
