# Skull-boy/scyvera

⭐ 25 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Skull-boy/scyvera) · [官网](https://pypi.org/project/scyvera/) · 个人维护

**AI agent 的运行时治理层：声明并强制行为边界**

为 AI agent 提供'操作契约'机制：用 contract.yaml 文件声明 agent 能做什么、需要人工审批什么、不能做什么，并在运行时强制执行（默认拒绝未声明调用），而非仅文档化。工作流为扫描→起草→校验→强制→证明：audit 命令做确定性扫描并生成 Blast Radius 评分，--generate 自动起草契约，ContractEnforcer 在 Python 调用点门控，哈希链注册表提供事后审计证明。提供 Python/TypeScript/Rust 三种运行时实现，共 33 个一致性测试向量，支持 MCP 服务器模式与四种 agent host 的技能集成。

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

- 契约文件声明边界，运行时默认拒绝未声明调用
- audit 扫描生成 Blast Radius 评分并可在 CI 设下限
- Python/TypeScript/Rust 三运行时共享同一一致性语料（33/33）
- 支持 MCP 服务器与 Claude Code/Codex/OpenCode/Antigravity 技能集成

## 适用场景

- 为生产环境 agent 声明工具权限与人工审批边界
- 在 CI 中检查代码是否符合其治理契约
- 事后追溯 agent 实际执行受哪个契约版本约束

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Operational contracts for AI agents: what a system can do, what it can access, and what it must never do — enforced 
> L11: MCP and A2A standardize how agents talk to tools and to each other. Scyvera defines the layer above
> L109: - **Enforce** is default-deny: undeclared calls raise, approval boundaries stop execution, and every


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `0457343a8a1e` · [字段定义](../../DATASET.md)*
