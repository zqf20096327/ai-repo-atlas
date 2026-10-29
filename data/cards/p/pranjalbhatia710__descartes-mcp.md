# pranjalbhatia710/descartes-mcp

⭐ 21 · Python · MIT · 推送 2026-06-21 · [GitHub](https://github.com/pranjalbhatia710/descartes-mcp) · [官网](https://pranjalbhatia710.github.io/descartes-mcp/) · 个人维护

**给 AI 规划流程的 MCP 服务器：递归质疑计划决策直至收敛**

一个 MCP 服务器，针对用户提交的计划运行递归式“笛卡尔怀疑”循环：起草计划、用 11 种怀疑算子质疑每个承重决策、再质疑怀疑本身、并以真实证据作答（代码疑点读传入 context，世界疑点经 Exa 检索并引用打分，无法落地的标记 NEEDS_HUMAN），循环受最大深度（默认 3）与怀疑预算（默认 64）约束，上限 20 轮，收敛后返回修订计划与需人工决断的少量问题。引擎自动选择：Fireworks 多模型面板、Claude 客户端 sampling、OpenRouter 或无 key 的确定性模板回退。以 Python 包形式安装，接入 Claude Code 等 MCP 客户端使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 递归怀疑循环输出怀疑树（depth+parent）与累积知识库，收敛判据为一轮无新增承重怀疑
- 11 种怀疑算子（assumption/falsify/inversion 等）以数据形式内置于 operators.py
- 四种引擎自动选择，无任何 API key 时仍可在支持 sampling 的客户端上运行
- 提供 doubt/ground/verdict 三个 MCP 工具与 --demo 脚本演示、CI 内置两个基准测试

## 适用场景

- 在 Claude Code 里让 AI 在执行计划前审查每个未检验的假设
- 把计划中需要人工决断的问题从 AI 可自行解决的疑点中分离出来
- 对 AI 生成方案做防幻觉的事前质疑与证据落地

## 场景标签

 · 领域:AI agent 基础设施/规划工具

## 证据(README 行号)

> L15: An MCP server that, on a prompt, **doubts every decision in a plan, doubts its own
> L104: Add this to your Claude Code MCP config (e.g. `.mcp.json` in your project, or via
> L110:     "descartes": {

## 星数曲线

```mermaid
xychart-beta
    title "pranjalbhatia710/descartes-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9dee581cd82c` · [字段定义](../../DATASET.md)*
