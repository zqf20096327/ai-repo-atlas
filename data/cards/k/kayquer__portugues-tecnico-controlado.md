# kayquer/portugues-tecnico-controlado

⭐ 14 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/kayquer/portugues-tecnico-controlado) · [官网](https://kayquer.github.io/portugues-tecnico-controlado/) · 个人维护

**Claude Code 技能：按 9 条规则将巴西葡萄牙语技术文本改写为单义版本**

一个以 Markdown 规则形式提供的 agent 技能（Skill），将巴西葡萄牙语技术文本改写为"只有一种读法"的受控语言。规则 PTC-1 至 PTC-9 覆盖消歧、一致性与信号三类，灵感来自航空业 ASD-STE100 但为葡萄牙语重写；支持 estrito/leve 等严格度分级与人类/agent 双受众，输出违规对照表、最终文本与待确认项清单，并提供 EN/PT 双语模式（只在完整版存在）。无任何依赖（无包、无网络调用），git clone 到 ~/.claude/skills 即装；另提供 dist/ 扁平化版本适配 Cursor、Codex、ChatGPT、Perplexity、Kimi 等工具。

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

- 9 条受控语言规则（PTC-1~9），按消歧/一致性/信号三组组织
- 输出违规规则对照表、改写文本与"待确认"信息缺口清单，不擅自补全事实
- 三种严格度分级 + 人类/agent 受众模式（agent 模式禁止指代跨句）
- EN/PT 双语模式：用葡语规则反向暴露英语原文的歧义

## 适用场景

- 把 runbook、操作手册改写成给 agent 或执行者无歧义消费的文本
- 统一团队技术文档的巴西葡语术语与数字/日期格式
- 产出供 LLM 流水线消费的状态/指令文本，避免事件与状态歧义

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: O **Português Técnico Controlado (PTC)** é uma skill do Claude Code que reescreve texto técnico em português do Bras
> L165: O Claude Code registra a skill na próxima sessão. Sem dependências: nenhum pacote, nenhuma outra skill, nenhuma ch
> L169: As regras são Markdown puro e não dependem do Claude Code. O que depende dele é o empacotamento — frontmatter YAML


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `23109a4e9e73` · [字段定义](../../DATASET.md)*
