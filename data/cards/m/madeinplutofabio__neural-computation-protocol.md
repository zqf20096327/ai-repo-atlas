# madeinplutofabio/neural-computation-protocol

⭐ 15 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/madeinplutofabio/neural-computation-protocol) · [官网](https://crates.io/crates/ncp-runtime) · 个人维护

**把 agent 例行任务改为确定性 WASM 计算的开源协议与运行时**

面向平台/AI 工程师与 SRE 团队的 agent 基础设施：定义 NCP 协议（v0.2.3），将无文件系统、无网络、默认确定性的纯函数 WASM 计算单元（Brick）连成有类型边与路由策略的有向图，由 Rust 参考运行时（Wasmtime 43）沙箱执行并强制资源上限、产出可回放 trace。通过 ncp-mcp-server 接入 MCP 兼容宿主，通过 ncp-langgraph 作为 LangGraph 节点使用，从而减少 LLM 调用量与延迟。协议不自动识别或替换 LLM 调用，需开发者自行拆分快慢路径；提供 JSON Schema、验证器与一致性向量，Phase 3 集成分发阶段进行中。

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

- Brick 为沙箱化 WASM 纯函数：无文件系统/网络、默认确定性
- 图执行带类型边、路由策略、阈值门控与资源上限，产出可回放 trace
- MCP 适配器（每个 graph 暴露为一个 MCP 工具）与 LangGraph 节点封装包
- 协议含规范、JSON Schema、验证器与一致性测试向量

## 适用场景

- 把高频 agent 工作流中的确定性任务移出 LLM 调用以降低成本与延迟
- 为支持工单分流等混合场景构建确定性快路径加 LLM 升级路径
- 以可回放 trace 审计与复现 agent 决策过程
- 通过 MCP 或 LangGraph 在既有 agent 栈中调用 NCP 图

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L36: NCP is an open protocol + reference implementation for building **agentic systems from small, sandboxed WASM functi
> L17: NCP works alongside your existing agent stack through MCP and LangGraph.

## 星数曲线

```mermaid
xychart-beta
    title "madeinplutofabio/neural-computation-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e5edad90fbfd` · [字段定义](../../DATASET.md)*
