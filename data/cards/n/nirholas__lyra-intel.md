# nirholas/lyra-intel

⭐ 29 · Python · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/nirholas/lyra-intel) · [官网](https://nirholas.github.io/lyra-intel/) · 个人维护

**面向大规模代码库的分析平台：静态分析+安全扫描+AI 洞察**

Python 3.9+ 的代码库智能分析平台，由 70+ 组件组成：多语言 AST 解析、依赖图、复杂度度量、安全扫描（OWASP/密钥/CVE）、语义搜索、知识图谱与取证分析（死代码、文档缺口、技术债）。AI 层提供代码解释、缺陷检测与重构建议，支持 OpenAI、Anthropic 或本地模型（Ollama/llama.cpp）。运行模式覆盖本地单机、分布式多 worker 与云上自动扩缩（AWS/GCP/Azure），存储可选 SQLite/PostgreSQL/BigQuery；提供 REST API、RBAC、JWT/OAuth 认证与 Web 仪表盘，Docker/Kubernetes 就绪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ 组件：AST 分析、依赖图、复杂度与取证分析
- 安全扫描覆盖 OWASP Top 10、硬编码密钥、50+ 漏洞模式与 CVE 追踪
- AI 分析器支持 OpenAI/Anthropic/本地模型（Ollama/llama.cpp）
- 本地/分布式/云端三种运行模式，SQLite/PostgreSQL/BigQuery 存储可选

## 适用场景

- 扫描数十万行遗留代码的安全漏洞并生成整改计划
- 为团队构建可语义搜索的代码知识库，加速新成员上手
- 规划框架升级：跨包影响分析与迁移步骤
- 按月追踪技术债与代码质量趋势并输出管理层报告

## 场景标签

`网络安全` `语义搜索` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L37: Unlike traditional linters or SonarQube-style tools, Lyra Intel combines:
> L114: - **AI Analyzer** - Code explanation, bug detection, refactoring suggestions. Understand complex code instantly.
> L115: - **Multiple Providers** - OpenAI (GPT-4/3.5), Anthropic (Claude), or Local (Ollama/llama.cpp). Choose what fits y

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/lyra-intel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-30 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `40d6df3d12e5` · [字段定义](../../DATASET.md)*
