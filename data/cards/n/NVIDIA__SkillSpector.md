# NVIDIA/SkillSpector

⭐ 27,801 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/NVIDIA/SkillSpector) · [官网](https://docs.nvidia.com/skills/scanning-agent-skills) · 组织维护 · 中文 README

**AI agent 技能安装前的安全扫描器，检测恶意与注入风险**

面向 Claude Code、Codex CLI、Gemini CLI 等使用的 agent 技能包的静态+LLM 两阶段安全扫描工具：覆盖 71 个漏洞模式、17 个类别（提示注入、数据外泄、权限提升、供应链、MCP 工具投毒等），输入支持 Git 仓库、URL、zip、目录或单文件；SC4 查询 OSV.dev 获取 CVE 数据；输出 0-100 风险评分与 Terminal/JSON/Markdown/SARIF 报告；支持递归与批量扫描、基线误报抑制。为 NVIDIA Verified Skills 发布管线的组成部分。默认 LLM 后端指向 DeepSeek，本地模型后端待社区贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 18,102 位贡献者
- 涨星:近 1 天 **+88**(自 20261016 起算)
- 平台:— · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 71 个漏洞模式、17 类别的静态分析，含 AST 危险代码与污点追踪
- 静态分析+可选 LLM 语义评估的两阶段流程
- OSV.dev 实时 CVE 查询与本地快照回退
- MCP 最小权限分析（LP1–LP4）与工具投毒检测（TP1–TP4）

## 适用场景

- 安装 Claude Code / Codex 技能前检测恶意模式与提示注入
- CI 中批量扫描技能集合并对不完整覆盖失败退出
- 对比 MCP Registry 快照发现服务端版本变更
- 审计技能的依赖供应链与包来源重定向行为

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before inst
> L33: - **71 vulnerability patterns** across 17 categories: prompt injection, data exfiltration, privilege escalation, su
> L34: - **Two-stage analysis**: Fast static analysis + optional LLM semantic evaluation

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/SkillSpector 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 20402 --> 28473
    line [21074, 21227, 21571, 22025, 22704, 23038, 23332, 23513, 23672, 23832, 21227, 24898, 25438, 25677, 25877, 26030, 26199, 26446, 26639, 26805, 26947, 27059, 27166, 27290, 27440, 27670, 27801]
```

2026-10-24 21,074 → 2026-11-27 27,801（+6,727）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `5b94b33834ba` · [字段定义](../../DATASET.md)*
