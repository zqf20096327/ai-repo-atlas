# ashp15205/guardian-runtime

⭐ 20 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/ashp15205/guardian-runtime) · [官网](https://ashp15205.github.io/guardian-runtime/) · 个人维护

**本地 LLM 代理防火墙：拦截提示词防泄密并管控 API 支出**

运行在用户本机的 HTTP 代理，部署在 AI 编程工具与云端 LLM 之间：出站前扫描每条请求，检测 AWS/GitHub/OpenAI/Anthropic 等密钥、Aadhaar/PAN/SSN/信用卡等 PII、40+ 越狱与提示注入模式，命中时在聊天内以 y/n 交互放行或拦截。同时提供每日预算硬上限、会话成本与 token 统计、Terse Mode 注入精简系统提示、PDF/DOCX/XLSX 转 Markdown，兼容 OpenAI/Anthropic/Gemini 原生 API 格式，配离线 Web 仪表盘与 policy.yaml 策略配置。以 pip 包发布，数据全部留在本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 密钥/PII/越狱三类本地扫描，命中时在聊天内 y/n 交互放行
- daily_budget 硬预算上限，拦截会超支的请求
- 同时兼容 OpenAI REST、Anthropic REST 与 Gemini v1beta 原生格式
- 内置离线分析仪表盘与 policy.yaml 策略配置

## 适用场景

- 给 Claude Code / Cursor 等工具加一道防密钥与 PII 外泄的本地关卡
- 给跑在循环里的 agent 设预算上限，避免高额 API 账单
- 本机追踪各 AI 工具的 token 消耗与拦截记录

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L23: Guardian Runtime is a **local HTTP proxy** that runs entirely on your own machine. It sits between your AI coding t
> L66: |08|🌐 **Universal Proxy**|Speaks OpenAI, Anthropic, AND native Gemini (`/v1beta/models/{model}:generateContent`) fo

## 星数曲线

```mermaid
xychart-beta
    title "ashp15205/guardian-runtime 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2de6e6fdda03` · [字段定义](../../DATASET.md)*
