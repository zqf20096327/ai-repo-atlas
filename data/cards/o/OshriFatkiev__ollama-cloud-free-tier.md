# OshriFatkiev/ollama-cloud-free-tier

⭐ 14 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/OshriFatkiev/ollama-cloud-free-tier) · 个人维护

**追踪 Ollama Cloud 模型在免费层可用性的探测清单**

非官方追踪仓库：通过最小 prompt 探测 Ollama 云端模型能否从免费 Ollama 账户调用，以表格记录每个模型的可用状态（✅ 免费 / 🔒 需订阅 / ⚠️ 探测失败）与 Ollama 报告的用量等级。探测脚本用 Python/uv 运行，仅记录模型名、状态、HTTP 状态、检查时间与错误摘要；状态基于免费账户观察，可能随时间变化，未测试的已发现模型不展示。附带手动触发的 GitHub Action 工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以最小 prompt 逐模型探测免费层可用性并生成状态表
- 记录模型名、状态、HTTP 状态、检查时间与脱敏错误摘要
- 提供 discover/probe/render_readme 脚本与手动触发的 GitHub Action
- MIT 许可，探测需设置 OLLAMA_API_KEY

## 适用场景

- 我想知道哪些 Ollama 云模型现在免费账户能用
- 选择免费层可用的云端模型做开发测试
- 跟踪某模型免费可用状态的变化

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: Unofficial tracker for Ollama cloud models that work on the Free Ollama Cloud tier.
> L5: This repo checks whether Ollama cloud models can be used from a Free Ollama account.
> L9: > Can this Ollama cloud model run on Free right now?

## 星数曲线

```mermaid
xychart-beta
    title "OshriFatkiev/ollama-cloud-free-tier 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26", "2026-10-30", "2026-10-31"]
    y-axis "stars" 10 --> 15
    line [11, 12, 13, 14, 14]
```

2026-10-18 11 → 2026-10-31 14（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0cab38823d7b` · [字段定义](../../DATASET.md)*
