# runta-dev/clawshell

⭐ 346 · Rust · Apache-2.0 · 推送 2026-07-13 · [GitHub](https://github.com/runta-dev/clawshell) · [官网](https://clawshell.org) · 组织维护

**为 OpenClaw/Hermes Agent 代理 LLM API 的安全网关，保护密钥与拦截 PII**

Rust 编写的安全特权代理进程，部署在 OpenClaw/Hermes Agent 与上游 LLM API（OpenAI、Anthropic、OpenRouter）之间：将虚拟 API 密钥映射为真实密钥，使 Agent 永不持有真实凭据（真密钥存于 /etc/clawshell，仅 clawshell 系统用户可读）；对请求/响应体做 DLP 正则扫描，按配置 block 或 redact PII；提供发件人白/黑名单的邮件隔离端点、Codex/ChatGPT OAuth 认证与设备码流程、运行统计端点。通过 cargo/npm 安装，sudo clawshell onboard 向导完成接入，内存占用低于 10MB。限制：流式 SSE 响应不做扫描与计数，每次 onboard 只配置一个下游 Agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 虚拟密钥到真实密钥的映射，Agent 不接触真实凭据
- 基于可配置正则的 PII DLP 扫描，支持 block 或 redact
- Gmail/Outlook 预设的发件人过滤邮件隔离端点
- Codex/ChatGPT OAuth 设备码流程与自动 token 刷新

## 适用场景

- 让本地 Agent 在不暴露真实 API 密钥的情况下调用 LLM 服务
- 在请求出站前拦截或脱敏 SSN、信用卡号等敏感数据
- 按发件人规则向 Agent 受控暴露邮箱内容
- 通过 /admin/stats 审计代理请求与 token 用量

## 场景标签

`模型网关` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L14: **ClawShell** is a security-privileged process for the **OpenClaw/Hermes Agent** ecosystem. It sits between OpenCla
> L16: OpenClaw/Hermes Agent never holds real API keys, only virtual keys that ClawShell swaps for real ones before forwar

## 星数曲线

```mermaid
xychart-beta
    title "runta-dev/clawshell 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 344 --> 347
    line [345, 346, 346]
```

2026-10-18 345 → 2026-10-24 346（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `385bae76079e` · [字段定义](../../DATASET.md)*
