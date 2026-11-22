# gogoymh/git-ontology-agent

⭐ 3 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/gogoymh/git-ontology-agent) · 个人维护

**为 agent 任务提供 git 分支与本体管理的中途请求处理框架**

一个 Python 库：把 agent 运行中的每条新请求开成 git 分支（req/<n>），由决策模型判定新请求与进行中任务的关系（补充/更正/独立/取消/进度），本体以类型化 claim 记录工作状态并维护依赖图，从而只重做受影响的步骤、按类型规则做 claim 级三方合并，并依据 claim 状态生成中间回答与最终回答。答案本身也是提交，可用 git show 回放溯源。零第三方依赖，提供 goa demo 离线演示。

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

- 每请求一个分支，本体依赖图决定只重做受影响的 claim
- claim 类型规则（Constraint 堆叠/Assumption 纠正/Decision 重算等）解决合并冲突
- 中间/最终回答按 claim status（confirmed/in_progress/invalid/superseded）组织措辞
- 答案记录为提交，可精确回放当时的回答依据

## 适用场景

- agent 执行长任务时插入新要求，只重算受影响步骤
- 多个独立请求并行处理并合并结果
- 追溯回答中每条信息来自哪条请求

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: Git lets the agent keep working on one branch while it handles a separate request on another. The ontology tracks d
> L140: |1|Open request?|git|No `req/*` branch open → branch from `main`, go to 4|
> L232: pip install git+https://github.com/gogoymh/git-ontology-agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `64c4fd5dc68d` · [字段定义](../../DATASET.md)*
