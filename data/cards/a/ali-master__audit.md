# ali-master/audit

⭐ 25 · TypeScript · MIT · 推送 2026-06-19 · [GitHub](https://github.com/ali-master/audit) · [官网](https://audit.usestrict.dev) · 个人维护

**给安全工程师的 8 阶段 AI 漏洞挖掘 agent 工具**

基于 Bun + TypeScript 与官方 Claude Agent SDK 的命令行工具，用多个并行窄域 agent 对代码库做漏洞发现：每个 agent 只查一类攻击面，另一模型对抗性复核，再以可达性（attacker 能否从外部触达 sink）作为最终门槛，输出 Schema 校验的结构化报告。计费走 Claude Pro/Max 订阅，支持 OpenRouter/Anthropic 兼容网关。支持 PR diff 扫描、基线增量、SARIF 输出、CI 门禁、opt-in 自动修复与漏洞赏金分诊。全局安装需 Bun ≥ 1.3 运行时；agent 有 Bash 权限且非 OS 沙箱，对不可信代码需在一次性 VM/容器中运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 阶段流水线：Recon→Hunt→Validate→Gapfill→Dedupe→Trace→Feedback→Report
- Validate 阶段由不同模型尝试证伪每条发现，可达性作为报告门槛
- PR/diff 扫描 + 基线指纹 + SARIF 输出 + --fail-on 严重度门禁
- 通过 Claude Pro/Max 订阅计费，无需 API key；支持 OpenRouter 网关

## 适用场景

- 对代码库做自动化漏洞发现并生成带可达性链路的报告
- 在每个 PR 上只扫描变更文件并对新增高危问题阻断构建
- 复现并分诊漏洞赏金/VDP 提交，输出接受/拒绝/重复判定

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3:  An 8-stage AI vulnerability-discovery agent.
> L12: `audit` finds real vulnerabilities in a codebase by running **many narrow agents
> L14: exactly one attack class; a **different model** then tries to *disprove* every

## 星数曲线

```mermaid
xychart-beta
    title "ali-master/audit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c13455dbcb73` · [字段定义](../../DATASET.md)*
