# zzjas/anypoc

⭐ 35 · Python · Apache-2.0 · 推送 2026-05-05 · [GitHub](https://github.com/zzjas/anypoc) · 组织维护

**AI agent 驱动的漏洞发现与可复现 PoC 自动生成工具**

面向安全研究者的漏洞挖掘工具：通过编排本地安装的 Claude Code 或 Codex CLI，在项目专属 Docker 沙箱中执行三阶段流水线——分析器 agent 判定漏洞真伪、生成器 agent 构造最小 PoC、独立 agent 从头复跑验证并记录证据（sanitizer 输出、崩溃回溯等）。扫描器支持三种策略：挖掘 git 历史中 bug-fix 提交并提取模式的 history、按自然语言描述审计的 focused、审查单个 commit/PR 的 commit-pr。无独立 API key，复用已有 CLI 账户凭证；已声明在 Firefox、OpenSSL、FFmpeg 等系统中发现 130+ 漏洞。附 arXiv 论文引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段 PoC 流水线：分析→生成→独立复跑取证
- history/focused/commit-pr 三种扫描策略
- Docker 沙箱隔离，复用本地 claude/codex CLI 凭证，无需独立 API key
- 扫描器与有界 PoC 工作池并发运行，带背压控制

## 适用场景

- 为已有漏洞报告生成可复现的 PoC
- 从提交历史中挖掘内存安全类漏洞并批量生成 PoC
- 合并前审查单个 commit/PR 引入的缺陷

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L91: PoC generation is the "reproduce" half. For each bug report it runs a three-stage pipeline inside a project-specifi
> L93: 1. **Analysis** — An analyzer agent reads the report plus the relevant source and decides whether the bug is real o
> L94: 2. **Generation** — A generator agent crafts a minimal proof-of-concept (crafted input, standalone program, script,

## 星数曲线

```mermaid
xychart-beta
    title "zzjas/anypoc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f53500bcc616` · [字段定义](../../DATASET.md)*
