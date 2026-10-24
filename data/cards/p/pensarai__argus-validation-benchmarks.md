# pensarai/argus-validation-benchmarks

⭐ 66 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/pensarai/argus-validation-benchmarks) · 组织维护

**面向 AI 渗透测试 agent 的评测基准集（71 渗透 + 10 威胁建模）**

Pensar 开源的攻防安全评测基准套件：71 个自包含 Docker 化渗透测试靶标（每个含特定漏洞与 flag，覆盖注入、认证绕过、SSRF、沙箱逃逸、OT/ICS、供应链等多步攻击链，横跨 Node.js/Python/Java/Go/PHP/Ruby 技术栈）与 10 个含已知答案的威胁建模应用（agent 读源码产出结构化威胁模型，按 ground-truth.json 评分）。为评估其自研 agent Apex 而建，供社区评测任意自动化渗透系统。运行需 Docker/Docker Compose 与 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 71 个 Docker 化渗透靶标，含难度分级（1-3）与漏洞类别/技术栈覆盖表
- 10 个威胁建模基准：agent 读源码生成威胁模型，对照 ground-truth.json 评分
- runner 中立的 benchmark.json v2 清单契约，记录防御、隔离边界与里程碑证据
- 附清单校验脚本 validate-benchmarks-v2.py，无需安装依赖即可校验

## 适用场景

- 评测自动化渗透测试 agent 的漏洞发现与利用能力
- 评测 AI 生成威胁模型的质量
- 考察 agent 在沙箱逃逸、OT/ICS、供应链等场景的多步攻击能力

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: > The most comprehensive open benchmark suite for evaluating AI-powered penetration testing agents -- 71 pentesting 
> L20: Built by Pensar to evaluate Apex, our AI-powered autonomous penetration testing agent, and open-sourced so the broa

## 星数曲线

```mermaid
xychart-beta
    title "pensarai/argus-validation-benchmarks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-24 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2c27e86c6be0` · [字段定义](../../DATASET.md)*
