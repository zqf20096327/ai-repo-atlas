# redscaresu/infrafactory

⭐ 18 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/redscaresu/infrafactory) · [官网](https://github.com/redscaresu/infrafactory) · 个人维护

**用 LLM 按场景生成多云 OpenTofu 代码并以 mock 验证**

面向基础设施工程师的 IaC 生成流水线：用户编写声明意图的 scenario YAML，三阶段 LLM 生成（plan→写 HCL→self-review）产出 OpenTofu 代码，经三层验证（静态 tofu/OPA→mock 部署→真实部署仅限 Scaleway）门控，结构化失败信息回灌到下一轮 prompt 迭代（默认 5 轮）。覆盖 AWS/GCP/Scaleway/Genesys Cloud，各配 mock 服务器，验证可在数秒内完成且无需云凭证。默认经 Claude CLI 驱动，可切换 OpenRouter。附带 44 个训练场景与 SvelteKit Web UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- scenario YAML → 3 阶段 LLM 生成 → 3 层验证 → 失败反馈迭代（默认 5 轮）
- 四个云各配 mock 服务器，亚秒级验证无需云凭证
- 自动学习循环：从真实运行提取 pitfalls 供后续运行使用，CI 拒绝手工条目
- Layer-3 真实部署仅限 Scaleway，凭人手工触发，配置文件不可开启（ADR-0026）

## 适用场景

- 我希望让 LLM 按意图 YAML 生成并通过验证的 Terraform/OpenTofu 代码
- 在不碰真实云 API 的情况下快速迭代 IaC 并调试 apply 失败
- 在 Scaleway 上对生成的栈做真实 apply/探测/销毁与孤儿清扫

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L13: InfraFactory closes that loop. You write a scenario YAML declaring intent (resources + acceptance criteria). The pi
> L117: scenario YAML  ──▶  3-phase LLM generation  ──▶  3-layer validation  ──▶  retry on failure

## 星数曲线

```mermaid
xychart-beta
    title "redscaresu/infrafactory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ea7afc9aefb7` · [字段定义](../../DATASET.md)*
