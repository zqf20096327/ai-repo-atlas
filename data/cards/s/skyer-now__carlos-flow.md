# skyer-now/carlos-flow

⭐ 3 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/skyer-now/carlos-flow) · [官网](https://github.com/skyer-now/carlos-flow#readme) · 个人维护 · 中文 README

**为 AI 编码 Agent 提供机械门禁的工作流工具，约束执行范围与验证**

面向 Windows 的 AI 编程门禁工具，以单一 npm 包形式为现有 AI 编码工具提供流程约束：留痕开卡、角色派发、真实命令验证、双轴独立审查、审计与一键还原，规则写入代码而非提示词。技术机制包括 enforceScope 越界拦截、Fail-Closed 严格退化、4KB 输出折叠落盘、MCP Progress 心跳通知与快照生命周期隔离。当前仅声明支持 Windows，macOS/Linux 未经验证。

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

- enforceScope 全域越界硬拦截，覆盖暂存区与未跟踪文件
- 真实 spawn 执行测试命令，无通过证据不允许完工
- 4KB 单流输出折叠与私有目录落盘，30 份/7 天轮转清理
- MCP 协议 Progress 心跳，长任务推送执行进度

## 适用场景

- 限制 AI 编码助手只能改动指定范围的代码
- 防止 AI 汇报未经真实执行的测试结果
- 长耗时测试运行时向客户端反馈进度避免误判超时

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L22: **Carlos 工作流是面向 Windows 的 AI 编程卫士**，为现有 AI 编程工具提供**“机械防撞护栏”**、**“通信优化保护”**与**“通俗智能向导”**。
> L92: 直接使用标准 MCP 协议，通过对话让 AI 助手调用门禁工具链。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6a45c77a548f` · [字段定义](../../DATASET.md)*
