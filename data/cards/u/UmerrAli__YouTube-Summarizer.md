# UmerrAli/YouTube-Summarizer

⭐ 16 · JavaScript · MIT · 推送 2025-12-23 · [GitHub](https://github.com/UmerrAli/YouTube-Summarizer) · [官网](https://summarizeyoutube.netlify.app/) · 个人维护

**用 GPT-3.5 生成 YouTube 视频摘要的网页应用**

前后端分离的视频摘要应用：前端为 HTML/CSS/JS（Parcel 打包，npm 启动开发服务器），后端为 Flask，在 config.py 中配置 OpenAI API key，调用 GPT-3.5 生成 YouTube 视频摘要。本地运行需 Node.js 与 Python 两套环境分别启动前后端，并要求后端先于前端运行。提供 Netlify 在线演示链接与视频演示，安装方式为 git clone 源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 OpenAI GPT-3.5 生成视频摘要
- 前端 Parcel + 后端 Flask 的分离架构
- 提供 Netlify 在线演示

## 适用场景

- 不想看完整视频时快速获取 YouTube 视频摘要
- 本地部署并用自己的 OpenAI key 运行摘要服务

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L1: # YouTube Videos Summarizer using OpenAI API
> L3: This project utilizes the power of GPT-3.5 to generate concise and informative summaries for YouTube videos. This re
> L70: Open the config.py file and add your OpenAI API key. If you don't have an API key, you can obtain one from the Open

## 星数曲线

```mermaid
xychart-beta
    title "UmerrAli/YouTube-Summarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c04d11c19c12` · [字段定义](../../DATASET.md)*
