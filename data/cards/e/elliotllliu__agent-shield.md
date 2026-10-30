# elliotllliu/agent-shield

⭐ 15 · TypeScript · MIT · 推送 2026-03-18 · [GitHub](https://github.com/elliotllliu/agent-shield) · [官网](https://www.npmjs.com/package/@elliotllliu/agentshield) · 个人维护 · 中文 README

**AI agent/MCP/Skill 安全扫描器：13 引擎一次扫描一份报告**

针对待安装的 MCP Server、Skill、插件执行安全体检：一条 npx 命令聚合 13 个独立扫描引擎（Semgrep、Trivy、Gitleaks、Bandit、Invariant 等），检测 Skill 劫持、后门、提示注入、工具投毒、数据外传、密钥泄露与依赖 CVE，输出统一报告（可生成 HTML）。内置引擎仅为参照，总体结论由 7 个外部引擎共识决定。首次运行自动将引擎安装到 ~/.agentshield/，无需 sudo。给使用 AI agent 生态、安装第三方组件前需风险评估的开发者使用。

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

- 聚合 13 个独立扫描引擎输出统一报告
- 结论由 7 个外部引擎共识决定，内置引擎仅参照
- 首次运行自动安装引擎到 ~/.agentshield/，无需 sudo
- 支持生成可分享的 HTML 报告

## 适用场景

- 安装第三方 MCP Server 前检查是否窃取 API key 或劫持 agent
- 扫描 Skill/插件中的提示注入与后门
- 生成安全报告与团队分享评估结果

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: **AgentShield answers that in seconds.** One command, 13 independent scanning engines, one clear report.
> L38: |📋 **AgentShield** *(reference)*|AI Agent basics — skill hijack, prompt injection, MCP runtime|

## 星数曲线

```mermaid
xychart-beta
    title "elliotllliu/agent-shield 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ffad6abfea31` · [字段定义](../../DATASET.md)*
