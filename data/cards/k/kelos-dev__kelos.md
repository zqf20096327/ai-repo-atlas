# kelos-dev/kelos

⭐ 346 · Go · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/kelos-dev/kelos) · 组织维护

**在 Kubernetes 上编排自主 AI 编码代理的框架**

Kelos 将编码代理（Claude Code、OpenAI Codex、Google Gemini、OpenCode、Cursor 及自定义代理镜像）转为 Kubernetes 工作负载，为其提供仓库、凭据、工具与计算。核心原语包括 Task、TaskPipeline、Session、Workspace、AgentConfig、TaskSpawner 等，控制器将资源转为 Pods/Jobs/StatefulSets。支持一次性任务、持久会话、事件驱动自动化与流水线，可由 GitHub/Jira/Linear/webhook/定时触发，提供 CLI、可选浏览器 Console 与教代理使用 Kelos 的技能包。要求 Kubernetes 1.28+ 集群与 cert-manager。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将代理转为 Kubernetes 工作负载，资源保持为普通 K8s 对象可纳入 Git 管理
- 支持 Claude Code、Codex、Gemini、OpenCode、Cursor 及自定义代理镜像
- TaskSpawner/SessionSpawner 由 GitHub webhook、Jira、cron 等事件触发代理工作
- Task 状态记录分支、提交、PR 与 token 用量

## 适用场景

- 把编码代理从开发本机迁移到隔离的 Kubernetes 集群运行
- 用 webhook 自动处理仓库 issue 并提交修复 PR
- 跨多个仓库批量执行相同变更
- 从终端或浏览器重连长期运行的代理会话

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3:  Run and orchestrate coding agents on Kubernetes.
> L17: Kelos turns coding agents into Kubernetes workloads. Give an agent a goal and
> L23: Claude Code, OpenAI Codex, Google Gemini, OpenCode, Cursor, and

## 星数曲线

```mermaid
xychart-beta
    title "kelos-dev/kelos 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 343 --> 347
    line [344, 346, 346]
```

2026-10-18 344 → 2026-10-22 346（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `66a3ef20bb27` · [字段定义](../../DATASET.md)*
