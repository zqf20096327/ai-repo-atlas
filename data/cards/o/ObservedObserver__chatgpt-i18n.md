# ObservedObserver/chatgpt-i18n

⭐ 805 · TypeScript · AGPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/ObservedObserver/chatgpt-i18n) · [官网](https://www.i18n.ing/) · 个人维护

**用 LLM 翻译本地化 locale 文件的 Web 应用**

基于 ChatGPT 类模型的 i18n 翻译工具：读取项目 locale 文件，通过 AI 翻译并在 Web 编辑器中查看与编辑，支持一次导出多个 locale 文件；将大 JSON 拆分为小块以避免模型破坏 JSON 结构（该功能作者标注仍在开发中，服务较慢且可能超出 Vercel FaaS 限制）。后端使用 OpenAI SDK 配合 OpenRouter，需 Node.js 22，自行部署到 Vercel 运行；浏览器端翻译使用设置中保存的 key，与后端环境独立。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 翻译 locale 文件并配套 Web 编辑器
- 一次导出多个 locale 文件
- 大 JSON 分块处理以避免模型破坏结构（WIP）
- 后端 OpenAI SDK + OpenRouter，Azure 设置仍受支持

## 适用场景

- 为网站或应用的多语言 locale 文件做 AI 辅助翻译
- 在 Web 编辑器中查看和修改翻译结果并批量导出
- 自行部署到 Vercel 供团队使用

## 场景标签

 · 领域:本地化/翻译工具

## 证据(README 行号)

> L3: Translate your locale files with AI Assistance.
> L28: Requires Node.js 22. The backend uses OpenAI SDK 7 with OpenRouter.

## 星数曲线

```mermaid
xychart-beta
    title "ObservedObserver/chatgpt-i18n 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 804 --> 806
    line [805, 805]
```

2026-10-18 805 → 2026-10-22 805（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d1faa0e9c3fe` · [字段定义](../../DATASET.md)*
