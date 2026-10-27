# OWASP/www-project-promptme

⭐ 43 · Python · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/OWASP/www-project-promptme) · [官网](https://owasp.org/www-project-promptme/) · 组织维护

**演示 OWASP LLM Top 10 安全漏洞的故意脆弱教学应用**

OWASP 维护的教育项目：基于 Python 与 Ollama 框架和开源模型（mistral、llama3、sqlcoder、granite 系列等）构建的故意脆弱 Web 应用，包含 10 个源自 OWASP LLM Top 10 的 CTF 式动手挑战，每题有目标、可选提示与通关 flag，并提供面向初学者的题解。面向 AI 安全从业者学习漏洞发现与缓解策略，无需 API key，支持 macOS/Linux（Windows 支持开发中），README 提示应在虚拟或沙箱环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个基于 OWASP LLM Top 10 的 CTF 挑战
- 基于 Ollama 与开源模型，无需 API key
- 提供挑战题解（Spoilers）与回归测试（pytest）
- 官方建议在沙箱环境运行（故意含不安全代码）

## 适用场景

- AI 安全从业者练习发现与利用 LLM 漏洞
- 学习 LLM Top 10 漏洞的缓解策略
- 以 CTF 形式开展 LLM 安全培训

## 场景标签

`网络安全` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: PromptMe is an educational project that showcases security vulnerabilities in large language models (LLMs) and their
> L13: The project is primarily developed using Python and the Ollama framework, with the open source LLM models. The exer

## 星数曲线

```mermaid
xychart-beta
    title "OWASP/www-project-promptme 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `05b2062cff5e` · [字段定义](../../DATASET.md)*
