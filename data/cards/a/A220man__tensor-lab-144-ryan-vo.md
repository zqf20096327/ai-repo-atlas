# A220man/tensor-lab-144-ryan-vo

⭐ — · [GitHub]() · 个人维护

**校验并修复进攻性安全技能文件合规性的工具**

针对 Agent Skills 规范的 SKILL.md 校验与修复工具：递归解析技能目录，提取 YAML frontmatter，校验必填字段、描述长度上限与 payload 占位符，并可为旧格式生成合规 frontmatter（支持 dry-run）。核心校验逻辑为确定性实现，无需 LLM；LLM 集成为可选，用于生成校验失败的可读解释。提供 React/TypeScript Web 面板、FastAPI REST 接口、Keycloak OIDC 认证与 GitHub Actions CI 集成。当前为进行中的检查点版本，README 提示可能不完整或未通过测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 确定性校验引擎：字段完整性、1024 字符描述上限、attacker.com 占位符检测
- 旧 ## Metadata 格式到合规 YAML frontmatter 的迁移生成（dry-run/apply）
- FastAPI REST 接口与 React+TypeScript Web 面板
- 可选 LLM 集成，支持 openai-compatible/anthropic/gemini/ollama

## 适用场景

- 校验自有技能库是否符合 Agent Skills 规范
- 批量迁移缺少 frontmatter 的旧技能文件
- 在 CI 中阻止技能校验回归

## 场景标签

 · 领域:AI 开发工具/agent 技能校验

## 证据(README 行号)

> L7: **Offensive Security Skill Validator** — A tool for validating and repairing offensive security skill files (SKILL.m
> L28: The validation logic is purely deterministic — no LLM required for core functionality. Optional LLM integration can
> L36: - **Skill Validation** — Scan `Skills/**/SKILL.md` and validate against Agent Skills spec

## 星数曲线

```mermaid
xychart-beta
    title "A220man/tensor-lab-144-ryan-vo 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-23 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `c0e28dbfed37` · [字段定义](../../DATASET.md)*
