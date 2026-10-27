# NoorQureshi/security-skills

⭐ 24 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/NoorQureshi/security-skills) · [官网](https://noorqureshi.github.io/security-skills/) · 个人维护 · 中文 README

**面向 AI agent 的 206 条安全技能库（渗透/赏金/CTF/逆向/防御）**

由 NoorQureshi 维护的开源安全技能库：206 条 SKILL.md 格式的技能页覆盖 web、api、cloud、逆向、防御等 23 个领域，教 agent 何时以及如何驱动 sqlmap、nmap、Ghidra 等既有工具。附带 data/routing.json 路由表（618 个触发用例，CI 验证）供确定性选技能。通过 ./secskills install 自动配置检测到的 agent（Claude Code、Codex、Gemini、Cursor 等），并提供只读浏览器控制台（secskills watch）。基准为对本地 OWASP Juice Shop 解出 116 题中的 9 题。限授权目标使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 206 个技能、23 个领域、618 条 CI 验证的路由触发用例
- 一键安装器自动配置 Claude Code/Codex/Gemini/Cursor 等检测到的 agent
- secskills watch 提供只读浏览器控制台（Attack Map/Findings/Activity）
- 防御类技能含 Sigma 规则与 ATT&CK 检测工程

## 适用场景

- 让 AI agent 按授权范围对目标做侦察与渗透测试并输出报告
- CTF（web/pwn/crypto/rev）解题时加载对应技术页
- 蓝队编写 Sigma 检测规则与 IR 分诊
- 漏洞赏金项目中的覆盖度检查与提交级 writeup

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L4: 206 offensive + defensive techniques your AI agent loads on demand to work an **authorized** target — from recon to 
> L28: It's not a replacement for your toolkit, either: the skills teach your agent when and how to drive the tools you al
> L128: **206 skills across 23 domains.** 🔎 Search them all · or browse CATALOG.md.

## 星数曲线

```mermaid
xychart-beta
    title "NoorQureshi/security-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `02ad9f36e3e3` · [字段定义](../../DATASET.md)*
