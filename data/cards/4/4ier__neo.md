# 4ier/neo

⭐ 757 · JavaScript · 推送 2026-04-28 · [GitHub](https://github.com/4ier/neo) · [官网](https://github.com/4ier/neo) · 个人维护

**把任意网页应用变成 API：Chrome 扩展捕获请求供 AI 重放**

Chrome 扩展加 CLI 的组合：扩展常驻拦截浏览器内所有 fetch/XHR 流量（含触发调用的 DOM 元素），neo-schema 命令为域名自动生成 API 结构（端点、鉴权头、参数、响应、错误码）；执行时通过 Chrome DevTools Protocol 在页面上下文内重放调用，自动继承 Cookie/CSRF/会话。v2 增加基于无障碍树的 UI 自动化层，API 不存在时可退回 UI 操作。面向需要让 AI agent 操作网页应用的开发者。捕获范围是 <all_urls>，README 明确列出隐私暴露面与使用建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 被动捕获浏览器 fetch/XHR 流量并自动生成 API schema
- 经 CDP 在页面上下文重放 API，自动继承 Cookie/CSRF/会话
- v2 提供无障碍树 UI 自动化（snapshot/click/fill 等）
- 本地运行：无外部服务器、无遥测，鉴权头捕获时脱敏

## 适用场景

- 让 AI agent 重放网页内部 API 而不依赖官方 API
- 录制并导出某域名的 API 结构供跨设备复用
- API 缺失时通过无障碍树驱动页面 UI 完成操作
- 实时监控浏览器发出的 API 流量

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: Neo is a Chrome extension that passively captures every API call your browser makes, learns the patterns, and lets A
> L16: **Neo is the third way.** Every web app already has a complete internal API — the frontend calls it every time you 
> L111: This gives AI agents a fast, semantic way to interact with any UI. Combine with API capture for a dual-channel app


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f9256ab8d587` · [字段定义](../../DATASET.md)*
