# t3x-dev/t3x-core

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/t3x-dev/t3x-core) · [官网](https://t3x.dev) · 组织维护

**给人与 AI agent 提供结构化状态变更的版本控制**

T3X 是一个结构化状态变更的控制平面：将 YAML 等机器可读状态收敛到统一仓库，支持提案、diff 审查、运行检查、带来源（来源、理由、决策）地提交变更，并提供分支、合并、回滚的可逆历史。人与 agent 走同一审查路径，agent 提案与人工变更同等可审。通过 npx 启动器运行本地 API 与 WebUI，也可 docker compose 自托管；核心引擎 YOps/YSchema/Transition 可独立 npm 使用。当前为 public alpha，WebUI、API、MCP 集成等属于内部或预览层。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 变更绑定来源、理由、检查与决策的可追溯记录
- YOps 声明式 YAML 操作与 YSchema 校验引擎可独立使用
- 分支、合并、回滚的可逆结构化历史
- 人与 agent 共用同一提案-审查-提交路径

## 适用场景

- 管理团队与 AI agent 共同修改的配置/文档状态
- 需要对状态变更做来源追溯与回滚的场景
- 用 YOps/YSchema 在自有流程中应用与校验 YAML 变更

## 场景标签

 · 领域:开发工具/版本控制

## 证据(README 行号)

> L5:  Version control for structured state.
> L16: T3X is a control plane for structured state changes. It gives people and agents
> L51: - **One path for people and agents.** Agent proposals remain as reviewable as


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d703d9ca586e` · [字段定义](../../DATASET.md)*
