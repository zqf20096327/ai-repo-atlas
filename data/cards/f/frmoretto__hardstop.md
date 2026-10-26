# frmoretto/hardstop

⭐ 32 · Python · NOASSERTION · 推送 2026-04-18 · [GitHub](https://github.com/frmoretto/hardstop) · 个人维护

**Claude Code 命令执行前的安全校验插件，拦截危险命令**

面向 AI 编码代理的预执行安全校验工具：在 LLM 与系统 shell 之间以 hook 形式拦截每条命令，Layer 1 用 428 个（会话内加载 262 个）MITRE ATT&CK 映射的正则模式检测破坏性操作、凭据窃取、云 CLI/数据库危险命令，Layer 2 用 LLM 语义分析补充；对文件读取按白名单阻止访问 .ssh/.aws/.env 等凭据文件。策略为 Fail-Closed，不确定时默认阻断。提供 /hs 聊天内控制命令、JSON-lines 审计日志，并支持无 hook 平台的 SKILL.md 软约束模式。已知限制：复杂混淆可绕过正则、代码文件中硬编码密钥不会被拦截。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 428 个检测模式（MITRE ATT&CK 映射）+ LLM 语义分析双层校验
- Fail-Closed：不确定时默认阻断
- Read 工具凭据文件白名单保护（.ssh/.aws/.env 等）
- 审计日志（~/.hardstop/audit.log）与 /hs 聊天内控制命令

## 适用场景

- 在 Claude Code 中防止 AI 误删目录或执行破坏性命令
- 阻止 agent 读取 SSH 密钥、云凭据等敏感文件
- 审查 agent 会话中的安全决策记录

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L16: Pre-execution safety validation for AI coding agents. Validates every shell command against 428 security patterns b
> L24: You trust your AI, but you shouldn't trust it with `rm -rf /` or reading your `~/.aws/credentials`. Hardstop sits b
> L50:     A[Tool Call] --> B{Bash or Read?};

## 星数曲线

```mermaid
xychart-beta
    title "frmoretto/hardstop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fb370082b174` · [字段定义](../../DATASET.md)*
