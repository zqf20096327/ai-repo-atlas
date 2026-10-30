# Deibiz4/claude-code-template

⭐ 21 · 推送 2026-03-01 · [GitHub](https://github.com/Deibiz4/claude-code-template) · 个人维护

**Claude Code 项目模板：CLAUDE.md、5 个 slash 命令与文档自动化**

面向使用 Claude Code 的开发者的项目模板：提供可复制的 CLAUDE.md 配置（描述项目 stack、命令与约定）、.claudeignore、3 份文档模板（LOGS/CHANGELOG/MANUAL）和 5 个 slash 命令（/log-session、/update-changelog、/document-feature、/session-summary、/new-version），用于自动生成会话日志、变更记录与功能文档。安装方式为 git clone 后复制文件到目标项目并填写占位字段。模板与语言/框架无关，slash 命令可编辑或自建（纯 markdown prompt 文件）。限制：依赖本机已安装 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLAUDE.md + .claudeignore + 3 份文档模板，复制即用
- 5 个 slash 命令自动生成会话日志、CHANGELOG、手册与版本摘要
- slash 命令为 markdown 文件，可编辑或新建自定义命令
- 与语言/框架无关，可应用于新建或已有项目

## 适用场景

- 让 Claude Code 从第一天就理解我的项目结构和约定
- 开发过程中自动维护 LOGS、CHANGELOG 和用户手册
- 团队共享同一份 CLAUDE.md 保证多人上下文一致
- 发版前用 /new-version 汇总变更生成 release 摘要

## 场景标签

`提示工程` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L7: Este template te da una **estructura de proyecto lista para trabajar con Claude Code** desde el primer minuto. En lu
> L9: - Un `CLAUDE.md` que le dice a Claude cómo funciona tu proyecto (stack, comandos, convenciones)
> L10: - **5 slash commands** que automatizan las tareas más repetitivas de documentación

## 星数曲线

```mermaid
xychart-beta
    title "Deibiz4/claude-code-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `42a3a0a989fb` · [字段定义](../../DATASET.md)*
