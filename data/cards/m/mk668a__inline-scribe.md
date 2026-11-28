# mk668a/inline-scribe

⭐ 10 · TypeScript · MIT · 推送 2026-06-25 · [GitHub](https://github.com/mk668a/inline-scribe) · [官网](https://chromewebstore.google.com/detail/inline-scribe/kmcgponcdfdpbmkahiolhnignkkpnkgm) · 个人维护

**本地 AI 校对浏览器输入的 Chrome 扩展，文本不出本机**

Chrome 扩展，在任何网页文本框按 Alt+G 触发校对，以 Track-Changes 风格的 diff 面板逐条接受或拒绝修改，支持选区校对与只读文本剪贴板回写。默认使用 Chrome 内置 Gemini Nano，可切换到任意 OpenAI 兼容本地端点（默认 Ollama llama3.2）；LLM 只返回纠正文本，diff 由扩展内确定性词级算法计算。通过 declarativeNetRequest 剥离 Origin 头解决 Ollama CORS 403。可选用 Harper 规则引擎做前置机械修正。无遥测、无服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Alt+G 触发逐条 accept/reject 的内联 diff 校对面板
- 默认 Chrome 内置 Gemini Nano，可选任意 OpenAI 兼容本地端点
- 经 declarativeNetRequest 剥离 Origin 头，原生 ollama serve 即可用
- 可选 Harper WASM 规则引擎前置处理机械性错误

## 适用场景

- 在 Gmail、GitHub 评论框等网页输入框里校对文字且不上传文本
- 处理公司保密文档、未发布代码等不能走云端校对的写作
- 只校对长邮件中的一段选区文字

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: **A Chrome extension that proofreads what you write in the browser, using an AI that runs on your own computer.** Pr
> L27: By default inline-scribe uses **Chrome's built-in Gemini Nano** — there is nothing to
> L121: - **The LLM never produces the diff.** Small local models are great at fixing prose and


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6572c9e6c24a` · [字段定义](../../DATASET.md)*
