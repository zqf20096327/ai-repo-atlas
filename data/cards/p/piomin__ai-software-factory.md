# piomin/ai-software-factory

⭐ 211 · Dockerfile · 推送 2026-11-24 · [GitHub](https://github.com/piomin/ai-software-factory) · 个人维护

**在 Kubernetes/OpenShift 上将 GitHub issue 自动转为 PR 的自托管工厂**

自托管的软件工厂：GitHub 事件（issue、评论、PR review）经 Tekton Triggers 触发流水线，由 OpenCode 编码代理连接集群内 vLLM 服务的开放模型（Qwen），在新分支上实现 issue 并开启 PR，经人工批准后自动合并，合并后关闭任务 issue 并释放后续任务。提供四条流水线（issue-agent、issue-comment-agent、pr-comment-agent、requirements-agent，后者每小时扫描 requirements 标签）。触发仅接受 OWNER/MEMBER/COLLABORATOR，代码与文本不出集群。限制：需 OpenShift 集群与 GPU 节点（每模型部署 2 GPU、180 GiB 内存），无合并后代码验证，AGENTS.md 规则是唯一质量门。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub 事件经 Tekton 触发，OpenCode 代理自动实现 issue 并开 PR
- vLLM 集群内推理（连续批处理、张量并行），OpenAI 兼容 API，模型可配置切换
- requirements-agent 按依赖顺序拆解任务 issue，最多同时 3 个开放
- GitHub App 短时安装令牌认证，技能经 OCI artifact 版本化管理

## 适用场景

- 让仓库 issue 自动被实现为待审 PR
- 通过 @ai 评论对 issue 下达指令或提问
- 自动拆解需求文档为有序任务并逐个实现
- 代码与提示不出内网的自托管 AI 开发流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A self-hosted "software factory" that turns GitHub issues and comments into pull requests.
> L40: |**vLLM**|High-throughput inference with continuous batching, so parallel agents share one GPU deployment. It serve
> L42: |**OpenCode**|Open-source coding agent that works with any OpenAI-compatible endpoint, so it does not tie the facto


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `a4c79cdeadaf` · [字段定义](../../DATASET.md)*
