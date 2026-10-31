# cortad/cortad

⭐ — · [GitHub]() · 组织维护

**AI 应用行为变更评测工具：模拟对话并报告改动影响**

面向 AI 应用开发者的 CLI 评测工具：针对运行中的应用生成模拟用户对话，对每条回复提问并以 yes/no/could not tell/did not come up 四种答案判定，改动后仅重测相关模拟并可对比历史运行，非零退出可门禁 PR。问题可由代码、应用自身 trace、用户自定义函数或带引文校验的模型作答；支持 CI（SARIF/JUnit 输出）、问题包、自有 eval 文件导入。默认写入与判题模型走 open.cortad.com（每日 20 次免费），可用 CORTAD_OFFLINE=1 配合本地模型完全离线。托管版（读取真实用户对话）闭源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按改动文件选择性重测（--changed）并对比保留的历史 run
- 四级问题答案（yes/no/could not tell/did not come up）
- 代码/trace/自定义函数/模型四种作答方式，模型答案需可核验引文
- CORTAD_OFFLINE=1 全离线，代码作答可无模型运行

## 适用场景

- 每次编辑后快速跑 smoke 评测并在 PR 上显示失败行
- 用本地 Ollama 模型离线生成模拟与判题
- 把自己的 eval 表文件转成带仓库地址的模拟套件

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7:  Your coding agent writes the changes. Cortad runs a simulation against your app, asks a set of
> L60: It exits non-zero when a question failed, and when your app answered nothing, so it gates a pull


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b4b7c10c610f` · [字段定义](../../DATASET.md)*
