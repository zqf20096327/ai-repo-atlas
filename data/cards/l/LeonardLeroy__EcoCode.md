# LeonardLeroy/EcoCode

⭐ 21 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/LeonardLeroy/EcoCode) · 个人维护

**离线运行的 Python 代码能耗/性能剖析 CLI，可选 AI 优化建议**

面向 Python 开发者的 CLI 工具：剖析脚本的 CPU 时间、内存峰值与估算能耗，建立基线并检测回归，扫描整个仓库（覆盖 Python、C/C++、C#、Rust、JS/TS 等语言），输出 JSON/SARIF 供 CI 门禁使用。建议功能默认为确定性规则引擎，完全离线无需 API key；AI 建议为可选，支持本地 Ollama 或远程 Anthropic（需自带 key，仅从环境变量读取）。另有 VS Code 扩展 EcoCode Insights 提供内联诊断与仪表盘。通过 pipx 或 venv 以 pip 安装，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 剖析 CPU/内存/估算能耗并标注 measured/estimated 区分实测与推测
- 基线对比检测性能与能耗回归，JSON/SARIF 导出接入 CI
- 多语言仓库扫描（Python、C/C++、C#、Rust、JS/TS、HTML/CSS、汇编）
- 可选 AI 建议：本地 Ollama 或远程 Anthropic，默认规则引擎全离线

## 适用场景

- 我想知道这次改动是否让代码变慢或更耗能
- 在 CI 中像测试和 lint 一样对能耗回归做门禁
- 找出仓库里最值得优先优化的文件

## 场景标签

 · 领域:开发者工具/性能与能耗剖析

## 证据(README 行号)

> L8: **For Python developers who want to know if their code got slower or greener — without guessing.** EcoCode profiles 
> L95: EcoCode works fully offline with deterministic, rule-based suggestions — **no API key needed**. AI-powered suggesti
> L97: - **Local (Ollama):** a model runs on your machine; your code never leaves it; no key. The endpoint is configurable

## 星数曲线

```mermaid
xychart-beta
    title "LeonardLeroy/EcoCode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7d2ff0ecd35a` · [字段定义](../../DATASET.md)*
