# ktol1/RedTeam-Agent

⭐ 78 · C · 推送 2026-04-24 · [GitHub](https://github.com/ktol1/RedTeam-Agent) · [官网](https://github.com/ktol1/RedTeam-MCP) · 个人维护 · 中文 README

**AI 驱动的自动化红队/内网渗透框架，经 MCP 与技能文件编排 15+ 渗透工具**

面向安全审计人员的红队自动化框架：以技能优先的终端工作流运行，AI 客户端读取仓库内 SKILL.md 与 copilot-instructions.md 技能文件，自主发现并调用 gogo、fscan、nuclei、impacket、SharpHound、nxc 等 15+ 渗透工具执行终端命令，再汇总高价值发现。覆盖侦察、AD 信息收集、攻击与横向移动全链路，通过输出过滤与文件优先策略控制 token 消耗。支持 Cursor、Claude Desktop、VS Code/Cline 多客户端接入，经 git clone 源码安装，要求 Python 3.8+ 与 8GB+ 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 技能驱动的终端工作流：AI 读技能文件后自主编排执行命令
- 15+ 渗透工具矩阵（网络扫描/Web/AD/横向移动）带自动配置
- BloodHound + impacket + Responder 的 AD 攻击链覆盖
- 输出过滤、截断与文件优先策略优化 token 消耗

## 适用场景

- 授权渗透测试中让 AI 端到端编排扫描与漏洞验证
- 域渗透场景下自动完成信息收集、攻击路径分析与横向移动
- 在 Cursor/Claude Desktop 等现有 AI 客户端中直接调用安全工具链

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L18: RedTeam-Agent is an AI-powered red team framework using a skill-first terminal workflow. AI reads project skills, d
> L20: Core philosophy: no manual tool-by-tool operation. Let AI orchestrate the workflow end-to-end.
> L83: AI will read the repository skill and `.github/copilot-instructions.md`, then execute terminal commands directly.

## 星数曲线

```mermaid
xychart-beta
    title "ktol1/RedTeam-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3af836ddf7a0` · [字段定义](../../DATASET.md)*
