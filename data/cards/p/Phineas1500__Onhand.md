# Phineas1500/Onhand

⭐ 31 · JavaScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Phineas1500/Onhand) · [官网](https://useonhand.com) · 组织维护

**浏览器 AI 阅读助手：就当前网页/PDF 提问并定位高亮答案**

Chrome/Firefox 浏览器扩展，作为上下文学习与研究助手：用户在侧边栏就当前打开的网页、PDF 或论文提问，扩展通过约 35 个浏览器工具（提取内容、搜索 PDF、定位引文、滚动到相关位置并高亮、添加笔记）在页面原位给出解释；会话与产物存入扩展 IndexedDB 供回放。模型接入支持 Onhand Free 托管端点（OpenAI GPT-6 Luna，每日限额）、OpenAI Codex OAuth 登录（gpt-5.5 默认）及 OpenAI/Anthropic/Gemini/OpenRouter API key 模式。旧 Electron 桌面应用与 localhost 桥接已移除，仅保留浏览器运行时。开发需 Node.js 22+，用户可从 Chrome Web Store 或 Firefox Add-ons 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 约 35 个浏览器运行时工具：PDF 搜索/读取/跳页/引文定位、页面高亮、笔记、滚动定位
- 三种认证模式：Onhand Free 托管端点、OpenAI Codex OAuth、Provider API key
- 会话与产物存入扩展 IndexedDB，Review 可回放快照/转录
- 语音模式通过 OpenAI Realtime API（GPT-Live 1）与文本共用同一 agent

## 适用场景

- 阅读网页或 PDF 时直接提问并看到答案高亮在原文位置
- 研读论文时让 AI 解释内容并跟踪引文
- 保存学习会话并在之后回放带标注的内容

## 场景标签

`文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: Onhand is a contextual AI assistant for learning and research. The goal is to help users understand what is already 
> L14: - have Onhand point to the relevant place, scroll to it, highlight it, and explain it in context

## 星数曲线

```mermaid
xychart-beta
    title "Phineas1500/Onhand 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8a647a40dafa` · [字段定义](../../DATASET.md)*
