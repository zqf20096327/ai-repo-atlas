# mouna23/OSINT-with-LLM

⭐ 85 · Python · 推送 2025-11-20 · [GitHub](https://github.com/mouna23/OSINT-with-LLM) · [官网](https://mouna23.github.io/OSINT-with-LLM/) · 个人维护

**本地 LLM 驱动的 OSINT 侦察 POC：输入邮箱/域名/IP 自动产出报告**

演示型 Python 项目：接收邮箱、域名或 IP 后自动执行多类侦察（WHOIS、Shodan、SSL 证书校验、VirusTotal 状态、AbuseIPDB 评分、泄露查询），随后用本地 Ollama 运行的 Mistral 模型将技术结果转为人类可读摘要，提取关键发现与风险洞察，并在 /reports/ 目录生成报告。需要配置 VirusTotal、AbuseIPDB、Shodan 三个 API key，本地运行要求 Python 3.13+ 并安装 Ollama 与 Mistral 模型。作者声明仅用于教育目的。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 域名/IP/邮箱三类目标的自动化 OSINT 侦察（WHOIS、Shodan、SSL、VirusTotal、AbuseIPDB、泄露查询）
- 本地 Ollama + Mistral 生成人类可读报告与风险洞察
- 报告保存至 /reports/ 目录

## 适用场景

- 安全研究人员学习 OSINT 侦察与 LLM 报告生成的结合
- 对域名或 IP 做多源信息汇总并生成摘要报告
- 教育场景下演示本地 LLM 在安全分析中的应用

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository demonstrates domain, IP, and email reconnaissance with **LLM-powered** security reporting..
> L34: * Converts technical OSINT into human-readable summaries
> L83: * Install Ollama on your machine and add the MISTRAL model.

## 星数曲线

```mermaid
xychart-beta
    title "mouna23/OSINT-with-LLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-27 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1871b3744224` · [字段定义](../../DATASET.md)*
