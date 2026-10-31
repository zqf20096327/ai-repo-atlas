# ultramancode/spring-ai-privacy-guardrails

⭐ 23 · Java · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/ultramancode/spring-ai-privacy-guardrails) · [官网](https://ultramancode.github.io/spring-ai-privacy-guardrails/) · 个人维护

**给 Spring AI 应用的隐私与安全护栏库：PII 令牌化与工具授权**

面向 Java/Spring 开发者的 Spring AI 扩展库，以 Boot starter 形式接入，提供三项可独立使用的能力：请求级 PII 检测与令牌化（替换后才发给模型）、按工具的最小披露（仅向被授权工具还原原始 PII，工具结果再次保护）、基于 Spring Security 的工具可见性与执行授权。内容检查支持规则、本地 ONNX 分类器或 HTTP guard 模型，PII 检测可选 Presidio 或 JVM 本地 OpenNLP。要求 Java 17+、Spring AI 2.0.0+、Spring Boot 4.0.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PII 检测令牌化后进入模型，工具执行前按需还原原文
- 基于 Spring Security 角色的工具可见性与执行授权
- 内容检查支持规则、本地 ONNX 分类器或 HTTP guard 模型
- PII 检测可选 Presidio 或 JVM 本地 OpenNLP

## 适用场景

- Spring AI 应用中防止 PII 泄露给模型或工具
- 按用户角色限制 agent 可见与可执行的工具
- 对模型请求与响应做内容审查与阻断

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: **Apply privacy protection, tool authorization and content inspection to your application.**
> L26: |Keep detected PII out of the model and allow originals only for selected tools|Privacy|
> L60: ChatClient chatClient(ChatModel chatModel, GuardrailsChatClientFactory guardrailsChatClientFactory) {

## 星数曲线

```mermaid
xychart-beta
    title "ultramancode/spring-ai-privacy-guardrails 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e928d9d5ecf0` · [字段定义](../../DATASET.md)*
