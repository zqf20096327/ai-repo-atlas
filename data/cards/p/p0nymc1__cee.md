# p0nymc1/cee

⭐ 97 · Go · Apache-2.0 · 推送 2026-08-07 · [GitHub](https://github.com/p0nymc1/cee) · [官网](https://p0nymc1.github.io/cee/) · 个人维护

**Go 编写的确定性优先 agent 工作流执行引擎库**

以 Go 库形式提供的执行引擎：确定性状态机驱动步骤 DAG 执行，LLM 仅在边缘做非结构化输入到结构化字段的抽取，不做流程决策。核心模块零外部依赖，仅用 Go 标准库。支持无代码 JSON manifest 插件与 Go hooks 两级扩展、suspend/resume、预执行只读探针、熔断与补偿；每次运行产出记分卡，`cee diff` 可回放策略变更会翻转哪些历史决策。附带 CLI、浏览器 playground（WebAssembly 编译）与 Docker/HTTP/WASM 等 satellites 后端。README 列出多项当前限制（内置沙箱为进程内模拟、挂起无 TTL 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性状态机驱动执行，LLM 仅做边缘抽取，不做流程决策
- 核心模块零外部依赖，仅用 Go 标准库
- 无代码 JSON manifest 插件 + Go hooks 两级扩展机制
- 运行产出记分卡与插件排行榜，`cee diff` 回放策略变更影响

## 适用场景

- 用现有 handler 集成确定性 agent 工作流（engine.Run / Resume）
- 通过 JSON manifest 以无代码方式定义业务策略与分支
- 回放历史决策，评估规则变更的影响范围
- 以只读探针在副作用步骤执行前进行演练

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: A business-agnostic, deterministic-first execution protocol. A deterministic state machine drives execution; the LLM
> L51: CEE is a library, not a service. Your existing handler calls `engine.Run(...)`; nothing listens on a port by defaul

## 星数曲线

```mermaid
xychart-beta
    title "p0nymc1/cee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-23 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d825119cf40e` · [字段定义](../../DATASET.md)*
