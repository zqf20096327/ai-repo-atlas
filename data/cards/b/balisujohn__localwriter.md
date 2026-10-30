# balisujohn/localwriter

⭐ 183 · Python · 推送 2026-02-22 · [GitHub](https://github.com/balisujohn/localwriter) · 个人维护

**为 LibreOffice Writer 添加本地推理生成式编辑的扩展**

LibreOffice Writer 的 .oxt 扩展，提供两个命令：Extend Selection（Ctrl+Q）用语言模型续写选中文本，Edit Selection（Ctrl+E）按用户指令改写、翻译或调整语气。推理后端需自备 text-generation-webui 或 Ollama 之一，通过可配置的 endpoint（默认 localhost:11434）以 completions 或 chat API 调用，支持 OpenAI 兼容端点与 API key。设置经 LibreOffice 内对话框或各平台 localwriter.json 文件配置。面向希望在文档编辑中获得本地 LLM 能力的 Writer 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中即续写（Ctrl+Q）与指令式改写（Ctrl+E）两个命令
- 兼容 text-generation-webui 与 Ollama 后端，支持 OpenAI 兼容端点
- 可配置系统提示词、最大 token 数与 API 类型（completions/chat）
- 以 .oxt 安装包分发，开发者可用 unopkg 从源码直接注册调试

## 适用场景

- 在写邮件或故事时让本地模型续写选中文本
- 改变邮件语气、翻译或按语义修改选段
- 在不联网、本地推理环境下给 Writer 加生成式 AI 功能

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: This is a LibreOffice Writer extension that enables inline generative editing with local inference. It's compatible 
> L19: * This uses a language model to predict what comes after the selected text. There are a lot of ways to use this.

## 星数曲线

```mermaid
xychart-beta
    title "balisujohn/localwriter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 182 --> 184
    line [183, 183]
```

2026-10-18 183 → 2026-10-30 183（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `767444dd78e7` · [字段定义](../../DATASET.md)*
