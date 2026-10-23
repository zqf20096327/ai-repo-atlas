# kstonekuan/simple-chromium-ai

⭐ 269 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/kstonekuan/simple-chromium-ai) · [官网](https://www.npmjs.com/package/simple-chromium-ai) · 个人维护

**封装 Chrome 内置 AI API 的 TypeScript 轻量库**

面向 Web 开发者的 TypeScript 封装库，包装 Chrome 浏览器内置的 Prompt、Translator、Language Detector、Summarizer 四个 AI API，简化初始化与会话管理：初始化时自动触发模型下载并返回必须使用的对象，提供 Safe 变体返回 Result 类型而非抛异常，支持结构化输出、token 用量检查、会话上下文与取消操作。不暴露流式响应与 Writer/Rewriter/Proofreader API。要求 Chrome 138+（Prompt API 需 148+），设备端模型约 4GB。附 demo 扩展并上架 Chrome Web Store。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 初始化即确保模型已下载，返回必须使用的对象
- Safe API 变体返回 Result 类型而非抛异常
- 支持会话上下文、结构化输出、token 用量检查与取消
- Prompt 与 Summarizer 共享同一约 4GB 底层模型

## 适用场景

- 在网页或 Chrome 扩展中调用浏览器内置 LLM 做问答与文本生成
- 使用浏览器本地翻译、语言检测与摘要功能
- 以类型安全方式快速接入 Chrome 内置 AI 而不处理原生初始化细节

## 场景标签

 · 领域:Web/浏览器开发库

## 证据(README 行号)

> L3: A lightweight TypeScript wrapper for Chrome's built-in AI APIs (Prompt, Translator, Language Detector, and Summarize
> L19: npm install simple-chromium-ai

## 星数曲线

```mermaid
xychart-beta
    title "kstonekuan/simple-chromium-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-23 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a99bca4c95aa` · [字段定义](../../DATASET.md)*
