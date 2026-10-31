# codexmark/kram

⭐ 13 · Go · MIT · 推送 2026-10-16 · [GitHub](https://github.com/codexmark/kram) · 个人维护

**Go 编写的本地优先编码 agent 运行时与多供应商 LLM 网关**

单一 Go 二进制（CGO_ENABLED=0）交付的终端编码 agent 运行时，同时内置多供应商 LLM 网关、持久化 daemon 与 TUI。agent 可检视代码、编辑文件、运行命令与测试、使用 LSP/MCP、跨会话记忆，模型调用经统一网关路由到多个供应商或本地 OpenAI 兼容服务。路由实现先做资格过滤（熔断/能力检查）再评分，支持 prompt 前缀亲和、有界流式回退、上下文预算与产物溢写。会话与状态保存在本机。当前为 Public Beta，跨平台行为与供应商兼容性仍在稳定中。安装为预编译二进制加校验和验证，覆盖 Linux/macOS/Windows/Termux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单进程启动网关、daemon、agent 循环与 TUI，组件可独立运行
- 路由先资格过滤再评分，支持 prompt 前缀亲和与有界流式回退
- 上下文预算策略：确定性输出过滤、产物溢写、结构性修剪与限额压缩
- 单 Go 二进制分发，安装器校验 SHA-256，无需 Go 工具链与 root

## 适用场景

- 在终端里让 agent 在项目内读码、改文件、跑测试完成开发任务
- 把模型调用路由到多个供应商或本地 OpenAI 兼容服务，避免绑定单一厂商
- 追踪整个回合的路由决策与尝试轨迹（Ctrl+R）

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L40: Kram is a terminal-native coding agent designed to do real work inside a project: inspect code, edit files, run com
> L48: One process starts the complete runtime — gateway, durable daemon, agent loop, and TUI — while keeping those compon
> L54: - **Provider independence.** The agent talks to one normalized gateway instead of embedding provider-specific behav

## 星数曲线

```mermaid
xychart-beta
    title "codexmark/kram 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5bb438822989` · [字段定义](../../DATASET.md)*
