# rhysha/claude-security-research-skill

⭐ 22 · Shell · MIT · 推送 2026-04-08 · [GitHub](https://github.com/rhysha/claude-security-research-skill) · 个人维护

**给 Claude Code 的安全研究技能：结构化渗透测试工作流编排**

一个安装到 Claude Code（或任意 Claude MCP 配置）中的安全研究技能包：向 Claude 注入 SKILL.md，使其按 RECON→枚举→漏洞扫描→验证→密钥审计→报告 六阶段组织评估流程，按目标类型路由并编排 nmap、nikto、nuclei、sqlmap 等外部工具的调用顺序。Claude 仅解读工具输出、建议下一步并撰写报告，不生成载荷或漏洞利用代码；每次行动前强制书面授权等四项伦理门检查。面向安全研究员、赏金猎人与安全工程师，通过 git clone 安装，需 Linux/macOS 环境及自装外部工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六阶段结构化评估工作流与按目标类型自动路由
- 编排 nmap/nikto/nuclei/sqlmap/trufflehog 等外部安全工具
- 四项伦理门检查（书面授权/范围界定/私有发现/工具边界），不可跳过
- 统一的发现输出格式与 CRITICAL→INFO 严重度分级

## 适用场景

- 授权测试中让 Claude 编排侦察与漏洞扫描流程并生成专业报告
- 赏金项目里按阶段链接工具完成结构化 recon 与枚举
- 内部安全评估或 CTF 中做漏扫结果分析与下一步建议

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: **A full-spectrum security research skill for Claude** — structured, tool-driven security assessment workflows built
> L9: Drop this skill into Claude Code or any Claude MCP setup and get an AI that thinks like a security researcher: struc
> L100: ├── SKILL.md                    # Core skill definition (loaded by Claude)

## 星数曲线

```mermaid
xychart-beta
    title "rhysha/claude-security-research-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `08a0a0226c1e` · [字段定义](../../DATASET.md)*
