# NK2552003/Select2AI_Extension

⭐ 19 · JavaScript · MIT · 推送 2026-04-26 · [GitHub](https://github.com/NK2552003/Select2AI_Extension) · 个人维护

**网页划词调用 GitHub Models AI 的浏览器扩展**

基于 Manifest V3 的浏览器扩展（Chrome/Edge/Firefox）：用户在任意网页选中文本后从浮动菜单选择总结、解释、回答或自定义提问，响应显示在浮动窗口中。通过用户自行配置的 GitHub Models API Token 调用模型，Token 存储于浏览器本地。v2.0 增加弹窗面板、历史与知识库标签、流式输出、模型对比模式、代码分析（解释/找 bug/重构/语言转换）、翻译与多轮对话等。以源码加载方式安装，商店版未发布。

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

- 网页划词触发总结/解释/回答/自定义提问
- v2.0 提供流式输出、多模型对比、代码分析与多轮对话
- API Token 存储于浏览器本地，需用户自行配置 GitHub Models Token
- 支持 LaTeX/KaTeX 数学公式渲染与亮/暗主题

## 适用场景

- 阅读网页或代码时选中内容即时获取 AI 解释或总结
- 在浏览器内对选中文本提问、翻译或做代码分析
- 收藏 AI 回答到本地知识库并搜索历史记录

## 场景标签

`AI 助手` `聊天机器人` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L6: A powerful browser extension that lets you select text on any webpage and interact with GitHub Models AI directly fr
> L52: 2. Enter your **GitHub Models API Token**
> L86: ├── background.js          # Service worker for API calls

## 星数曲线

```mermaid
xychart-beta
    title "NK2552003/Select2AI_Extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `07eb3e748f44` · [字段定义](../../DATASET.md)*
