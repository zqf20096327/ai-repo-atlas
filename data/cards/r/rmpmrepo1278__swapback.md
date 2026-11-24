# rmpmrepo1278/swapback

⭐ 3 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/rmpmrepo1278/swapback) · [官网](https://pypi.org/project/swapback/) · 个人维护

**本地代理：把 PII 替换为占位符后再发给 LLM，回复中还原**

运行在 127.0.0.1:8787 的本地 HTTP 代理，拦截发往 LLM 提供方的请求，将用户名单中的姓名、邮箱、电话、密钥及检测到的电话/邮箱/银行卡/IBAN/API key 替换为类型化占位符，出站二次检查失败则返回 503 阻断（fails closed），回复中的占位符按字节精确还原，覆盖流式与工具调用参数；网络/shell/发送类工具调用默认保留占位符，需显式放行。默认无模型下载，约 7,100 行 Python、3 个核心依赖；可选本地 NER 后端支持 54 种语言。面向在自己客户端与 agent 中保护个人数据的用户。

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

- 发送前 PII 替换、回复字节精确还原，覆盖流式与工具调用
- 出站二次检查，失败即阻断（503），fails closed
- 默认无需下载模型：精确匹配+模式检测，3 个核心依赖
- 可选本地 NER 后端（54 种语言），并提供 selftest 泄漏自测

## 适用场景

- 让 AI agent 处理真实邮件和日历时避免 PII 进入提示词
- 把 OpenAI/Anthropic 客户端的 base_url 指向本地代理即接入
- 为 Claude Code/Codex CLI 配置工具放行策略防止数据外带

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: Python 3.11 or newer. `swapback demo` runs a fake model with made-up data: no key, no network. The proxy listens on
> L44: - **Any OpenAI-compatible client**: OpenAI Chat Completions and Responses (the official SDKs, OpenRouter, LiteLLM
> L46: - **Anthropic Messages**: the Anthropic SDK, plain and streamed, including `tool_use`.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `73df0db450a7` · [字段定义](../../DATASET.md)*
