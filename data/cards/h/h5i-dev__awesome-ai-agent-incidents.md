# h5i-dev/awesome-ai-agent-incidents

⭐ 59 · MIT · 推送 2026-10-15 · [GitHub](https://github.com/h5i-dev/awesome-ai-agent-incidents) · [官网](https://h5i.dev/) · 组织维护

**自主 AI agent 安全事件与攻防对策的策展语料清单**

Awesome 风格的策展清单，汇编针对自主 AI agent 的真实安全事件、攻击技术、CVE 与防御工具。主体为按类别组织的表格：提示注入与目标劫持（含 EchoLeak、CamoLeak 等 CVE 与时间线、影响与参考来源）、供应链攻击（ClawHub 恶意技能、npm 蠕虫、PyPI 后门）、基础设施入侵（Ray 集群利用、OpenAI API 作 C2 通道）。条目附带 CVSS 评分、披露时间与外部引用，面向安全研究者与 agent 系统开发者作为威胁情报检索源，MIT 许可并开放 PR 收录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按提示注入/供应链/基础设施三类组织真实事件表格
- 每条事件附日期、影响与外部参考来源（arXiv、厂商博客、安全媒体）
- 覆盖 CVE 编号与 CVSS 评分的量化条目
- MIT 许可、开放 PR 收录

## 适用场景

- 检索针对 AI agent 的历史攻击事件与 CVE
- 为 agent 系统威胁建模与安全评估收集案例
- 了解提示注入与供应链攻击的已知技术路径

## 场景标签

`精选清单` `网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: **A curated corpus of real-world security incidents, attack techniques, CVEs, frameworks, and defensive tools for au
> L13: ## Real-World Incidents

## 星数曲线

```mermaid
xychart-beta
    title "h5i-dev/awesome-ai-agent-incidents 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-27"]
    y-axis "stars" 56 --> 60
    line [57, 58, 59, 59]
```

2026-10-18 57 → 2026-10-27 59（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6dbefa8abf01` · [字段定义](../../DATASET.md)*
