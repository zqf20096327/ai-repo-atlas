# pierridotite/explore-compile-replay

⭐ 4 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/pierridotite/explore-compile-replay) · 个人维护

**AI agent 探索一次、编译为标准测试、在 CI 无模型回放的工具**

ECR 是一个确定性的 agent 测试模式与开放契约：agent 按角色探索应用一次，动作与断言记录为类型化 trace，再编译为普通测试文件（当前为移动端 Maestro flow），在 CI 中无模型、无 token 地回放，每次判定相同。应用变更时由有界 repair 修补失效步骤且不弱化检查。附 trace 格式 JSON Schema、适配器契约、七条法则与一致性检查套件。当前在玩具系统与 demo 移动应用上端到端可跑，尚无 npm 包，iOS 未支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- trace 编译为可独立运行的测试文件，编译与回放均不调用模型
- 有界 repair：补丁只作用于失败步骤，不改变测试断言
- 七条法则（确定性/忠实性/可追溯/无模型等）与逐条一致性检查套件
- 规范以 JSON Schema 发布，定位为任何人可实现的标准

## 适用场景

- 把 agent 探索发现的行为固化为 CI 中可重复运行的测试
- 对移动应用做无模型的确定性回放测试
- 按契约实现自己的适配器并通过一致性套件验证

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18:  Explore once with an agent. The trace is compiled to a test file that runs without ECR and is replayed in CI with 
> L76: ECR is meant to be a standard that anyone can implement, not one tool.
> L97: - **Works today:** the `ecr` command (`validate`, `compile`, `replay`, `repair`, `conformance`), a reference adapte


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `d868cb3c23d1` · [字段定义](../../DATASET.md)*
