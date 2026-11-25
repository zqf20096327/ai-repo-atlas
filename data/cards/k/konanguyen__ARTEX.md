# konanguyen/ARTEX

⭐ 3 · Go · AGPL-3.0 · 推送 2026-11-14 · [GitHub](https://github.com/konanguyen/ARTEX) · 组织维护 · 中文 README

**自主 AI 渗透测试系统：为安全人员自动执行测试任务**

Go 后端 + Next.js 前端的自主渗透测试系统：以任务为单位运行 agent 探索资产图并执行工具调用，产出 findings、执行轨迹与流量记录，支持人工拦截审批与 human-in-the-loop 对话，可从 ScopeSentry 同步资产数据。探索环节需接入 LLM（配置 ANTHROPIC/OPENAI API key 或在 UI 中填写）。运行需 PostgreSQL，提供脚本安装、Docker Compose、二进制与源码构建五种安装/更新路径，支持页面内一键升级与回滚。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 任务执行：可配置 worker 并发数（默认 3），带执行轨迹与探索图展示
- 拦截审批与 human-in-the-loop 对话机制
- 从 ScopeSentry 一键同步资产并合并到资产图
- 支持远程 MCP（Streamable HTTP/SSE）与工具结果防注入边界

## 适用场景

- 对授权目标运行自主渗透测试任务并审阅 findings
- 资产测绘后让 agent 在资产图上探索测试
- 漏洞修复后手动发起复测（Retest）验证

## 场景标签

`网络安全` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Autonomous AI Penetration Testing System (Go backend + Next.js frontend)
> L58: > Requires **PostgreSQL**; exploration requires an **LLM** (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, or configure i


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f84d60a01f2f` · [字段定义](../../DATASET.md)*
