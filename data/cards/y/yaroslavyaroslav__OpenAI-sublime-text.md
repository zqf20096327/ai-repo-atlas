# yaroslavyaroslav/OpenAI-sublime-text

⭐ 466 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/yaroslavyaroslav/OpenAI-sublime-text) · 个人维护

**Sublime Text 编辑器的 AI 助手插件，支持多模型对话与补全**

面向 Sublime Text 用户（build 4205+，Python 3.14 插件宿主）的 AI 助手插件：通过命令面板与模型对话，支持 OpenAI Responses、Anthropic Claude、Google Gemini 及 llama.cpp server、ollama、llmman 等 OpenAI 兼容 API。功能含内联 Phantom 回答、整文件/部分文件作为上下文、项目级独立聊天历史、Build/LSP 输出附带提问、SSE 流式输出、图片处理（png/jpg）与代理支持。本地运行时需自行安装 llama.cpp/ollama/llmman 或使用远程 API key。经 Package Control 或 git clone 安装；旧版 Sublime（4050–4204）冻结在 6.1.0 兼容线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 OpenAI/Anthropic/Gemini 及 OpenAI 兼容 API（llama.cpp、ollama、llmman）
- Phantom 内联回答模式，支持 Copy/Append/Replace 操作
- 文件与 Build/LSP 诊断输出可作为请求上下文
- 项目级独立聊天历史与助手配置

## 适用场景

- 在 Sublime Text 内与多种远程或本地模型对话
- 把构建错误或 LSP 诊断发给模型解释和调试
- 在编辑器内联获取模型回答并直接替换或追加代码

## 场景标签

 · 领域:开发工具/编辑器 AI 插件

## 证据(README 行号)

> L8: Works with OpenAI Responses, Anthropic Claude, Google Gemini and the whole zoo of OpenAI-compatible APIs: llama.cpp 
> L25: - Sublime Text build 4205 or newer (Python 3.14 plugin host)
> L65:  * **`OpenAI: Chat Model Select`**: This is the most flexible command. It opens a panel allowing you to:

## 星数曲线

```mermaid
xychart-beta
    title "yaroslavyaroslav/OpenAI-sublime-text 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 465 --> 467
    line [466, 466]
```

2026-10-18 466 → 2026-10-21 466（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1ab679d0133c` · [字段定义](../../DATASET.md)*
