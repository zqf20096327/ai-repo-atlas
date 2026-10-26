# mmlong818/lightnovel-studio

⭐ 50 · TypeScript · GPL-3.0 · 推送 2026-06-08 · [GitHub](https://github.com/mmlong818/lightnovel-studio) · 个人维护 · 中文 README

**纯前端中日双语 AI 轻小说生成器，一句话生成全稿**

基于 React 19 / Vite 6 / TypeScript 的纯前端 SPA，无后端：输入一句概念后，AI 依次生成世界观、角色群、章节大纲并逐章写出正文，支持中文与日文轻小说题材。AI 调用通过浏览器直连 Google Gemini、Anthropic Claude、OpenAI 及任意 OpenAI 兼容接口（DeepSeek、Qwen、本地 Ollama 等）。作品数据存于浏览器 localStorage，不经过服务器；提供写作台续写/对话/场景助手与设定审查面板。需自备 API Key，以 npm 构建/开发方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一句话概念依次生成世界观→角色→大纲→逐章正文
- 内置中文题材与日式轻小说题材，中日双语输出
- 多提供商支持：Gemini / Claude / OpenAI / OpenAI 兼容接口（含本地 Ollama）
- 纯前端 SPA，所有作品存于浏览器 localStorage

## 适用场景

- 输入一句点子让 AI 生成整部轻小说草稿
- 用本地 Ollama 或自选 API 在浏览器里写中日双语小说
- 管理角色设定、世界观与章节大纲并做一致性审查

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: > 一句话概念，AI 帮你写出整部轻小说：世界观 → 角色 → 章节大纲 → 逐章正文。
> L24: - 🎯 **一句话生成全稿**：输入一句概念，AI 依次生成世界观、角色群、章节大纲，并逐章写出正文
> L34: React 19 · Vite 6 · TypeScript · Tailwind (CDN)。纯前端 SPA，无后端，AI 调用通过浏览器直连各提供商 API。

## 星数曲线

```mermaid
xychart-beta
    title "mmlong818/lightnovel-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-26 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c152820579d0` · [字段定义](../../DATASET.md)*
