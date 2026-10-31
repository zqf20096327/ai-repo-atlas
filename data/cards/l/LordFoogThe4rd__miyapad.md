# LordFoogThe4rd/miyapad

⭐ 14 · TypeScript · AGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/LordFoogThe4rd/miyapad) · [官网](https://lordfoogthe4rd.github.io/miyapad/) · 个人维护

**浏览器端 LLM 协作写作界面，支持多后端生成文本**

mikupad 的分支重构版：基于浏览器的语言模型交互界面，面向写作场景提供续写/聊天两种模式。支持 llama.cpp、koboldcpp、AI Horde、DeepSeek 及任意 OpenAI 兼容 API 作为后端；含连接预设管理、会话持久化、Memory/Author's Note/World Info 上下文注入、token 概率悬停查看、Logit Bias、Markdown 渲染、截图生成等功能。可选 Node.js 服务器托管供局域网访问，采用模块化 Parcel 2 + React Context 架构，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多后端支持：llama.cpp / koboldcpp / AI Horde / DeepSeek / OpenAI 兼容 API
- 持久上下文注入（Memory、Author's Note、World Info 关键词触发）
- token 概率悬停展示与从任意 token 重新生成
- 会话持久化与导入导出、连接预设管理

## 适用场景

- 在浏览器中连接本地或远程模型进行 AI 协作写作
- 通过 World Info 与 Author's Note 精细控制生成上下文
- 查看 token 概率并从指定位置重新生成以打磨文本

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Miyapad is a user-friendly, browser-based interface for interacting with language models. It is a fork of mikupad by
> L9: * **Multiple Backends**: Supports **llama.cpp**, **koboldcpp**, **AI Horde**, **DeepSeek** and any **OpenAI Compatib

## 星数曲线

```mermaid
xychart-beta
    title "LordFoogThe4rd/miyapad 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `136d27ba2f63` · [字段定义](../../DATASET.md)*
