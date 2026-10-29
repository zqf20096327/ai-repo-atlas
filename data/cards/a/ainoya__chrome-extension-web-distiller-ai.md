# ainoya/chrome-extension-web-distiller-ai

⭐ 20 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ainoya/chrome-extension-web-distiller-ai) · [官网](https://chromewebstore.google.com/detail/web-distiller-ai/ooaogogbdciochplilffdihffdijakfk) · 个人维护

**用 Chrome 内置 Gemini Nano 网页摘要的浏览器扩展**

基于 React 实现的 Chrome 扩展：读取当前网页，用 Readability 抽取正文、Turndown 转为 Markdown，再通过 window.ai 调用 Chrome 内置的 Gemini Nano 在浏览器内完成摘要，可将结果翻译为英文或日文，输出附带标题与 URL 的 Markdown 链接并可复制。要求使用 Chrome Canary 并启用内置 Gemini Nano；当前仅从页面开头截取内容以适配上下文长度限制，不支持全文摘要。提供源码构建与 releases 中的 dist.zip 两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 window.ai 调用 Chrome 内置 Gemini Nano，摘要过程不外发网络请求
- Readability 抽取正文并转为 Markdown
- 摘要可翻译为英文或日文
- 输出含标题与 URL 的 Markdown 链接并支持一键复制

## 适用场景

- 浏览网页时快速获取当前页面的本地摘要
- 将摘要翻译成英文或日文阅读
- 复制带来源链接的摘要用于笔记或分享

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: This Chrome extension provides a summary of web page contents using the built-in Gemini Nano model. It is implemente
> L17: - Calls Gemini Nano via `window.ai` for summarization.
> L23: - Using Chrome Canary Release.

## 星数曲线

```mermaid
xychart-beta
    title "ainoya/chrome-extension-web-distiller-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `25c53f9978ae` · [字段定义](../../DATASET.md)*
