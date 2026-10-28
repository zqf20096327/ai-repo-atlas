# retrofor/iamai

⭐ 32 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/retrofor/iamai) · [官网](https://iamai.is-a.dev) · 组织维护 · 中文 README

**跨平台聊天机器人/AI agent 消息运行时框架**

介于聊天平台与应用逻辑之间的消息运行时：适配器层将 Terminal、OneBot 11、Telegram 与 Webhook 流量规范化为 Event/Message 对象；插件层提供命令、规则、权限、依赖注入、中间件与状态会话；Rust 核心加速消息链操作与 OneBot 规范化。Agent 能力（OpenAI 兼容调用、ToolRegistry、审批钩子、AgentTrace、护栏）全部可选，不强制依赖 LLM。另含暂定的 iamai.harness 命名空间，用于可录制、可重放的 agent 实验（试验、轨迹、评估），该部分不属于 1.x 稳定契约。以 Python 包（Rust 核心）分发，MIT 许可。

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

- 多平台适配器（Terminal/OneBot 11/Telegram/Webhook）统一为 Event/Message 规范化对象
- 类型化异步 Python 插件模型：命令、规则、权限、DI、中间件、多后端状态（Memory/JSON/SQLite）
- 可选 Agent 原语：OpenAI 兼容调用、ToolRegistry、审批钩子、追加式 AgentTrace 与输出护栏
- iamai.harness：无头、模型无关的可录制重放 agent 实验框架（Trial/Trajectory/Evaluation）

## 适用场景

- 构建跨 QQ（OneBot）、Telegram 等平台的聊天机器人
- 在统一运行时上叠加带工具调用与轨迹审计的 Agent 插件
- 以可复现的 Trial/Experiment 方式评测 agent 变体
- 以入口点机制发布或复用第三方插件与适配器扩展

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Normalize events once. Run typed async Python plugins, optional agent workflows,
> L38: iamai is a runtime, not an all-in-one bot dashboard. It does not require an LLM, hide the
> L160: |**Agent primitives**|OpenAI-compatible calls, `ToolRegistry`, approval hooks, append-only `AgentTrace`, and outpu

## 星数曲线

```mermaid
xychart-beta
    title "retrofor/iamai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8f929772275b` · [字段定义](../../DATASET.md)*
