# mwilber/zeta-comic-generator

⭐ 13 · PHP · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/mwilber/zeta-comic-generator) · [官网](https://comicgenerator.greenzeta.com/) · 个人维护

**用 AI 生成三格漫画的实验项目，提供在线站与 MCP 服务**

用户输入一两句漫画前提，由 GPT 等多个 AI 模型生成含对白、背景与角色动作的三格漫画脚本，背景文本送图像生成器出图，角色动作从预绘角色素材库选取，最终由 JavaScript 渲染合成漫画。提供公开 MCP 服务器（Streamable HTTP，无需认证），支持 openai/xai/google 三种生成工作流与 8 个工具（生成、浏览、保存、系列查询等），生成受每日配额限制。仓库代码为示例性质，不含 PHP/MySQL 服务端搭建说明；其中的 ComicRenderer/DialogBalloon/CharacterAction 类可独立复用于其他项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型工作流生成三格漫画脚本并合成成图
- 公开远程 MCP 服务器，8 个工具支持生成/浏览/保存/系列查询
- ComicRenderer 等渲染类可独立复制到其他项目使用
- 生成受网站每日配额限制，浏览不受限

## 适用场景

- 输入一句话前提快速生成三格漫画
- 通过 AI 助手（MCP 客户端）内联生成和浏览漫画
- 把 ComicRenderer 复用到自己的漫画渲染项目中

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: An experiment in AI and art to create dynamic comic strips.
> L11: Write a sentence or two describing a premise for the comic strip. GPT, and variaous other AI models, take the premi
> L17: Create and browse Zeta comics from an AI assistant by adding a remote MCP (Model Context Protocol) server with the 

## 星数曲线

```mermaid
xychart-beta
    title "mwilber/zeta-comic-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `315f0d0ec2a0` · [字段定义](../../DATASET.md)*
