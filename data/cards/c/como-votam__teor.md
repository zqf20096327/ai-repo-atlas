# como-votam/teor

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/como-votam/teor) · [官网](https://teor.comovotam.com.br) · 个人维护

**面向巴西立法流程的 LLM 开放基准测试**

由 Como Votam 发布的开放基准，评估 LLM 在巴西立法流程相关任务上的表现，按事实理解、预测、工具使用三条轨道分别发布指标，不合并为单一分数。答案来自官方来源，语义保真依赖人工评审。基于 inspect-ai 构建，通过 uv 安装并按 provider extra 接入各模型；离线评估与数据构建不需要 API key。仓库不包含原始数据、本地预测与私有答案，仅发布显式导出的产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条轨道（事实理解/预测/工具使用）分别计分，不合并单一分数
- 答案来自官方来源，语义保真依赖人工评审
- 运行前强制预算上限与价格文件（teor run --help）
- 离线评估与数据构建无需 API key

## 适用场景

- 评估 LLM 在巴西立法文本任务上的能力
- 研究者复现基准并按轨道查看指标
- 通过 CLI 构建数据与提交评估运行

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmark aberto de LLMs sobre o processo legislativo brasileiro, por Como Votam.
> L5: O Teor separa compreensão factual, previsão e uso de ferramentas. Publica métricas por trilha; não transforma tarefa


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `7ea344193f9e` · [字段定义](../../DATASET.md)*
