# fastly/fastly-agent-toolkit

⭐ 36 · Shell · MIT · 推送 2026-10-22 · [GitHub](https://github.com/fastly/fastly-agent-toolkit) · 组织维护

**给 AI 编码 agent 的 Fastly 平台技能集（12 个技能）**

Fastly 官方维护的 Agent Plugin：以 SKILL.md 加 references 目录的形式提供 12 个技能，覆盖 Fastly 平台操作、CLI、Fiddle 测试、流量统计、NGWAF 审计、VCL 开发（Falco/XVCL）、Compute 本地运行（Viceroy/Fastlike）与参考架构。客户端读取根 plugin.json 清单发现技能。安装方式包括手动复制 .agents/skills/、各 agent 专属插件安装（Claude Code/Codex/Perplexity/Swival/Qwen Code 等）及 skills CLI。插件本身不安装开发工具也不连接 Fastly 账号，各工作流需自备 CLI/curl/jq 等依赖并自行认证。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个技能覆盖 Fastly 平台、CLI、VCL、WAF、统计与 Compute 本地运行
- plugin.json 清单 + skills/ 目录的可移植 Agent Plugin 结构
- 适配 Claude Code、Codex、Perplexity、Swival、Qwen Code、Gemini CLI 等多种 agent 的安装方式
- skills CLI（bunx/npx）支持按技能粒度安装

## 适用场景

- 让 AI 编码 agent 代为操作 Fastly 服务、缓存与 WAF 配置
- 用 Fiddle 对 VCL 做断言式测试与 CI 集成
- 本地开发调试 Fastly Compute 应用
- 审计 NGWAF 防护规则覆盖情况

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A collection of skills for AI coding agents to work with the Fastly platform and edge computing tools.
> L9: This repository is a portable Agent Plugin.
> L31: These skills are intended for coding environments that can read project files and run commands.

## 星数曲线

```mermaid
xychart-beta
    title "fastly/fastly-agent-toolkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-30 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `72a442b75db5` · [字段定义](../../DATASET.md)*
