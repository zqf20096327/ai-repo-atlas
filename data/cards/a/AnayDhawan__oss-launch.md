# AnayDhawan/oss-launch

⭐ 16 · Shell · NOASSERTION · 推送 2026-09-23 · [GitHub](https://github.com/AnayDhawan/oss-launch) · 个人维护

**让 agent 把裸仓库补齐开源文件的技能（脚手架）**

面向 agent 框架的技能（SKILL.md）：运行 /oss-launch 扫描仓库技术栈与既有文件，报告缺口并仅就不可推断的信息提问，然后生成 LICENSE、README、CONTRIBUTING、SECURITY、CHANGELOG、CI 配置等一整套开源文件，附带 Show HN/Reddit/YouTube 发布模板。以 Claude Code 为日常开发平台，另有面向 Codex CLI、Gemini CLI、Windsurf、Aider 的捆绑包（多数未实测）；提供无 agent 的 headless 模式（apply.sh）与独立 audit.sh。要求 bash 环境，Windows 需 Git Bash/WSL；不覆盖既有文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 扫描→缺口报告→提问→生成开源文件（含 CI 与 issue/PR 模板）的工作流
- audit.sh 输出 16 项缺口清单，可独立于 agent 运行
- apply.sh headless 模式支持无 agent 的 CI/终端执行
- 生成 Show HN/Reddit/YouTube 发布模板与演示 GIF 工具

## 适用场景

- 为自己的项目一键补齐 LICENSE、贡献指南、安全策略等开源文件
- 用 audit.sh 检查仓库开源完备度
- 开源发布时按 playbook 准备公告与演示材料

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L4: Agent harness skill
> L36: This is a skill for agent harnesses. For Claude Code, install it where the harness discovers skills:

## 星数曲线

```mermaid
xychart-beta
    title "AnayDhawan/oss-launch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cdf961d467c4` · [字段定义](../../DATASET.md)*
