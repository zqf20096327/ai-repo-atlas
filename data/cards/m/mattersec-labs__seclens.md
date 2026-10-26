# mattersec-labs/seclens

⭐ 42 · Python · 推送 2026-08-01 · [GitHub](https://github.com/mattersec-labs/seclens) · [官网](https://mattersec-labs.github.io/seclens/) · 组织维护

**按角色视角评测 LLM 漏洞检测能力的基准（406 个 CVE 任务）**

SecLens 是一个基于 406 个真实 CVE 任务（来自 93 个开源项目、10 种语言）的 LLM 漏洞检测基准，覆盖 Code-in-Prompt 推理与 Tool-Use 两层评测。核心机制是通过 CISO、首席 AI 官、安全研究员、工程负责人、AI Agent 五种利益相关者的权重配置，把 35 个度量维度聚合成 0-100 的角色决策分（A-F 等级）；同一模型在不同角色下分差可达 31 分。以 Python 3.13 + uv 的 CLI 工具形式提供，附 arXiv 论文与文档，面向安全评测与研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 406 个 CVE 任务，成对包含漏洞版与补丁后版本，8 类 OWASP 对齐类别
- 5 种角色权重配置产出独立决策分，量化角色分歧
- 35 个维度覆盖检测、覆盖率、推理、效率、工具使用、风险、鲁棒性 7 类
- 提供 run/summary/report/compare CLI 命令与按角色生成报告

## 适用场景

- 按自己角色（如 CISO 或工程负责人）选择适合的漏洞检测模型
- 对模型做成本与质量（MCC/美元）权衡评估
- 学术研究中引用并复现角色化安全评测结果

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L15: SecLens is a benchmark that evaluates LLMs on real-world vulnerability detection using confirmed CVEs from open-sou
> L88: SecLens evaluates models in two layers, then scores through role-specific weight profiles:
> L116: |`seclens run`|Evaluate a model on CVE tasks|

## 星数曲线

```mermaid
xychart-beta
    title "mattersec-labs/seclens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `935fb3fe50aa` · [字段定义](../../DATASET.md)*
