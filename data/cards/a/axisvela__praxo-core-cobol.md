# axisvela/praxo-core-cobol

⭐ 3 · COBOL · MIT · 推送 2026-11-27 · [GitHub](https://github.com/axisvela/praxo-core-cobol) · [官网](https://axisvela.github.io/praxo-core/languages/cobol/) · 组织维护

**给需要在 COBOL 进程内跑 agent 循环的开发者提供嵌入式 agent 框架**

PRAXO-CORE 的 GnuCOBOL 原生实现，以 COBOL 语言实现进程内 agent 循环，包含工具调用、策略、中间件、事件、检查点与人审（HITL）决策机制。模型接入采用 transport seam：OpenAI 兼容、Anthropic、Gemini、MCP 客户端均为 native 能力但由调用方提供传输程序，SSE 流式重组内容与工具调用。仓库为发现镜像，无已发布包，仅源码构建，版本 0.9.0，MIT 许可。README 明确声明其非托管模型、非工作流引擎、非安全控制器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程内 agent 循环，含工具、策略、中间件、事件与检查点
- OpenAI 兼容/Anthropic/Gemini/MCP 客户端为 native transport seam，由调用方提供传输程序
- 带 13 个可运行示例与场景教程（批量异常复核、检查点、HITL、路径策略等）
- 与共享 spec/ 一致性向量和 monorepo CI 合规测试关联

## 适用场景

- 在 COBOL 系统进程内嵌入带策略与检查点的 agent 循环
- 需要人工审批的写入型工具调用（HITL）场景
- 批量作业中把异常记录交给独立复核步骤
- 复用 MCP 客户端在进程内调用工具服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native GnuCOBOL Core: an in-process a
> L23: - OpenAI-compatible model: native (transport seam)
> L118: PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-o


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `d10e9b363074` · [字段定义](../../DATASET.md)*
