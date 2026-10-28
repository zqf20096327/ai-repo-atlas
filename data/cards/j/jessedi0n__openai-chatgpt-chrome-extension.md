# jessedi0n/openai-chatgpt-chrome-extension

⭐ 71 · JavaScript · MIT · 推送 2026-02-12 · [GitHub](https://github.com/jessedi0n/openai-chatgpt-chrome-extension) · 个人维护

**浏览器工具栏弹出窗口中调用 OpenAI 聊天与图像生成的 Chrome 扩展**

基于 Manifest V3 的 Chrome 扩展，以工具栏弹出窗口形式提供 OpenAI 对话与图像生成：调用 OpenAI Responses API 进行流式聊天、Images API 生成图像，支持模型切换、推理力度选择、web_search 工具开关、最多 6 个文件/图片附件（单个 10 MB）、自定义系统消息，聊天记录与设置存于 chrome.storage.local。无需构建步骤，请求直连 api.openai.com，无独立后端。安装方式为克隆仓库后通过 chrome://extensions 加载未打包扩展，并需用户自行配置 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Responses API 的流式聊天与 Images API 图像生成
- 支持模型切换、模型感知的推理力度选择与 web search 开关
- 文件/图片附件（最多 6 个，单个 10 MB）与自定义系统消息
- 纯 JavaScript/CSS/HTML，无构建步骤，请求直连 OpenAI 无独立后端

## 适用场景

- 在浏览器任意页面快速调用 ChatGPT 对话与图像生成
- 需要 web search 或指定推理力度的轻量 AI 问答
- 不离开当前标签页处理带附件的提问

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L3: A Chrome extension that brings OpenAI chat and image generation into a compact popup.
> L5: The project is built on top of the OpenAI Responses API for chat and the Images API for image generation, with strea

## 星数曲线

```mermaid
xychart-beta
    title "jessedi0n/openai-chatgpt-chrome-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-28 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `adf0aa23a976` · [字段定义](../../DATASET.md)*
