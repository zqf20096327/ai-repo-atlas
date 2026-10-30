# anmolksachan/LLMInjector

⭐ 50 · Python · Apache-2.0 · 推送 2026-04-06 · [GitHub](https://github.com/anmolksachan/LLMInjector) · [官网](https://medium.com/@anmolksachan/i-built-a-burp-suite-extension-to-automate-llm-prompt-injection-testing-b4add8a11774) · 个人维护

**Burp Suite 扩展：自动化 LLM 提示注入渗透测试**

面向渗透测试人员与安全工程师的 Burp Suite 扩展（Jython 2.7），对与 LLM 交互的 HTTP 端点自动注入提示。核心机制：§ 标记或自动 JSON 递归遍历定位注入点，解析后重序列化以保证 JSON/OData 完整性；v4 增加响应 diff、密钥/token 提取（JWT、API key、AWS key 等）、header 与 multipart 注入、SSE 流式响应重组、1–10 并行线程、Burp Collaborator OOB 检测，并生成自包含 HTML 报告。安装需 Burp Suite Pro/Community 与 Jython standalone JAR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- § 标记定位与递归 JSON 遍历两种注入模式，JSON 往返校验防止请求损坏
- 响应 diff、token/密钥提取、SSE 流式响应重组
- 200+ prompt 库（GitHub 拉取/本地导入/自建）与跨会话命中统计
- 一键 HTML 报告与 JSON 导出，支持 Burp Collaborator OOB 检测

## 适用场景

- 对 LLM 后端 API 做提示注入渗透测试
- 检测响应中泄露的 API key、JWT 等密钥
- 生成客户可交付的 HTML 渗透测试报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **Burp Suite Extension for Automated LLM Prompt Injection Testing**
> L20: LLM Injector is a Burp Suite extension that automates prompt injection testing against any HTTP endpoint that inter

## 星数曲线

```mermaid
xychart-beta
    title "anmolksachan/LLMInjector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e45247347b7a` · [字段定义](../../DATASET.md)*
