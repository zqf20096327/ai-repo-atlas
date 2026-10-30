# gin337/ChatGPTReversed

⭐ 86 · TypeScript · 推送 2025-12-30 · [GitHub](https://github.com/gin337/ChatGPTReversed) · [官网](https://www.npmjs.com/package/chatgptreversed) · 个人维护

**教学向 Node.js 库：逆向 ChatGPT 网页端 API 与前端令牌机制**

作者自述为教育项目，用于学习如何逆向复杂 API：以 ChatGPT 网页端为对象，通过 Chromium DevTools 分析网络请求，逐步讲解会话/CSRF/Requirements/Proof 等令牌的获取流程（含 hash-wasm 哈希与 seed/difficulty 工作量证明）。同时以 npm 包 chatgptreversed 形式提供可实例化的 ChatGPTReversed 类，直接调用 chatgpt.com 后端接口与 LLM 对话。README 更新说明称 OpenAI 已更改前端流程，项目将在数月内更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐步拆解 ChatGPT 前端令牌体系（JWT/CSRF/Requirements/Proof Token）
- 讲解 Proof Token 的 seed+difficulty 哈希生成过程
- 提供 chatgptreversed npm 包可直接实例化调用

## 适用场景

- 学习网页端 API 的逆向分析方法
- 研究 OpenAI 前端的反滥用机制（限流/验证码/工作量证明）
- 在 Node.js 中直接调用 ChatGPT 网页端后端接口

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: Lets keep it simple, this is a educational project to learn to reverse complex API's and understand how they communi
> L8: In this case we take a look at the ChatGPT frontend and reverse engineer the API used to communicate with the LLM.
> L51: So we have all the required tokens to call the conversation endpoint and start a conversation with the LLM.

## 星数曲线

```mermaid
xychart-beta
    title "gin337/ChatGPTReversed 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 84 --> 87
    line [85, 86, 86]
```

2026-10-18 85 → 2026-10-30 86（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cb9ae7c8027b` · [字段定义](../../DATASET.md)*
