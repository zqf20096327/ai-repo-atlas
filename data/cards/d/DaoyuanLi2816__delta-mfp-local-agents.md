# DaoyuanLi2816/delta-mfp-local-agents

⭐ 51 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/DaoyuanLi2816/delta-mfp-local-agents) · [官网](https://openreview.net/forum?id=KAA8FR6fEq) · 个人维护

**本地工具型 agent 失败轨迹的反事实重放诊断方法与工件**

ICML 2026 FAGEN workshop 论文配套仓库：给定失败轨迹，恢复已保存前缀、采样新延续，按重放失败概率将失败区分为初始态即复现（Prefix-0）、后置前缀跨越阈值（Nontrivial Delta-MFP）、不稳定/无 Delta 等机制。含诊断实现、120 个确定性任务测试床、已发布轨迹与结果，以及无需 GPU 的论文声明验证路径。原始实验用 Ollama 在单卡 RTX 4080 上运行，覆盖 Qwen2.5-7B/14B 与 Llama3.1-8B。作者声明这是受控诊断套件而非总体估计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 恢复保存前缀并估计重放失败概率，输出失败机制分类
- 120 个确定性任务测试床与已发布轨迹/结果
- verify_paper_claims.py 仅凭打包数据即可复现论文计数，无需 GPU/Ollama/网络
- Python 3.10–3.12 CI 覆盖测试、声明验证与工件完整性检查

## 适用场景

- 复现论文的实验计数与图表（无需模型）
- 在本地 Ollama 环境重跑模型观测实验
- 诊断有状态工具型 agent 失败轨迹进入失败机制的位置

## 场景标签

`LLM 可观测性` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L16: Delta-MFP is a counterfactual-replay diagnostic for **stateful tool-use
> L20: repository contains the diagnostic implementation, a 120-task local testbed,
> L36: |**Execution**|Local Ollama inference on a single GPU, with released traces and a fully GPU-free verification path|

## 星数曲线

```mermaid
xychart-beta
    title "DaoyuanLi2816/delta-mfp-local-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2fe64f917e4b` · [字段定义](../../DATASET.md)*
