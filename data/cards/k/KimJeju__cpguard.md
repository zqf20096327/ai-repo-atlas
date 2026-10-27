# KimJeju/cpguard

⭐ 24 · Python · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/KimJeju/cpguard) · 个人维护

**离线 CPG 污点分析 SAST 工具：扫描到审计报告一站式交付**

面向安全分析人员的静态代码审计工具：tree-sitter 解析→语言中立 IR→代码属性图（AST/CFG/def-use/call）→带函数摘要的跨过程污点分析，覆盖 11 种语言、78 条规则，另含模式类检测（硬编码密钥、弱加密等）。提供三栏审查界面（Source→Sink 流可视化、裁决与批注）、按韩国 MOIS/电子金融/OWASP Top 10 等标准生成 PDF/Word/xlsx/SARIF 交付物，支持批量扫描与项目组合管理。LLM 三诊（Claude/ChatGPT/Gemini，可选厂商）用于复核可达性，另提供 MCP server 供 AI agent 驱动扫描与动态验证探针。Windows 提供安装包，三平台可 pip 从源码运行，全程离线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPG + 函数摘要的跨过程污点分析（11 语言、78 规则）
- 人机审查界面：裁决继承、按流内容过滤、相似问题分组
- 按 MOIS/OWASP Top 10/CWE 等标准生成 PDF/Word/xlsx/SARIF 交付物
- LLM 三诊可选 Claude/ChatGPT/Gemini；MCP server 供 agent 驱动与探针 oracle 验证

## 适用场景

- 对客户源码做安全评估并产出可直接交付的审计报告
- 在 CI/CD 中扫描并按严重度门禁拦截新漏洞
- 批量管理数百个项目的扫描与复核状态
- 让 AI 编码 agent 通过 MCP 拉取证据并动态验证漏洞可达性

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L25: **tree-sitter parsing → language-neutral IR → CPG (AST · CFG · def-use · call) → interprocedural taint with functio
> L81: - Claude · ChatGPT (OpenAI) · Gemini. Re-verifies findings for reachability and explains them; provider and model a
> L91: - **Offline, clean-machine install** — a single exe (PyInstaller + Inno Setup); no Python, no internet, no admin ri

## 星数曲线

```mermaid
xychart-beta
    title "KimJeju/cpguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b40bdec17486` · [字段定义](../../DATASET.md)*
