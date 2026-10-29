# code-forge-temple/scribe-pal

⭐ 22 · TypeScript · GPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/code-forge-temple/scribe-pal) · 个人维护

**调用本地 Ollama 的浏览器聊天扩展，保护隐私**

适用于 Chrome/Edge/Firefox 等 Chromium 与 Gecko 浏览器的开源扩展：通过可拖拽的聊天框与局域网内 Ollama 服务通信，实现网页上下文问答。支持捕获选中网页文本（@captured-text）与页面截图（@captured-image，供视觉模型使用）插入对话、文件附件（@attached-files）、提示词自定义、模型选择/下载/删除，以及按模型设置思考开关、采样温度与上下文长度。上下文用量仪表基于 Ollama 报告的精确 token 计数。限制：需本机或局域网自建 Ollama 服务；上下文上限未显式设置时仪表默认按 4096 估算。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页文本/截图捕获与文件附件插入对话（@captured-text/@captured-image/@attached-files）
- 按模型设置思考模式、温度与上下文长度（num_ctx）
- 基于 Ollama 精确 token 计数的上下文用量仪表
- 推理模型可展开查看思考过程面板

## 适用场景

- 浏览网页时对页面内容提问或总结
- 在本地/局域网 Ollama 上私密使用 LLM，数据不出本机
- 捕获页面截图供视觉模型分析

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: ScribePal is an Open Source intelligent browser extension that leverages AI to empower your web experience by provid
> L19: - **AI-powered assistance:** Communicates with an AI service (using ollama) to generate responses.
> L205:  - Use the chat interface to send messages to the Ollama AI service, review conversation history, and manage model

## 星数曲线

```mermaid
xychart-beta
    title "code-forge-temple/scribe-pal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e1d544eb8bde` · [字段定义](../../DATASET.md)*
