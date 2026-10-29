# rakanssh/hakawati

⭐ 24 · TypeScript · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/rakanssh/hakawati) · [官网](https://hakawati.dev) · 个人维护

**跨平台开源 AI 文字冒险游戏，支持自有 API key 或本地模型**

基于 Tauri 2 的 AI 文字冒险应用，覆盖 Windows、macOS、Linux、Android 与 iOS。提供 Story Teller（自由叙事）与 Game Master（AI 维护物品栏与属性，实验性）两种模式，AI 叙述响应用户行动。模型接入由用户配置：ChatGPT 订阅、OpenRouter/OpenAI 等提供商预设、Generic OpenAI 兼容端点，或 LM Studio/Ollama/LocalAI 本地服务器；应用本身不含模型与 API 额度。故事与场景存于本地 SQLite，可选账户提供云同步与场景发布；场景支持占位符提问与 JSON 导入导出。桌面端提供安装包，移动端与本地构建需 Node.js 与 Rust 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两种游戏模式：自由叙事的 Story Teller 与带物品栏/属性追踪的 Game Master（实验性，需支持工具调用的模型）
- 多提供商接入：ChatGPT 订阅、OpenRouter/OpenAI 预设、Generic OpenAI 兼容端点、LM Studio/Ollama/LocalAI 本地服务器
- 故事与场景本地存储（SQLite），可选账户云同步与场景发布到公共目录
- 场景编辑器支持故事卡片、占位符提问与 JSON 导入导出

## 适用场景

- 用自有 API key 或本地模型进行 AI 文字冒险
- 创建可复用的冒险场景并发布到公共目录
- 通过 Game Master 模式体验带属性与物品栏的角色扮演

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: Hakawati is a free and open-source AI text adventure for Windows, macOS, Linux,
> L10: Android, and iOS. Play with your ChatGPT plan, your own API key, or a local model. Tales and
> L49: Hakawati does not include a model or API credits. Requests go to the provider or

## 星数曲线

```mermaid
xychart-beta
    title "rakanssh/hakawati 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-22 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6dfc62c4c087` · [字段定义](../../DATASET.md)*
