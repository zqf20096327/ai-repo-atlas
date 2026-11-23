# ArthurQQQQ/yuelao-chatgpt-plugin

⭐ 5 · Python · 推送 2026-11-16 · [GitHub](https://github.com/ArthurQQQQ/yuelao-chatgpt-plugin) · [官网](https://yuelao-trial-feedback.arthurqiu50.chatgpt.site/) · 个人维护 · 中文 README

**面向中文用户的多聊法月老连麦对话插件，可检索相似连麦案例**

以 ChatGPT MCP 插件形式运行的婚恋对话原型：提供 8 种取材于中文月老连麦直播的 AI 聊法，可按四象限选择、通过四道场景题匹配或点名切换。提示词控制接话方式并支持改判；RAG 工具从 33 条原片记录、41 张案例卡中检索相似片段，给出带时码的原片链接。完整逐字稿与音视频存于本机，说话人归属待人工核听。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 种可选、可比较、可中途切换的月老聊法（四象限分类）
- RAG 案例检索：33 条原片记录、41 张短卡，附可跳转时码
- 四道场景题库，借鉴 MBTI 与 SBTI 的选题方式
- 只读 MCP 工具：场景题匹配、案例查询、证据卡展示

## 适用场景

- 在 ChatGPT 中以特定连麦聊法讨论自己的情感处境
- 对同一件事比较不同主播风格的接话方式
- 遇到具体情境时查看相似连麦片段与原片出处

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L25: **同一件事，换个人接下一句，你愿不愿意继续讲？** 这是我们做月老连麦时想回答的问题。我们把这些接话动作做成可以选择、比较和切换的 AI 聊法。对话里需要例子时，插件会查案例库，给出相似片段和能跳到对应秒数的原片链接。
> L64: 提示词决定怎样接话，用户补充新事实时可以改判。工具负责场景题匹配、查询案例和展示证据卡。RAG 优先找相同主播的短卡，必要时用索引里的词项补找候选。每张卡保存来访情境、接话动作和原片时码。仓库内有 **33 条原片记录和 41 张
> L117: Prompts guide how the model responds and when it updates its view. The read-only MCP tools match a style, search f

## 星数曲线

```mermaid
xychart-beta
    title "ArthurQQQQ/yuelao-chatgpt-plugin 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-23"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-21 5 → 2026-11-23 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `744f0bac2834` · [字段定义](../../DATASET.md)*
