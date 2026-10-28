# preambleai/prompt-injector

⭐ 33 · TypeScript · Apache-2.0 · 推送 2026-02-14 · [GitHub](https://github.com/preambleai/prompt-injector) · [官网](https://preamble.com) · 组织维护

**面向安全研究者的 LLM 提示注入测试桌面应用**

Preamble 公司开源的 AI 安全测试 Electron 桌面应用，面向安全研究者、渗透测试人员与 AI 开发者。内置覆盖 OWASP LLM01-LLM10 十类的 100+ 攻击载荷库，可对配置的 LLM（OpenAI/Anthropic/Google/Ollama）执行提示注入、越狱等安全测试并输出成败结果分析。数据本地处理、AES-256 加密存储。macOS/Windows 提供预编译包，Linux 需自行构建。ML 检测、Agent 框架测试等仍在开发或规划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 OWASP LLM01-LLM10 十类的 100+ 攻击载荷库
- 多 AI 提供商接入（OpenAI/Anthropic/Google/Ollama）
- 本地优先架构，敏感数据 AES-256 加密存储
- 实时执行测试并输出成败指示与安全建议

## 适用场景

- 对自家 LLM 应用做提示注入与越狱漏洞评估
- 渗透测试中按 OWASP LLM Top 10 类别执行攻击测试
- 用本地 Ollama 模型免费执行安全测试

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: An AI security testing platform for detecting and mitigating prompt injection vulnerabilities in AI agent solutions
> L19: Prompt Injector is an open-source desktop application for AI security testing, designed specifically for security r
> L24: - **Advanced Attack Engine**: Core testing engine with 100+ OWASP LLM01-LLM10 attack payloads

## 星数曲线

```mermaid
xychart-beta
    title "preambleai/prompt-injector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8120001dd510` · [字段定义](../../DATASET.md)*
