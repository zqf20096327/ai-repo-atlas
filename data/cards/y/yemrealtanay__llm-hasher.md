# yemrealtanay/llm-hasher

⭐ 23 · Go · MIT · 推送 2026-04-11 · [GitHub](https://github.com/yemrealtanay/llm-hasher) · 个人维护

**LLM 管线中的 PII 令牌化中间件：发送前脱敏、返回时还原**

以 HTTP 服务或 Go 库形式嵌入应用与 LLM 之间的隐私中间件：先在本地检测敏感数据（正则处理信用卡/邮箱/电话/IBAN/IP，Ollama 本地模型处理姓名/地址/证件号），用不透明令牌替换后送入 LLM，响应经 /v1/detokenize 还原原值。令牌映射存于 SQLite 并以 AES-256-GCM 加密，支持 context_id 作用域、TTL、批量并行处理与按上下文硬删除（合规/被遗忘权场景）。运行依赖 Docker Compose（含 Ollama）或 Go 1.25+，约需 4GB 内存；LLM 检测延迟 2-8 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正则 + 本地 Ollama LLM 混合检测 10 种 PII 类型
- AES-256-GCM 加密的 SQLite 令牌金库，密钥不离开进程
- tokenize/detokenize/batch API 与按 context 的硬删除
- 可作独立 HTTP 服务或 Go 库嵌入使用

## 适用场景

- 把客服通话/工单送 LLM 分析前先脱敏，避免明文 PII 外泄
- 数据库只存令牌化文本，需要时按 context_id 还原
- 配合合规/被遗忘权要求批量删除某上下文的全部映射

## 场景标签

 · 领域:LLM 基础设施/数据隐私

## 证据(README 行号)

> L3: **Privacy-first PII tokenization middleware for LLM pipelines.**
> L19: **llm-hasher sits between your app and the LLM.** It strips sensitive data, sends clean tokens, and puts the real v
> L42: - **Local PII detection** — uses Ollama running on your own server, no data leaves your infra for detection

## 星数曲线

```mermaid
xychart-beta
    title "yemrealtanay/llm-hasher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f83628a1e9ff` · [字段定义](../../DATASET.md)*
