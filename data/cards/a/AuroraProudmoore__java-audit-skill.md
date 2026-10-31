# AuroraProudmoore/java-audit-skill

⭐ 27 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/AuroraProudmoore/java-audit-skill) · [官网](https://github.com/AuroraProudmoore/java-audit-skill) · 个人维护 · 中文 README

**AI 代码安全审计 Skill：给 LLM 装上资深审计员工作流协议**

面向 Java/Kotlin 与 JavaScript/React/Vue 项目的 LLM 代码安全审计框架：以 SKILL.md 协议与 Python 脚本（语言检测、Java/前端审计脚本）定义 6 阶段审计流水线，含 grep 预扫描、双轨 LLM 审计、覆盖率门禁（T1 文件 100%）、DKTSS 漏洞评分、7 条反幻觉铁律与 CVE 联网核实。可作 OpenClaw Skill 在对话中触发，也可独立运行脚本；脚本需 Python 3.8+ 与 PowerShell 5.0+，Semgrep 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 阶段审计流水线（代码度量→多层审计→覆盖率门禁→漏洞验证→标准化报告）
- 覆盖率门禁按项目规模分级，T1 文件要求 100% 覆盖
- DKTSS 漏洞优先级评分与 7 条反幻觉铁律（CVE 联网核实等）
- 覆盖 Java 反序列化/SQL注入/SSTI 与前端 XSS/原型污染等漏洞类型

## 适用场景

- 对企业 Java 项目做完整的安全审计并生成标准化报告
- 作为 OpenClaw Skill 让 LLM 在对话中执行审计流程
- 挖掘前后端项目的 XSS、反序列化、SSRF 等漏洞

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L20: **Code Audit Skill** 是一个 AI 驱动的多语言代码安全审计框架，将资深安全审计员的方法论编码成 LLM 可执行的工作流协议。
> L184: #### 方式一：作为 OpenClaw Skill 使用（推荐）

## 星数曲线

```mermaid
xychart-beta
    title "AuroraProudmoore/java-audit-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d577173d484c` · [字段定义](../../DATASET.md)*
