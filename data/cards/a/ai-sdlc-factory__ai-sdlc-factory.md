# ai-sdlc-factory/ai-sdlc-factory

⭐ 25 · C# · MIT · 推送 2026-11-25 · [GitHub](https://github.com/ai-sdlc-factory/ai-sdlc-factory) · [官网](https://ai-sdlc-factory.com) · 组织维护

**给工单打标签即产出已评审 PR 的 AI 软件流水线**

围绕 git 主机（Forgejo 或 GitHub）、Temporal 与一次性 agent 容器构建的软件工厂：在工单上打 `feature`/`bug`/`docs`/`incident` 标签后，角色 agent 在隔离沙箱中分析、写代码或修复，最终交付一个经评审的 pull request，人工负责评审与合并。关键机制包括：代码决定流程走向、agent 仅输出经过校验的 JSON 建议判定；每个 agent 运行在无外网的临时容器中，仅经白名单代理出网。需 Docker (Compose v2)、约 10 GB 磁盘、8 GB 内存及 ChatGPT Plus/Pro 账号；基于 WSL 2 构建测试，其他模型接入方式未经测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四类标签流程：feature/bug/docs/incident 各有专属工作流与验收检查
- bug 修复必须由先失败后通过的测试证明，工厂自行运行该证明
- agent 仅建议（单个校验 JSON 判定），代码决定每个下一步；沙箱容器仅经白名单代理出网
- 通过工单/PR 评论以 /fix、/review、/ask、/retry、/qa 等命令操控流程

## 适用场景

- 给 issue 打 feature 标签，自动产出带分析与评审的 PR
- 提交 bug 后获得由测试证明的修复 PR
- 监控告警自动建单并生成事故评估与缓解选项
- 让只读 agent 回答关于仓库的问题

## 场景标签

`工作流自动化` `代码审查` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L3: **AI SDLC Factory** is an AI software factory built around a git host (Forgejo or GitHub), Temporal and disposable a
> L12: |`feature`|analysis, a check that it is not already built, an optional design review, the implementation, the proje


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bcc704a02e6e` · [字段定义](../../DATASET.md)*
