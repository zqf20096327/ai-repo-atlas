# 0dayInc/pwn

⭐ 86 · Ruby · MIT · 推送 2026-10-24 · [GitHub](https://github.com/0dayInc/pwn) · [官网](https://github.com/0dayinc/pwn) · 组织维护

**开源 Ruby 攻击性安全自动化工具包，AI 代理可调用其工具链**

以单一 Ruby gem 形式提供的攻击性安全自动化工具包：67 个插件、48 个 SAST 模块、90 个 AWS 封装、22 个站点驱动、54 个可执行文件，覆盖 OSINT、网络扫描、Web/云测试、硬件与无线电。其上叠加工具调用型 AI 代理（pwn-ai，6 种 LLM 引擎、13 个代理工具集、87 个可调用工具），含强化学习式反馈循环、跨会话错误指纹（~/.pwn/mistakes.json）与多代理 Swarm。同一代码可在 REPL、LLM 工具循环、shell 脚本、CI 与 cron 中运行。安装通过 gem install 加内置 pwn setup 检测包管理器并按 profile 供应外部工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 67 个插件 / 48 个 SAST 模块 / 90 个 AWS 封装 / 87 个 LLM 可调用工具
- pwn-ai 工具调用代理：6 种 LLM 引擎、反馈学习循环、跨会话错误指纹与自动回填修复
- Swarm 多代理：多个 persona 可各用不同 LLM 引擎，经共享 append-only 消息总线通信
- pwn setup 内置 doctor/供应器，按 web/net/sdr 等 profile 安装外部工具并可作 CI 门禁

## 适用场景

- 红队/渗透测试人员在单一工作区编排 OSINT、扫描、Web/云测试与硬件无线电工具
- 通过对话让 AI 代理代为执行侦察、SAST 扫描与漏洞研究流程
- 在 CI 中以 pwn --ai 无人值守运行扫描并汇总高危发现

## 场景标签

`网络安全` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: PWN (pronounced *pone*, like "own" with a p) is an open-source Ruby toolkit for
> L14: radio, reporting, and disclosure. A **tool-calling AI agent** sits on top and
> L40: - live in the REPL
> L42: - in a shell script or CI job

## 星数曲线

```mermaid
xychart-beta
    title "0dayInc/pwn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-27 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `82b55fa3c2e6` · [字段定义](../../DATASET.md)*
